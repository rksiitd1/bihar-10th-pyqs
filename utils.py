import os
import logging
import time
import threading
import random
import re
import google.generativeai as genai
from logging.handlers import RotatingFileHandler
import pathlib
from dotenv import load_dotenv
import json
import hashlib
from datetime import datetime, timedelta, timezone

# Load environment variables
load_dotenv()

# --- Time-Aware API Key State ---
# IST timezone offset
IST = timezone(timedelta(hours=5, minutes=30))

# State file to persist key exhaustion data
KEY_STATE_FILE = pathlib.Path("logs/api_key_state.json")

# In-memory exhaustion state: {key_hash: {"exhausted_at": str, "available_after": str}}
_key_exhaustion_state = {}

# --- Logging Configuration ---
def setup_logger(name, log_file, level=logging.INFO):
    """Function to setup as many loggers as you want"""
    
    # Create logs directory if it doesn't exist
    log_path = pathlib.Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    
    # File Handler
    handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5, encoding='utf-8')
    handler.setFormatter(formatter)

    # Console Handler (Optional: Keep it if user wants *some* feedback, or remove if they want silence)
    # User said "not get printed in the terminal... otherwise this will lead to frustration"
    # So we will limit console output to INFO/WARNING/ERROR, or maybe just critical.
    # But usually a progress bar or minimal status is good.
    # I'll keep a console handler but maybe we can control what goes there.
    # For now, I will mirror to console but the main goal is to HAVE the logs in file.
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    
    # Avoid adding handlers multiple times
    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(console_handler)

    return logger

# Global logger for this module
# We can use specific loggers in scripts
# logger = setup_logger('pipeline_utils', 'logs/pipeline.log')

# --- API Management ---

API_KEYS = []
# 1. Start with the explicit GOOGLE_API_KEY if present
if os.environ.get('GOOGLE_API_KEY'):
    API_KEYS.append(os.environ.get('GOOGLE_API_KEY'))

# 2. Scan all environment variables for other keys starting with "AIza"
for key, value in os.environ.items():
    if value and value.startswith('AIza') and value not in API_KEYS:
        API_KEYS.append(value)

# Fallback
if not API_KEYS:
     print("⚠️ No Google API keys found in environment variables!")

# Remove duplicates
API_KEYS = list(dict.fromkeys(API_KEYS))
print(f"🔑 Found {len(API_KEYS)} API Keys available for rotation.")

# Global state for rotation
_rotation_lock = threading.Lock()
_global_call_count = 0
_current_key_index = 0

# --- Time-Aware Key Management Functions ---

def _get_key_hash(key: str) -> str:
    """Returns a short hash of the API key for safe logging."""
    return hashlib.sha256(key.encode()).hexdigest()[:8]

def _get_next_reset_time() -> datetime:
    """Returns next midnight IST as the reset time."""
    now = datetime.now(IST)
    # Next midnight IST
    tomorrow = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
    return tomorrow

def _load_key_state():
    """Loads exhaustion state from JSON file."""
    global _key_exhaustion_state
    if KEY_STATE_FILE.exists():
        try:
            with open(KEY_STATE_FILE, 'r', encoding='utf-8') as f:
                _key_exhaustion_state = json.load(f)
            # Clean up expired entries
            now = datetime.now(IST)
            to_remove = []
            for key_hash, state in _key_exhaustion_state.items():
                available_after = datetime.fromisoformat(state.get("available_after", ""))
                if now >= available_after:
                    to_remove.append(key_hash)
            for key_hash in to_remove:
                del _key_exhaustion_state[key_hash]
            if to_remove:
                _save_key_state()
        except Exception as e:
            print(f"⚠️ Failed to load key state: {e}")
            _key_exhaustion_state = {}

