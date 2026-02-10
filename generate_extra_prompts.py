import os

# --- Hindi Data ---
HINDI_DATA = {
    'essay': {'total': 49, 'years': 10, 'target': 10},
    'letter_writing': {'total': 34, 'years': 10, 'target': 8},
    'comprehension': {'total': 50, 'years': 10, 'target': 8}
}

# --- English Data ---
ENGLISH_DATA = {
    'essay': {'total': 23, 'years': 10, 'target': 8},
    'letter_writing': {'total': 47, 'years': 10, 'target': 10},
    'comprehension': {'total': 54, 'years': 10, 'target': 8},
    'translation': {'total': 18, 'years': 8, 'target': 10} # 18 seems low? Maybe groups of sentences.
}

# --- Sanskrit Data ---
SANSKRIT_DATA = {
    'essay': {'total': 88, 'years': 15, 'target': 12},
    'letter_writing': {'total': 62, 'years': 10, 'target': 10},
    'comprehension': {'total': 64, 'years': 13, 'target': 8},
    'translation': {'total': 182, 'years': 15, 'target': 25}
}

# --- Templates ---

ESSAY_TEMPLATE = """These are Class 10 Bihar Board {subject} Essay (Nibandh/Paragraph) topics collected from the past {years} years of board examinations.

The dataset contains {total_items} essay topics. In the examination, students are typically given 4-5 options and must choose one to write on.

Your task is to analyze all {total_items} topics and identify the {target} most probable and important essay topics that students must prepare.

Follow this methodology:
1. **Thematic Clustering**: Group topics by core theme (e.g., Environmental, National Festivals, Social Problems, Personal Ambition, Health/Sports).
2. **Frequency Analysis**: Identify themes that repeat almost every year.
3. **Current Relevance**: Weight topics that are currently socially or politically relevant (e.g., Pollution, Digital India).
4. **Standard Favorites**: Include "Evergreen" topics that examiners love (e.g., Discipline, Friendship, My School).

**Output Requirements:**
- Provide a numbered list of the top {target} essay topics.
- For each topic, list 3-4 **Key Points/Sub-headings** that the student should cover to score maximum marks.
- Mention the **Probability** of this theme appearing.

**Objective:**
Ensure that if a student prepares these {target} essays, they will almost certainly find at least one match in their exam question paper.
"""

LETTER_TEMPLATE = """These are Class 10 Bihar Board {subject} Letter/Application Writing questions collected from the past {years} years.

The dataset contains {total_items} questions. In the exam, usually 2 questions are asked (one formal, one informal or internal choice), and students attempt one.

Your task is to analyze all {total_items} questions and identify the {target} essential letter types/scenarios to practice.

Follow this methodology:
1. **Recipient Analysis**: Categorize by recipient (Headmaster/Principal, Father/Mother/Relative, Editor, Municipal/Police authorities).
2. **Subject Analysis**: Identify common requests (Leave due to illness, Fee concession, Book purchase, Complaining about filth/crime, Inviting to a function).
3. **Format Frequency**: Determine which formats (Formal vs. Informal) are most dominant.

**Output Requirements:**
- Provide a numbered list of {target} distinct scenarios (e.g., "Application to Principal for Fee Concession").
- For each, provide a **Format Checklist** (e.g., "Must include Date, Subject, Salutation 'Mahashaya', Body, Closing").
- highlighting specifically *why* this scenario is high-yield.

**Objective:**
Mastering these {target} scenarios should cover 90% of the possible letter questions in the exam.
"""

