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

# Setup logger
logger = utils.setup_logger('process_paper', 'logs/process_paper.log')

# --- Core Functions ---

def generate_extraction_prompt(uploaded_file_uri: str) -> list:
    prompt = textwrap.dedent("""
    Your task is to act as an expert data extraction engine. You will receive a PDF file of a Class 10 Bihar Board question paper. You must meticulously extract all questions and convert them into a single, clean JSON array.

    Follow these instructions precisely:

    1.  **JSON Structure**: The output must be a JSON array where each element is an object representing a single question.
    2.  **Required Fields for All Questions**:
        - id: A unique string identifier. For each question type, numbering must start from 1. For example: "obj_1", "obj_2", ... "short_1", "short_2", ... "long_1", "long_2", etc.
        - If two or more questions are given as alternatives (using "or"/"athva") under the same question number, represent them as long_1_1, long_1_2, etc.
        - type: The question type as a string ("objective", "short_answer", "long_answer").
        - question: The full English text of the question.
        - prashna: The full Hindi text of the question.

    3.  **If a question, option, or sub-question is present only in one language (either English or Hindi), you MUST translate it to the other language and fill both fields.**

    4.  **Fields for "objective" Type Questions**:
        - options: An object containing the English options, with keys "A", "B", "C", "D".
        - vikalpa: An object containing the Hindi options, with keys "A", "B", "C", "D".

    5.  **Fields for Questions with Sub-Questions**:
        - If a question contains sub-questions, include:
            - sub_questions: An object containing the English sub-questions, with keys like "A", "B".
            - anuprashna: An object containing the Hindi sub-questions, with keys like "A", "B".

    6.  **LaTeX Formatting (CRITICAL)**:
        - You MUST convert all mathematical, chemical, and scientific notations into proper LaTeX format.
        - Examples: F_1 -> $F_1$, H2O -> $H_2O$, 2 x 2^{1/2} = 5 -> $2 \\times 2^{1/2} = 5$

    7.  **Accuracy**: Ensure the text is extracted exactly as it appears in the document.

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
    logger.info(f"Starting processing for: {input_pdf_path}")
    print(f"Starting processing for: {input_pdf_path}") # Keep minimal console feedback
    
    input_path = pathlib.Path(input_pdf_path)

    if not input_path.exists():
        logger.error(f"Input file not found at: {input_pdf_path}")
        raise FileNotFoundError(f"Input file not found at: {input_pdf_path}")

    # Prepare raw output folder
    output_path = pathlib.Path(output_json_path)
    output_parent = output_path.parent
    raw_folder_name = output_parent.name + "_raw"
    raw_folder = output_parent.parent / raw_folder_name
    raw_folder.mkdir(exist_ok=True)
    
    # Initialize API
    import google.generativeai as genai # local import to avoid potential circular issues if moved to utils mostly
    utils.configure_genai()

    logger.info("Uploading file to the File API...")
    try:
        uploaded_file = genai.upload_file(path=input_path, display_name=input_path.name)
        logger.info(f"File uploaded successfully: {uploaded_file.uri}")
    except Exception as e:
        logger.error(f"Failed to upload file: {e}")
        raise

    prompt_parts = generate_extraction_prompt(uploaded_file.uri)

    logger.info("Generating content with Gemini...")
    model = utils.get_generative_model(model_name="models/gemini-3-flash-preview")
    
    response = utils.generate_content_with_retry(model, prompt_parts, logger=logger)
                
    if not response:
        logger.error("Skipping this file due to API failure.")
        try:
            genai.delete_file(uploaded_file.name)
        except:
            pass
        raise Exception("API call failed after retries")

    # Save raw response IMMEDIATELY
    raw_path = raw_folder / f"{input_path.stem}_raw.txt"
    with open(raw_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
    logger.info(f"Raw API response saved to: {raw_path}")

    logger.info("Cleaning and parsing the JSON response...")
    try:
        cleaned_json_string = utils.clean_json_response(response.text)
        data = json.loads(cleaned_json_string)
    except json.JSONDecodeError as e:
        logger.error(f"Failed to decode JSON: {e}")
        logger.error(f"Raw response is preserved in: {raw_path}")
        try:
            genai.delete_file(uploaded_file.name)
        except:
            pass
        return
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}")
        try:
            genai.delete_file(uploaded_file.name)
        except:
            pass
        return

    logger.info(f"Writing structured data to: {output_path}")
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

    logger.info("Processing complete!")
    print(f"✅ Processed {input_path.name}") 
    
    try:
        logger.info(f"Deleting file {uploaded_file.name} from the API...")
        genai.delete_file(uploaded_file.name)
        logger.info("File deleted.")
    except Exception as e:
        logger.warning(f"Could not delete file: {e}")
    
    end_time = time.time()
    execution_time = end_time - start_time
    logger.info(f"Time: {execution_time:.2f} seconds ({execution_time/60:.2f} minutes)")


# --- Interactive Interface ---

def get_available_files():
    subjects = ['science', 'mathematics', 'social_science', 'hindi', 'english', 'sanskrit']
    available_files = []
    
    for subject in subjects:
        papers_folder = pathlib.Path(f"{subject}_papers")
        if papers_folder.exists():
            pdf_files = list(papers_folder.glob("*.pdf"))
            for pdf_file in pdf_files:
                available_files.append({
                    'path': pdf_file,
                    'subject': subject,
                    'name': pdf_file.name
                })
    
    return available_files

def create_data_folder(subject):
    data_folder = pathlib.Path(f"{subject}_data")
    data_folder.mkdir(exist_ok=True)
    return data_folder

if __name__ == "__main__":
    print("Bihar Class 10 Question Paper Processor")
    print("=" * 50)
    
    files = get_available_files()
    
    if not files:
        print("No PDF files found in any subject folders!")
        exit(1)
    
    print(f"\nFound {len(files)} PDF files:")
    print("=" * 80)
    print(f"{'No.':<4} {'Subject':<16} {'Year':<6} {'Filename':<30} {'Status':<10}")
    print("-" * 80)
    
    for i, file_info in enumerate(files, 1):
        filename = file_info['name']
        year = filename.split('_')[-1].replace('.pdf', '') if '_' in filename else 'N/A'
        
        data_folder = pathlib.Path(f"{file_info['subject']}_data")
        json_filename = file_info['path'].stem + ".json"
        json_path = data_folder / json_filename
        status = "Done" if json_path.exists() else "Pending"
        
        print(f"{i:<4} {file_info['subject']:<16} {year:<6} {filename:<30} {status:<10}")
    
    print("=" * 80)
    
    while True:
        try:
            choice = input(f"\nEnter file number (1-{len(files)}) or 'q' to quit: ").strip()
            
            if choice.lower() == 'q':
                print("Goodbye!")
                exit(0)
            
            choice_num = int(choice)
            if 1 <= choice_num <= len(files):
                selected_file = files[choice_num - 1]
                break
            else:
                print(f"Please enter a number between 1 and {len(files)}")
        except ValueError:
            print("Please enter a valid number")
    
    print(f"\nProcessing: {selected_file['name']}")
    print(f"Subject: {selected_file['subject']}")
    
    data_folder = create_data_folder(selected_file['subject'])
    json_filename = selected_file['path'].stem + ".json"
    json_path = data_folder / json_filename
    
    print(f"Output will be saved to: {json_path}")
    
    confirm = input("\nProceed with processing? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Processing cancelled.")
        exit(0)
    
    try:
        process_question_paper(str(selected_file['path']), str(json_path))
        print(f"\n Successfully processed {selected_file['name']}")
        print(f" Output saved to: {json_path}")
    except Exception as e:
        print(f"\nAn error occurred during execution: {e}")
        logger.exception("An error occurred during execution")
