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

# Load environment variables
load_dotenv()

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

def configure_genai(api_key=None):
    """Configures Gemini. If no key provided, uses current global key."""
    if api_key:
        genai.configure(api_key=api_key)
    else:
        with _rotation_lock:
            key = API_KEYS[_current_key_index] if API_KEYS else None
        if key:
            genai.configure(api_key=key)

def rotate_api_key(logger=None):
    """Manual rotation (legacy support)."""
    global _current_key_index
    with _rotation_lock:
        _current_key_index = (_current_key_index + 1) % len(API_KEYS)
        key = API_KEYS[_current_key_index]
    
    msg = f"🔄 Manual Rotation to Key Index {_current_key_index}"
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
                 _current_key_index = (_current_key_index + 1) % len(API_KEYS)
                 print(f"🔄 Global Rotation: Switching to Key Index {_current_key_index} (Total Calls: {_global_call_count})")
        
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
                msg = f"⏳ Rate limit reached. Retrying in {wait_time:.1f}s..."
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