COMPREHENSION_TEMPLATE = """These are Class 10 Bihar Board {subject} Reading Comprehension (Unseen Passage/Gadyansh) passages collected from the past {years} years.

The dataset contains {total_items} passages.

Your task is to analyze these passages to understand the *nature* of texts selected by the board and identify {target} representative themes or types for practice.

Follow this methodology:
1. **Source Analysis**: Are passages usually Story-based (moral fables), Biographies (great leaders), or Descriptive (nature/science)?
2. **Difficulty Assessment**: Analyze the complexity of vocabulary and sentence structure.
3. **Question Pattern**: Are questions mostly direct fact-retrieval or do they ask for title/summary/inference?

**Output Requirements:**
- Identify {target} **Themes/Types** of passages most likely to appear (e.g., "Moral Story about Cooperation", "Biography of a Patriot").
- For each type, suggest a **Reading Strategy** (e.g., "Focus on the moral at the end", "Note down dates and names first").
- Provide 3-4 keywords or vocabulary often found in such passages in {subject}.

**Objective:**
To give students a clear expectation of what *kind* of texts they will read, reducing exam anxiety.
"""

TRANSLATION_TEMPLATE = """These are Class 10 Bihar Board {subject} Translation questions (Hindi to {subject} or vice-versa) collected from the past {years} years.

The dataset contains {total_items} translation sentences/items.

Your task is to analyze all {total_items} items and identify the {target} most critical **Grammar Rules or Sentence Patterns** that are repeatedly tested.

Follow this methodology:
1. **Grammar Decomposition**: Break down sentences to identify the underlying rule (e.g., Simple Present Tense, Case endings/Vibhakti usage, Passive Voice, Imperative Mood).
2. **Vocabulary Frequency**: detailed analysis of common nouns and verbs used (e.g., "going", "reading", "King", "Village", "Ganga").
3. **Pattern Recognition**: Identify set phrases or idioms that appear often (e.g., "There is a...", "Tree falls from leaf...").

**Output Requirements:**
- List the {target} **Golden Rules/Patterns** of translation for this exam.
- For each rule, provide a **Model Sentence** from the dataset and its correct translation.
- Explain the specific grammatical trap or point to watch out for.

**Objective:**
A student proficient in these {target} patterns should be able to solve majority of the translation questions correctly.
"""

def generate():
    os.makedirs("analysis_prompts", exist_ok=True)
    
    # --- Process Hindi ---
    subject = "Hindi"
    s_key = "hindi"
    for type_key, data in HINDI_DATA.items():
        if type_key == 'essay': templ = ESSAY_TEMPLATE
        elif type_key == 'letter_writing': templ = LETTER_TEMPLATE
        elif type_key == 'comprehension': templ = COMPREHENSION_TEMPLATE
        else: continue
        
        content = templ.format(subject=subject, years=data['years'], total_items=data['total'], target=data['target'])
        filename = f"analysis_prompts/{s_key}_{type_key}_analysis_prompt.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated {filename}")

    # --- Process English ---
    subject = "English"
    s_key = "english"
    for type_key, data in ENGLISH_DATA.items():
        if type_key == 'essay': templ = ESSAY_TEMPLATE
        elif type_key == 'letter_writing': templ = LETTER_TEMPLATE
        elif type_key == 'comprehension': templ = COMPREHENSION_TEMPLATE
        elif type_key == 'translation': templ = TRANSLATION_TEMPLATE
        else: continue
        
        content = templ.format(subject=subject, years=data['years'], total_items=data['total'], target=data['target'])
        filename = f"analysis_prompts/{s_key}_{type_key}_analysis_prompt.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated {filename}")

    # --- Process Sanskrit ---
    subject = "Sanskrit"
    s_key = "sanskrit"
    for type_key, data in SANSKRIT_DATA.items():
        if type_key == 'essay': templ = ESSAY_TEMPLATE
        elif type_key == 'letter_writing': templ = LETTER_TEMPLATE
        elif type_key == 'comprehension': templ = COMPREHENSION_TEMPLATE
        elif type_key == 'translation': templ = TRANSLATION_TEMPLATE
        else: continue
        
        content = templ.format(subject=subject, years=data['years'], total_items=data['total'], target=data['target'])
        filename = f"analysis_prompts/{s_key}_{type_key}_analysis_prompt.md"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Generated {filename}")

if __name__ == "__main__":
    generate()
