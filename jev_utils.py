"""
Jev API Client and Annotation Utilities for Bihar 10th PYQs.
Uses TypeSafe AI's System One (Jev) for deterministic, non-generative classification.
"""

import os
import json
import time
import random
import logging
import requests
from dotenv import load_dotenv
from typing import Dict, Any, Optional, Tuple, List
import chapter_config

load_dotenv()

# API key is loaded strictly from the environment (set TYPESAFE_API_KEY in .env).
API_KEY = os.environ.get("TYPESAFE_API_KEY")
API_URL = "https://api.typesafe.ai/v1/systemone"

logger = logging.getLogger("jev_utils")
if not logger.handlers:
    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s: %(message)s"))
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)

# Cache precomputed criteria for each subject
_SUBJECT_CRITERIA_CACHE = {}

def get_criteria_for_subject(subject: str) -> Tuple[Dict[str, str], Dict[str, Dict[str, Any]]]:
    """
    Returns (criteria_dict, mapping_dict) where:
    criteria_dict: { label: "Topic: ..." }
    mapping_dict: { label: { "section": ..., "number": ..., "name_en": ..., "name_hi": ... } }
    """
    if subject in _SUBJECT_CRITERIA_CACHE:
        return _SUBJECT_CRITERIA_CACHE[subject]
    
    opts = chapter_config.get_all_chapter_options(subject)
    criteria = {}
    mapping = {}
    for opt in opts:
        label = opt["label"]
        criteria[label] = opt.get("desc", f"Syllabus Topic: {opt['name_en']} / {opt['name_hi']}")
        mapping[label] = {
            "section": opt.get("section", ""),
            "number": opt["number"],
            "name_en": opt["name_en"],
            "name_hi": opt["name_hi"]
        }
    _SUBJECT_CRITERIA_CACHE[subject] = (criteria, mapping)
    return criteria, mapping

def build_question_state(q: Dict[str, Any]) -> str:
    """Builds a rich semantic representation of the question for Jev."""
    parts = []
    
    # Context / instructions
    if q.get("instructions"):
        parts.append(f"Instructions: {q['instructions']}")
    if q.get("context"):
        parts.append(f"Context: {q['context']}")
        
    # Main question text (English)
    if q.get("question"):
        parts.append(f"Question (EN): {q['question']}")
        
    # Main question text (Hindi)
    if q.get("prashna"):
        parts.append(f"Question (HI): {q['prashna']}")
        
    # Options (English)
    if q.get("options") and isinstance(q["options"], dict):
        opts_str = " | ".join(f"{k}: {v}" for k, v in q["options"].items() if v)
        if opts_str:
            parts.append(f"Options (EN): {opts_str}")
            
    # Options (Hindi)
    if q.get("vikalpa") and isinstance(q["vikalpa"], dict):
        v_str = " | ".join(f"{k}: {v}" for k, v in q["vikalpa"].items() if v)
        if v_str:
            parts.append(f"Options (HI): {v_str}")
            
    # Sub-questions if present
    if q.get("sub_questions") and isinstance(q["sub_questions"], list):
        for sq in q["sub_questions"]:
            if isinstance(sq, dict) and sq.get("question"):
                parts.append(f"Sub-question: {sq['question']}")
                
    return "\n".join(parts).strip()

def call_jev_with_retry(
    state: str,
    subject: str,
    max_retries: int = 4,
    timeout: int = 15
) -> Optional[Dict[str, Any]]:
    """Calls Jev Choice primitive with exponential backoff."""
    if not API_KEY:
        raise RuntimeError(
            "TYPESAFE_API_KEY not set. Add it to your .env file "
            "(see .env.example)."
        )

    criteria, _ = get_criteria_for_subject(subject)
    
    subj_data = chapter_config.CHAPTERS.get(subject, {})
    is_multi = subj_data.get("is_multi_section", False)
    
    instructions = (
        f"Select the exact section and chapter for this Class 10 {subject.replace('_', ' ').title()} question from the official BSEB syllabus options:"
        if is_multi else
        f"Select the exact chapter for this Class 10 {subject.replace('_', ' ').title()} question from the official BSEB syllabus options:"
    )
    
    payload = {
        "model": "jev-latest",
        "state": state,
        "questions": {
            "chapter": {
                "type": "choice",
                "instructions": instructions,
                "criteria": criteria
            }
        }
    }
    
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    
    for attempt in range(1, max_retries + 1):
        try:
            resp = requests.post(API_URL, json=payload, headers=headers, timeout=timeout)
            if resp.status_code == 200:
                data = resp.json()
                return data.get("answers", {}).get("chapter")
            elif resp.status_code == 429:
                wait_time = (2 ** attempt) + random.uniform(0.5, 2.0)
                logger.warning(f"Rate limited (429). Retrying in {wait_time:.1f}s (attempt {attempt}/{max_retries})")
                time.sleep(wait_time)
            elif resp.status_code >= 500:
                wait_time = (2 ** attempt) + random.uniform(0.5, 1.5)
                logger.warning(f"Server error {resp.status_code}. Retrying in {wait_time:.1f}s (attempt {attempt}/{max_retries})")
                time.sleep(wait_time)
            else:
                logger.error(f"Jev API returned error {resp.status_code}: {resp.text[:200]}")
                return None
        except Exception as e:
            wait_time = (2 ** attempt) + random.uniform(0.5, 1.5)
            logger.warning(f"Request exception: {e}. Retrying in {wait_time:.1f}s (attempt {attempt}/{max_retries})")
            time.sleep(wait_time)
            
    logger.error(f"Failed to get response from Jev after {max_retries} attempts.")
    return None

def classify_question(
    q: Dict[str, Any],
    subject: str,
    confidence_threshold: float = 0.5
) -> Dict[str, Any]:
    """
    Classifies a question using Jev and returns annotation metadata:
    {
        "section": str (if multi-section),
        "chapter": str,
        "chapter_name": str,
        "confidence": float,
        "is_unclassified": bool,
        "raw_choice": str
    }
    """
    state = build_question_state(q)
    if not state:
        return {
            "section": "UNCLASSIFIED",
            "chapter": "UNCLASSIFIED",
            "chapter_name": "UNCLASSIFIED",
            "confidence": 0.0,
            "is_unclassified": True,
            "raw_choice": "Empty question state"
        }
        
    ans = call_jev_with_retry(state, subject)
    if not ans:
        return {
            "section": "UNCLASSIFIED",
            "chapter": "UNCLASSIFIED",
            "chapter_name": "UNCLASSIFIED",
            "confidence": 0.0,
            "is_unclassified": True,
            "raw_choice": "API call failure"
        }
        
    choice_label = ans.get("choice", "")
    confidence = float(ans.get("confidence", 0.0))
    
    _, mapping = get_criteria_for_subject(subject)
    match_meta = mapping.get(choice_label)
    
    subj_data = chapter_config.CHAPTERS.get(subject, {})
    is_multi = subj_data.get("is_multi_section", False)
    
    if match_meta and confidence >= confidence_threshold:
        res = {
            "chapter": match_meta["number"],
            "chapter_name": match_meta["name_en"],
            "confidence": confidence,
            "is_unclassified": False,
            "raw_choice": choice_label
        }
        if is_multi:
            res["section"] = match_meta["section"]
        return res
    else:
        # Below threshold or unmapped
        res = {
            "chapter": "UNCLASSIFIED",
            "chapter_name": "UNCLASSIFIED",
            "confidence": confidence,
            "is_unclassified": True,
            "raw_choice": choice_label
        }
        if is_multi:
            res["section"] = "UNCLASSIFIED"
        return res
