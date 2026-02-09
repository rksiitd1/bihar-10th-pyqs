import os
import json
import re

SUBJECTS = ['english', 'hindi', 'mathematics', 'sanskrit', 'science', 'social_science']

PREFIX_MAP = {
    'english': 'eng',
    'hindi': 'hin',
    'mathematics': 'math',
    'sanskrit': 'san',
    'science': 'sci',
    'social_science': 'soc'
}

# Known patterns as fallbacks if 2025 analysis fails
# Format: (total_asked, to_attempt)
FALLBACK_PATTERNS = {
    'science': {
        'short': (20, 10),
        'long': (6, 4) 
    },
    'social_science': {
        'short': (20, 10), # Approximation
        'long': (8, 4)
    },
    'mathematics': {
        'short': (30, 15),
        'long': (8, 4)
    },
    'hindi': {
        'short': (10, 5),
        'long': (6, 3) 
    },
    'english': {
        'short': (10, 5),
        'long': (6, 3)
    },
    'sanskrit': {
        'short': (16, 8),
        'long': (6, 3) # Hypothetical
    }
}

TARGET_SELECTION_COUNTS = {
    'short': 40,
    'long': 12
}

PROMPT_TEMPLATE_SHORT = """These are Class 10 Bihar Board {subject} short-answer questions collected from the past {years} years of board examinations. Only short-answer type questions are included.

The dataset contains {total_items} questions. In the actual examination, {exam_questions_count} short-answer questions are asked, and students are required to attempt only {attempt_questions_count}.

Your task is to analyze all {total_items} questions and identify the {target_selection_count} most important questions that students must study to maximize their chances of success.

You must follow the logical methodology below strictly and systematically:

Frequency Analysis

Count how many times each question, or its close variants, has appeared over the {years} years.

Assign a frequency score to each question.

Conceptual Clustering

Group questions that test the same core concept, even if their wording is different.

Treat rephrased or slightly modified questions as conceptually identical.

Trend Detection Over Time

Identify questions or concepts that:

Appear repeatedly in recent years, or

Reappear at regular intervals (for example, every 2–3 years).

Syllabus Centrality Weighting

Give higher importance to questions derived from:

Core chapters

Foundational definitions and principles

Concepts that frequently act as prerequisites for long-answer questions

Reduce weight for highly niche or rarely connected questions.

Exam-Setter Behavior Modeling

Assume the examiner prefers:

Standard textbook-aligned definitions

Frequently tested terms and principles

Questions that check conceptual clarity in limited words

Penalize overly obscure, one-off, or trick-based questions.

Coverage Optimization Constraint

The final set of {target_selection_count} questions must:

Cover maximum syllabus breadth

Minimize redundancy across similar definitions or concepts

Ensure that at least {attempt_questions_count} questions from the set are likely to appear together in the exam.

Probability-Based Selection

Assign an estimated probability of appearance to each shortlisted question.

Select the final {target_selection_count} questions such that the combined probability of being able to answer any {attempt_questions_count} out of {exam_questions_count} exam questions is maximized.

Output Requirements:

Present the final {target_selection_count} questions in a numbered list.

For each question, briefly mention:

Why it was selected (frequency, trend, syllabus importance, etc.)

The core concept or definition it tests.

Avoid vague statements; base all decisions strictly on the above logical steps.

Objective:
The goal is to ensure that a student who thoroughly prepares only these {target_selection_count} short-answer questions will be able to confidently attempt all {attempt_questions_count} required questions and score very high marks in the examination.
"""

