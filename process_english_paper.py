import os
import json
import argparse
import pathlib
import textwrap
import time
from dotenv import load_dotenv
import utils

# --- Configuration ---
load_dotenv()
logger = utils.setup_logger('process_english', 'logs/process_english.log')

# --- Core Functions ---

def generate_extraction_prompt(uploaded_file_uri: str) -> list:
    prompt = textwrap.dedent("""
    Your task is to act as an expert data extraction engine. You will receive a PDF file of a Bihar Board Class 10 English question paper. You must meticulously extract all questions and convert them into a single, clean JSON array.

    Follow these instructions precisely:

    1.  **JSON Structure**: The output must be a JSON array where each element is an object representing a single question.
    2.  **Required Fields for All Questions**:
        - `id`: A unique string identifier. For each question type, numbering must start from 1. 
          - Examples: "obj_1", "passage_1", "essay_1", "letter_1", "short_1", "long_1".
          - The numbering for each type must always start at 1.
        - `type`: The question type. You MUST categorize each question into one of the following granular types:
          - `objective`: Section A (Grammar + Textbook MCQs).
          - `passage`: Reading Comprehension (Unseen Passages).
          - `poem`: Poetry Comprehension (Read the poem and answer).
          - `essay`: Paragraph Writing options.
          - `letter`: Letter Writing / Application Writing options.
          - `short_answer`: Short answer type questions from the textbook (e.g., Answer any 5).
          - `long_answer`: Long answer type questions from the textbook (e.g., Answer any 1).
          - `translation`: Translation questions (Hindi to English) if present.
        - `question`: The full English text of the question.
        - `prashna`: The Hindi text of the question if it exists in the paper.
          - **CRITICAL**: Since this is an English paper, most questions usually DO NOT have Hindi text.
          - If NO Hindi text exists for a question, you MUST Translate the "question" into Hindi and put it in "prashna".
          - Do NOT leave `prashna` empty.

    3.  **Handling Alternatives**:
        - If two or more questions are given as alternatives (using "OR" / "Athva"), represent them as distinct objects with IDs like `letter_1_1`, `letter_1_2`.

    4.  **Fields for "objective" Type Questions**:
        - `options`: An object containing the options, with keys "A", "B", "C", "D".
        - `vikalpa`: Translate the options to Hindi for this field.

    5.  **Fields for Questions with Sub-Questions (e.g., Passages)**:
        - If a question (like a Passage) contains sub-questions:
            - `sub_questions`: An object where keys are "1", "2", "3" etc., and values are the sub-question text.
            - `anuprashna`: Translated Hindi version of sub-questions.
            - `context`: The full text of the Passage or Poem itself.

    6.  **Accuracy & Formatting**:
        - Extract text exactly as it appears.
        - Preserve formatting where possible.
        - Do not add external text.

    The PDF file is provided. Begin processing now and generate only the JSON array as your output.
    """)

    return [
        {'text': prompt},
        {'file_data': {
            'mime_type': 'application/pdf',
            'file_uri': uploaded_file_uri
        }}
    ]

def process_question_paper(input_pdf_path: str, output_json_path: str):
    start_time = time.time()
    logger.info(f"Starting English processing for: {input_pdf_path}")
    print(f"🚀 Starting English processing for: {input_pdf_path}")
    
    input_path = pathlib.Path(input_pdf_path)
    if not input_path.exists():
        msg = f"Input file not found: {input_pdf_path}"
        logger.error(msg)
        raise FileNotFoundError(msg)

    # Prepare raw output folder
    output_path = pathlib.Path(output_json_path)
    output_parent = output_path.parent
    raw_folder_name = output_parent.name + "_raw"
    raw_folder = output_parent.parent / raw_folder_name
    raw_folder.mkdir(exist_ok=True, parents=True)

    # Initialize API
    import google.generativeai as genai
    utils.configure_genai()

    logger.info("Uploading file...")
    print("Uploading file...")
    try:
        uploaded_file = genai.upload_file(path=input_path, display_name=input_path.name)
        logger.info(f"File uploaded: {uploaded_file.uri}")
    except Exception as e:
        logger.error(f"Upload failed: {e}")
        raise

    logger.info("Generating content...")
    print("Generating content...")
    prompt_parts = generate_extraction_prompt(uploaded_file.uri)
    model = utils.get_generative_model(model_name="models/gemini-3-flash-preview")
    
    response = utils.generate_content_with_retry(model, prompt_parts, logger=logger)

    if not response:
        logger.error("API call failed")
        try: genai.delete_file(uploaded_file.name)
        except: pass
        return

    # Save raw response IMMEDIATELY
    raw_path = raw_folder / f"{input_path.stem}_raw.txt"
    try:
        with open(raw_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        logger.info(f"Raw API response saved to: {raw_path}")
    except Exception as e:
        logger.error(f"Failed to save raw response: {e}")

    logger.info("Parsing response...")
    print("Parsing response...")
    try:
        cleaned_json = utils.clean_json_response(response.text)
        data = json.loads(cleaned_json)
        
        output_path.parent.mkdir(exist_ok=True, parents=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
            
        logger.info(f"Saved extracted data to {output_json_path}")
        print(f"✅ Saved to {output_json_path}")
    except Exception as e:
        logger.error(f"Error parsing/saving: {e}")
        logger.info(f"Raw response is preserved at {raw_path}")
        print(f"❌ Error: {e}")

    try:
        genai.delete_file(uploaded_file.name)
        logger.info("Deleted uploaded file from API")
    except:
        pass

    elapsed = time.time() - start_time
    logger.info(f"Time: {elapsed:.2f}s")
    print(f"⏱️  Time: {elapsed:.2f}s")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pdf")
    parser.add_argument("output_json")
    args = parser.parse_args()
    process_question_paper(args.input_pdf, args.output_json)
