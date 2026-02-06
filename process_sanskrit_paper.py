import os
import google.generativeai as genai
import json
import argparse
import pathlib
import textwrap
import re
import time
from dotenv import load_dotenv
import utils

load_dotenv()
logger = utils.setup_logger('process_sanskrit', 'logs/process_sanskrit.log')

def clean_json_response(raw_text: str) -> str:
    match = re.search(r'```json\s*([\s\S]*?)\s*```', raw_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_text.strip()

def generate_extraction_prompt(uploaded_file_uri: str) -> list:
    prompt = textwrap.dedent("""
    Your task is to act as an expert data extraction engine. You will receive a PDF file of a Bihar Board Class 10 Sanskrit question paper. You must meticulously extract all questions and convert them into a single, clean JSON array.

    Follow these instructions precisely:

    1.  **JSON Structure**: The output must be a JSON array where each element is an object representing a single question.
    2.  **Required Fields for All Questions**:
        - `id`: A unique string identifier. Numbering must start from 1 for EACH type. 
          - Examples: "obj_1", "gadyansh_1", "patra_1", "essay_1", "translation_1", "short_1".
        - `type`: Categorize each question into one of these types:
          - `objective`: Section A (Vastunisth Prashna).
          - `comprehension`: Unseen Passages (Gadyansh).
          - `letter_writing`: Letter Writing (Patra Lekhan).
          - `essay`: Paragraph/Article Writing (Anuched).
          - `translation`: Translation Hindi to Sanskrit (Anuvad).
          - `short_answer`: Short Answer Questions (Laghu Uttariya).
        - `question`: The text of the question (in Sanskrit/Hindi as appears).
        - `prashna`: Same as question.
        - `instructions`: Any specific instructions (e.g., "Answer in Sanskrit", "Answer any 8").

    3.  **Handling Alternatives**:
        - If questions have alternatives (OR/Athva), create separate objects.

    4.  **Fields for "objective" Type**:
        - `options`: An object with keys "A", "B", "C", "D".
        - `vikalpa`: Same as options.

    5.  **Fields for "comprehension" (Gadyansh)**:
        - `context`: The Sanskrit passage text.
        - `sub_questions`: The questions based on the passage (Ekpaden/Purnavakyen).

    6.  **Accuracy**:
        - Preserve all Sanskrit text exactly (Devanagari script).
        - Maintain the Hindi instructions where present.

    The PDF file is provided. Begin processing now.
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
    logger.info(f"Starting Sanskrit processing for: {input_pdf_path}")
    print(f"🚀 Starting Sanskrit processing for: {input_pdf_path}")
    
    input_path = pathlib.Path(input_pdf_path)
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_pdf_path}")

    utils.configure_genai()

    print("Uploading file...")
    uploaded_file = genai.upload_file(path=input_path, display_name=input_path.name)
    
    print("Generating content...")
    prompt_parts = generate_extraction_prompt(uploaded_file.uri)
    model = utils.get_generative_model(model_name="models/gemini-2.0-flash")
    
    response = utils.generate_content_with_retry(model, prompt_parts, logger=logger)

    if response:
        print("Parsing response...")
        try:
            cleaned_json = clean_json_response(response.text)
            data = json.loads(cleaned_json)
            
            output_path = pathlib.Path(output_json_path)
            output_path.parent.mkdir(exist_ok=True, parents=True)
            with open(output_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            print(f"✅ Saved to {output_json_path}")
        except Exception as e:
            logger.error(f"Error: {e}")
            print(f"❌ Error: {e}")
    
    try: genai.delete_file(uploaded_file.name)
    except: pass

    logger.info(f"Time: {time.time() - start_time:.2f}s")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_pdf")
    parser.add_argument("output_json")
    args = parser.parse_args()
    process_question_paper(args.input_pdf, args.output_json)