def _save_key_state():
    """Persists exhaustion state to JSON file."""
    KEY_STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        with open(KEY_STATE_FILE, 'w', encoding='utf-8') as f:
            json.dump(_key_exhaustion_state, f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️ Failed to save key state: {e}")

def _mark_key_exhausted(key_index: int, logger=None):
    """Marks a key as exhausted with timestamp."""
    if key_index < 0 or key_index >= len(API_KEYS):
        return
    
    key = API_KEYS[key_index]
    key_hash = _get_key_hash(key)
    now = datetime.now(IST)
    reset_time = _get_next_reset_time()
    
    _key_exhaustion_state[key_hash] = {
        "exhausted_at": now.isoformat(),
        "available_after": reset_time.isoformat(),
        "key_index": key_index
    }
    _save_key_state()
    
    msg = f"🚫 Key {key_index} ({key_hash}) exhausted. Available after {reset_time.strftime('%Y-%m-%d %H:%M IST')}"
    if logger:
        logger.warning(msg)
    else:
        print(msg)

def _is_key_available(key_index: int) -> bool:
    """Checks if a key is available (not exhausted or cooldown expired)."""
    if key_index < 0 or key_index >= len(API_KEYS):
        return False
    
    key = API_KEYS[key_index]
    key_hash = _get_key_hash(key)
    
    if key_hash not in _key_exhaustion_state:
        return True
    
    now = datetime.now(IST)
    available_after = datetime.fromisoformat(_key_exhaustion_state[key_hash].get("available_after", ""))
    
    if now >= available_after:
        # Key is available again, remove from exhaustion state
        del _key_exhaustion_state[key_hash]
        _save_key_state()
        return True
    
    return False

def _get_next_available_key(start_index: int = 0, logger=None) -> int:
    """Finds the next available key starting from start_index. Returns -1 if all exhausted."""
    for offset in range(len(API_KEYS)):
        idx = (start_index + offset) % len(API_KEYS)
        if _is_key_available(idx):
            return idx
    
    # All keys exhausted
    msg = "❌ All API keys are exhausted! No available keys until quota reset."
    if logger:
        logger.error(msg)
    else:
        print(msg)
    return -1

def get_available_key_count() -> int:
    """Returns the number of currently available API keys."""
    return sum(1 for i in range(len(API_KEYS)) if _is_key_available(i))

# Load key state on module import
_load_key_state()
print(f"🔓 {get_available_key_count()}/{len(API_KEYS)} API keys currently available.")

def configure_genai(api_key=None):
    """Configures Gemini. If no key provided, uses current global key."""
    if api_key:
        genai.configure(api_key=api_key)
    else:
        with _rotation_lock:
            key = API_KEYS[_current_key_index] if API_KEYS else None
        if key:
            genai.configure(api_key=key)

def rotate_api_key(logger=None, mark_current_exhausted=False):
    """Manual rotation with time-aware exhaustion tracking."""
    global _current_key_index
    with _rotation_lock:
        # Optionally mark current key as exhausted
        if mark_current_exhausted:
            _mark_key_exhausted(_current_key_index, logger)
        
        # Find next available key
        next_idx = _get_next_available_key((_current_key_index + 1) % len(API_KEYS), logger)
        if next_idx == -1:
            msg = "❌ No available API keys! All keys exhausted until reset."
            if logger: logger.error(msg)
            else: print(msg)
            return None
        
        _current_key_index = next_idx
        key = API_KEYS[_current_key_index]
    
    msg = f"🔄 Rotation to Key Index {_current_key_index} ({get_available_key_count()} keys available)"
    if logger: logger.info(msg)
    else: print(msg)
    return key

class RotatableModel:
    """
    A wrapper around genai.GenerativeModel that handles automatic API key rotation
    using global state, so all instances share the rotation counter.
    """
    def __init__(self, model_name, rotation_threshold=20):
        self.model_name = model_name
        self.rotation_threshold = rotation_threshold
        self.local_model = None
        self.last_known_key_idx = -1
        self._ensure_model_sync()

    def _ensure_model_sync(self):
        """Checks if global key index changed, updates local model if so."""
        global _current_key_index
        with _rotation_lock:
            target_idx = _current_key_index
            target_key = API_KEYS[target_idx] if API_KEYS else None
        
        if not target_key:
            return

        # If we aren't synced with the global key index, re-create the model
        if self.last_known_key_idx != target_idx or self.local_model is None:
             # Configure specifically for this switch
             genai.configure(api_key=target_key)
             self.local_model = genai.GenerativeModel(self.model_name)
             self.last_known_key_idx = target_idx
             # print(f"🔄 Synced to Key Index {target_idx}")

    def generate_content(self, *args, **kwargs):
        global _global_call_count, _current_key_index
        
        with _rotation_lock:
            _global_call_count += 1
            # Rotate after every 'rotation_threshold' calls globally
            if _global_call_count > 0 and _global_call_count % self.rotation_threshold == 0:
                 # Find next available key (skip exhausted ones)
                 next_idx = _get_next_available_key((_current_key_index + 1) % len(API_KEYS))
                 if next_idx != -1:
                     _current_key_index = next_idx
                     print(f"🔄 Global Rotation: Switching to Key Index {_current_key_index} (Total Calls: {_global_call_count}, Available: {get_available_key_count()})")
        
        # Ensure we are using the up-to-date key before generation
        self._ensure_model_sync()
        
        return self.local_model.generate_content(*args, **kwargs)

def get_generative_model(model_name="models/gemini-3-flash-preview"):
    """Returns a configured RotatableModel instance."""
    return RotatableModel(model_name=model_name)

def generate_content_with_retry(model, prompt_parts, logger=None, max_retries=5):
    """
    Generates content using the provided model with retry logic.
    Supports RotatableModel.
    
    Args:
        model: The Google GenAI model instance (or RotatableModel).
        prompt_parts: The prompt or parts to send.
        logger: Optional logger instance.
        max_retries: Maximum number of retries.
        
    Returns:
        response object or None if failed.
    """
    global _current_key_index
    response = None
    
    for attempt in range(max_retries):
        try:
            # Add safety settings to avoid blocking on educational content
            safety_settings = [
                {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
            ]
            response = model.generate_content(prompt_parts, safety_settings=safety_settings)
            
            # Simple validation to ensure response isn't empty on a successful HTTP 200
            if not response.text: 
                raise ValueError("Empty response text")
                
            return response
        except Exception as e:
            error_str = str(e)
            msg = f"⚠️ Attempt {attempt+1}/{max_retries} failed: {e}"
            if logger: logger.warning(msg)
            else: print(msg)
            
            # Use exponential backoff for all errors
            wait_time = (2 ** attempt) + random.uniform(1, 4) 
            
            if "429" in error_str or "Resource has been exhausted" in error_str:
                # Mark current key as exhausted and rotate to next available
                with _rotation_lock:
                    _mark_key_exhausted(_current_key_index, logger)
                    next_idx = _get_next_available_key((_current_key_index + 1) % len(API_KEYS), logger)
                    if next_idx != -1:
                        _current_key_index = next_idx
                        msg = f"🚫 Key exhausted! Switched to Key {next_idx}. Retrying in {wait_time:.1f}s..."
                    else:
                        msg = f"❌ All keys exhausted! Waiting {wait_time:.1f}s before retry..."
            else:
                msg = f"⏳ Error occurred. Retrying in {wait_time:.1f}s..."
                
            if logger: logger.info(msg)
            else: print(msg)
            time.sleep(wait_time)
                
    if not response:
        msg = "❌ All retries failed."
        if logger: logger.error(msg)
        else: print(msg)
        return None
    
    return response

# --- Data Processing ---

def clean_json_response(raw_text: str) -> str:
    """Extracts JSON content from a string, handling markdown code blocks and repairing common issues."""
    match = re.search(r'```json\s*([\s\S]*?)\s*```', raw_text, re.DOTALL)
    if match:
        text = match.group(1).strip()
    else:
        text = raw_text.strip()
    
    # --- Repair Logic ---
    
    # 1. Fix unescaped backslashes (common in LaTeX outputs)
    # Strategy: First, normalize all double backslashes to single ones to avoid triple-escaping.
    # Then, escape all backslashes that are NOT part of a valid JSON escape.
    text = text.replace('\\\\', '\\')
    text = re.sub(r'\\(?![\\\"/bfnrtu])', r'\\\\', text)
    
    # 2. Fix trailing commas in objects and arrays
    text = re.sub(r',\s*}', '}', text)
    text = re.sub(r',\s*]', ']', text)
    
    # 3. Fix missing commas between objects or elements
    text = re.sub(r'}\s*{', '}, {', text)
    text = re.sub(r']\s*\[', '], [', text)
    
    # 4. Fallback: If there's still extra text, try to isolate the array or object
    if not (text.startswith('[') or text.startswith('{')):
        start_array = text.find('[')
        start_obj = text.find('{')
        
        # Determine the earliest starting point
        if start_array != -1 and (start_obj == -1 or start_array < start_obj):
            start = start_array
            end = text.rfind(']')
        elif start_obj != -1:
            start = start_obj
            end = text.rfind('}')
        else:
            start = -1
            
        if start != -1 and end != -1 and end > start:
            text = text[start:end+1]
    
    return text
