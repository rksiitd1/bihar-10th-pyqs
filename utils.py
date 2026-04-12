import os
import logging
import time
import threading
import random
import re
import sys
import pathlib
from logging.handlers import RotatingFileHandler
from dotenv import load_dotenv

load_dotenv()

# --- Centralized Pool Detection ---
repo_tools_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "repo-management-tools"))
POOL_AVAILABLE = os.path.exists(os.path.join(repo_tools_path, "gemini_pool.py"))

if POOL_AVAILABLE:
    sys.path.append(repo_tools_path)
    from gemini_pool import call_gemini, call_gemini_with_file
    from google.genai import types
else:
    # Standalone mode: requires google-generativeai installed locally
    try:
        import google.generativeai as genai
    except ImportError:
        print("Error: google-generativeai not found. Please install it to use standalone mode.")

# --- Logging Configuration ---
def setup_logger(name, log_file, level=logging.INFO):
    log_path = pathlib.Path(log_file)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler = RotatingFileHandler(log_file, maxBytes=10*1024*1024, backupCount=5, encoding='utf-8')
    handler.setFormatter(formatter)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger = logging.getLogger(name)
    logger.setLevel(level)
    if not logger.handlers:
        logger.addHandler(handler)
        logger.addHandler(console_handler)
    return logger

def configure_genai(api_key=None):
    if not POOL_AVAILABLE:
        genai.configure(api_key=api_key or os.getenv("GOOGLE_API_KEY"))

def rotate_api_key(logger=None):
    pass # Managed by gemini_pool globally if available, or manually if needed

def get_generative_model(model_name="models/gemini-3-flash-preview"):
    if POOL_AVAILABLE:
        return model_name.replace("models/", "")
    else:
        return genai.GenerativeModel(model_name)

def generate_content_with_retry(model, prompt_parts, logger=None, max_retries=5):
    """
    Bridge to call_gemini or local genai.
    """
    if POOL_AVAILABLE:
        try:
            config = types.GenerateContentConfig(
                safety_settings=[
                    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
                    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
                    types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
                    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
                ]
            )
            response = call_gemini(model=model, contents=prompt_parts, config=config, max_retries=max_retries)
            if not response or not response.text:
                raise ValueError("Empty response text")
            return response
        except Exception as e:
            if logger: logger.error(f"Generate content failed after retries in pool: {e}")
            else: print(f"Error: {e}")
            return None
    else:
        # Standalone retry logic
        for attempt in range(max_retries):
            try:
                safety_settings = [
                    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
                    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
                ]
                response = model.generate_content(prompt_parts, safety_settings=safety_settings)
                if not response.text: raise ValueError("Empty response text")
                return response
            except Exception as e:
                wait_time = (2 ** attempt) + random.uniform(1, 4)
                if logger: logger.warning(f"Attempt {attempt+1} failed: {e}. Retrying in {wait_time:.1f}s")
                time.sleep(wait_time)
        return None

def clean_json_response(raw_text: str) -> str:
    match = re.search(r'```json\s*([\s\S]*?)\s*```', raw_text, re.DOTALL)
    if match: text = match.group(1).strip()
    else: text = raw_text.strip()
    text = text.replace('\\\\', '\\')
    text = re.sub(r'\\(?![\\\"/bfnrtu])', r'\\\\', text)
    text = re.sub(r',\s*}', '}', text)
    text = re.sub(r',\s*]', ']', text)
    text = re.sub(r'}\s*{', '}, {', text)
    text = re.sub(r']\s*\[', '], [', text)
    if not (text.startswith('[') or text.startswith('{')):
        start_array = text.find('[')
        start_obj = text.find('{')
        if start_array != -1 and (start_obj == -1 or start_array < start_obj):
            start, end = start_array, text.rfind(']')
        elif start_obj != -1:
            start, end = start_obj, text.rfind('}')
        else: start = -1
        if start != -1 and end != -1 and end > start:
            text = text[start:end+1]
    return text

def generate_content_from_file_with_retry(model, file_path, prompt_text, logger=None, max_retries=5):
    if POOL_AVAILABLE:
        try:
            config = types.GenerateContentConfig(
                safety_settings=[
                    types.SafetySetting(category="HARM_CATEGORY_HARASSMENT", threshold="BLOCK_NONE"),
                    types.SafetySetting(category="HARM_CATEGORY_HATE_SPEECH", threshold="BLOCK_NONE"),
                    types.SafetySetting(category="HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold="BLOCK_NONE"),
                    types.SafetySetting(category="HARM_CATEGORY_DANGEROUS_CONTENT", threshold="BLOCK_NONE"),
                ]
            )
            response = call_gemini_with_file(model, file_path, "application/pdf", prompt_text, config=config, max_retries=max_retries)
            if not response or not response.text:
                raise ValueError("Empty response text")
            return response
        except Exception as e:
            if logger: logger.error(f"Generate file content failed pool: {e}")
            else: print(f"Error: {e}")
            return None
    else:
        # Standalone file upload logic
        for attempt in range(max_retries):
            try:
                uploaded_file = genai.upload_file(path=file_path, display_name=os.path.basename(file_path))
                response = model.generate_content([prompt_text, uploaded_file])
                genai.delete_file(uploaded_file.name)
                if not response.text: raise ValueError("Empty response text")
                return response
            except Exception as e:
                wait_time = (2 ** attempt) + random.uniform(1, 4)
                if logger: logger.warning(f"File attempt {attempt+1} failed: {e}. Retrying in {wait_time:.1f}s")
                time.sleep(wait_time)
        return None
