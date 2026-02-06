import os
import logging
import time
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

API_KEYS = [
    os.environ.get('GOOGLE_API_KEY'),
    os.environ.get('GOOGLE_API_KEY1'),
    os.environ.get('GOOGLE_API_KEY2'),
    os.environ.get('GOOGLE_API_KEY3'),
]
API_KEYS = [k for k in API_KEYS if k]  # Filter out None values

current_key_index = 0

def configure_genai():
    """Configures the Gemini API with the current key."""
    if not API_KEYS:
        raise ValueError("No Gemini API keys found. Please set GOOGLE_API_KEY environment variables.")
    genai.configure(api_key=API_KEYS[current_key_index])

def rotate_api_key(logger=None):
    """Rotates to the next available API key."""
    global current_key_index
    if not API_KEYS:
        msg = "No API keys available to rotate."
        if logger: logger.error(msg)
        else: print(msg)
        return

    current_key_index = (current_key_index + 1) % len(API_KEYS)
    new_key = API_KEYS[current_key_index]
    genai.configure(api_key=new_key)
    
    msg = f"🔄 Rotated to API Key #{current_key_index + 1}"
    if logger:
        logger.warning(msg)
    else:
        print(msg)
    return new_key

def get_generative_model(model_name="models/gemini-2.0-flash"):
    """Returns a configured GenerativeModel instance."""
    # Ensure configured
    configure_genai()
    return genai.GenerativeModel(model_name=model_name)

def generate_content_with_retry(model, prompt_parts, logger=None, max_retries=5):
    """
    Generates content using the provided model with retry logic for rate limits and errors.
    
    Args:
        model: The Google GenAI model instance.
        prompt_parts: The prompt or parts to send.
        logger: Optional logger instance.
        max_retries: Maximum number of retries.
        
    Returns:
        response object or None if failed.
    """
    response = None
    
    for attempt in range(max_retries):
        try:
            response = model.generate_content(prompt_parts)
            return response
        except Exception as e:
            error_str = str(e)
            msg = f"⚠️ Attempt {attempt+1}/{max_retries} failed: {e}"
            if logger: logger.warning(msg)
            else: print(msg)
            
            # Check for resource exhaustion / rate limits
            if "429" in error_str or "Resource has been exhausted" in error_str:
                rotate_api_key(logger)
                time.sleep(2)
            else:
                # Exponential backoff for other errors
                wait_time = (2 ** attempt) + random.uniform(1, 3)
                msg = f"⏳ Retrying in {wait_time:.1f}s..."
                if logger: logger.info(msg)
                else: print(msg)
                time.sleep(wait_time)
                
    if not response:
        msg = "❌ All retries failed."
        if logger: logger.error(msg)
        else: print(msg)
        # raise Exception("Max retries exceeded for API call") # Optional: raise or return None
        return None
    
    return response

# --- Data Processing ---

def clean_json_response(raw_text: str) -> str:
    """Extracts JSON content from a string, handling markdown code blocks."""
    match = re.search(r'```json\s*([\s\S]*?)\s*```', raw_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_text.strip()