PROMPT_TEMPLATE_LONG = """These are Class 10 Bihar Board {subject} long-answer questions collected from the past {years} years of board examinations. Only long-answer type questions are included.

The dataset contains {total_items} questions. In the actual examination, {exam_questions_count} long-answer questions are asked, and students are required to attempt only {attempt_questions_count}.

Your task is to analyze all {total_items} questions and identify the {target_selection_count} most important questions that students must study to maximize their chances of success.

You must follow the logical methodology below strictly and systematically:

Frequency Analysis

Count how many times each question, or its close variants, has appeared over the {years} years.

Assign a frequency score to each question.

Conceptual Clustering

Group questions that test the same core concept, even if their wording is different.

Treat rephrased or slightly modified questions as conceptually identical.

Trend Detection Over Time

Identify questions or concepts that:

Appear repeatedly in recent years, or

Reappear at regular intervals (for example, every 2–3 years).

Syllabus Centrality Weighting

Give higher importance to questions derived from:

Core chapters

Foundational concepts

Topics that connect multiple chapters

Reduce weight for highly niche or isolated questions.

Exam-Setter Behavior Modeling

Assume the examiner prefers:

Conceptually rich questions

Questions that allow step-by-step explanation

Questions that test both understanding and presentation

Penalize questions that are too narrow or purely factual.

Coverage Optimization Constraint

The final set of {target_selection_count} questions must:

Cover maximum syllabus breadth

Minimize overlap of underlying concepts

Ensure that at least {attempt_questions_count} questions from the set are likely to appear together in the exam.

Probability-Based Selection

Assign an estimated probability of appearance to each shortlisted question.

Select the final {target_selection_count} questions such that the combined probability of being able to answer any {attempt_questions_count} out of {exam_questions_count} exam questions is maximized.

Output Requirements:

Present the final {target_selection_count} questions in a numbered list.

For each question, briefly mention:

Why it was selected (frequency, trend, core concept, etc.)

The main concept it tests.

Avoid vague statements; base all decisions strictly on the above logical steps.

Objective:
The goal is to ensure that a student who thoroughly prepares only these {target_selection_count} questions will be able to confidently attempt all {attempt_questions_count} required long-answer questions and achieve excellent marks in the examination.
"""

def get_exam_pattern(subject, q_type):
    """
    Attempts to determine (total_asked, to_attempt) from 2025 data.
    Falls back to hardcoded patterns if data is missing or insufficient.
    """
    prefix = PREFIX_MAP.get(subject, subject[:3])
    
    # Try multiple files
    files_to_check = [f"{prefix}_2025i.json", f"{prefix}_2025ii.json"]
    base_dirs = [f"{subject}_data_annotated", f"{subject}_data_annotated0", f"{subject}_data"]
    
    found_count = 0
    
    for filename in files_to_check:
        for base_dir in base_dirs:
            filepath = os.path.join(base_dir, filename)
            if os.path.exists(filepath):
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                        current_count = sum(1 for item in data if item.get('type') == q_type)
                        if current_count > found_count:
                            found_count = current_count
                except:
                    continue
    
    if found_count > 0:
        # Heuristic for attempt count if we have the total asked
        # Usually 50% choice
        total_asked = found_count
        to_attempt = found_count // 2
        
        # Override for specific odd cases if known? 
        # But generally 50% is a safe bet if derived from data
        return total_asked, to_attempt
        
    # Fallback
    fallback = FALLBACK_PATTERNS.get(subject, {}).get(q_type, (20, 10)) # Default default
    print(f"  Note: Using fallback pattern for {subject} {q_type}: Asked {fallback[0]}, Attempt {fallback[1]}")
    return fallback

def main():
    os.makedirs("analysis_prompts", exist_ok=True)
    
    for subject in SUBJECTS:
        manifest_path = f"{subject}_pro_types0/manifest.json"
        
        if not os.path.exists(manifest_path):
            print(f"Skipping {subject}: Manifest not found.")
            continue
            
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
            
        subject_display = subject.replace('_', ' ').title()
        
        # Process Short
        short_data = next((item for item in manifest if item["type"] == "short"), None)
        if short_data:
            total_items = short_data.get("total_items", 0)
            years = short_data.get("years", 0)
            
            exam_q, attempt_q = get_exam_pattern(subject, 'short')
            
            prompt = PROMPT_TEMPLATE_SHORT.format(
                subject=subject_display,
                years=years,
                total_items=total_items,
                exam_questions_count=exam_q,
                attempt_questions_count=attempt_q,
                target_selection_count=TARGET_SELECTION_COUNTS['short']
            )
            
            with open(f"analysis_prompts/{subject}_short_qa_analysis_prompt.md", 'w', encoding='utf-8') as f:
                f.write(prompt)
            print(f"Generated Short Prompt for {subject}")
            
        # Process Long
        long_data = next((item for item in manifest if item["type"] == "long"), None)
        if long_data:
            total_items = long_data.get("total_items", 0)
            years = long_data.get("years", 0)
            
            exam_q, attempt_q = get_exam_pattern(subject, 'long')
            
            prompt = PROMPT_TEMPLATE_LONG.format(
                subject=subject_display,
                years=years,
                total_items=total_items,
                exam_questions_count=exam_q,
                attempt_questions_count=attempt_q,
                target_selection_count=TARGET_SELECTION_COUNTS['long']
            )
            
            with open(f"analysis_prompts/{subject}_long_qa_analysis_prompt.md", 'w', encoding='utf-8') as f:
                f.write(prompt)
            print(f"Generated Long Prompt for {subject}")

if __name__ == "__main__":
    main()
