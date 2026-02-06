import json
import pathlib
import textwrap
import utils
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# NCERT Class 10 Sanskrit (Shemushi Part 2) Chapters
SANSKRIT_CHAPTERS = [
    "Shuchiparyavaranam (शुचिपर्यावरणम्)",
    "Buddhirbalvati Sada (बुद्धिर्बलवती सदा)",
    "Shishulalanam (शिशुलालनम्)",
    "Janani Tulyavatsala (जननी तुल्यवत्सला)",
    "Subhashitani (सुभाषितानि)",
    "Souhardam Prakriteh Shobha (सौहार्दं प्रकृतेः शोभा)",
    "Vichitrah Sakshi (विचित्रः साक्षी)",
    "Suktayah (सूक्तयः)",
    "Bhukampabhibhishika (भूकम्पविभीषिका)",
    "Anyoktayah (अन्योक्तयः)"
]

print_lock = threading.Lock()

def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)

def generate_sanskrit_annotation_prompt(chapters, questions):
    chapter_lines = [f"{i+1}. {ch}" for i, ch in enumerate(chapters)]
    prompt = textwrap.dedent(f"""
    You are an expert in educational content classification.
    You will receive a JSON array of questions from a Class 10 Sanskrit question paper.
    Your task is to annotate each question with the correct chapter number and chapter name from the official NCERT Class 10 Sanskrit chapters below.
    - Insert the fields "chapter": "<number>", "chapter_name": "<name>" immediately after the "type" field in each question object.
    - Only use the chapter numbers/names from the list below.
    - Output the result as a JSON array, with the new fields added to each question.

    Chapters:
    {chr(10).join(chapter_lines)}

    Here is the input JSON array of questions:
    ```json
    {json.dumps(questions, ensure_ascii=False, indent=2)}
    ```

    Output only the annotated JSON array.
    """)
    return prompt

def process_single_file(fpath, out_folder, raw_folder, chapters, model, logger):
    out_path = out_folder / fpath.name
    if out_path.exists():
        safe_print(f"⏭️  Skipping {fpath.name} (already annotated)")
        return

    safe_print(f"🚀 Processing: {fpath.name}")
    
    try:
        with open(fpath, 'r', encoding='utf-8') as f:
            questions = json.load(f)
    except Exception as e:
        logger.error(f"Failed to read input file {fpath.name}: {e}")
        return

    prompt = generate_sanskrit_annotation_prompt(chapters, questions)
    
    response = utils.generate_content_with_retry(model, prompt, logger=logger)
    
    if not response:
        logger.error(f"Failed to process {fpath.name}.")
        return

    # Save raw response IMMEDIATELY
    raw_path = raw_folder / f"{fpath.stem}_raw.txt"
    with open(raw_path, 'w', encoding='utf-8') as f:
        f.write(response.text)
    
    try:
        cleaned_json_string = utils.clean_json_response(response.text)
        annotated = json.loads(cleaned_json_string)
        
        # Reorder fields
        for i, q in enumerate(annotated):
            if "type" in q and "chapter" in q and "chapter_name" in q:
                new_q = {}
                for k, v in q.items():
                    new_q[k] = v
                    if k == "type":
                        new_q["chapter"] = q["chapter"]
                        new_q["chapter_name"] = q["chapter_name"]
                annotated[i] = new_q
                
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(annotated, f, indent=4, ensure_ascii=False)
        safe_print(f"✓ Annotated data saved to: {out_path}")
    except Exception as e:
        logger.error(f"Failed to parse Gemini's response for {fpath.name}: {e}")
        safe_print(f"❌ Failed to parse {fpath.name}. Raw preserved.")

def main():
    logger = utils.setup_logger('batch_annotate_sanskrit', 'logs/batch_annotate_sanskrit.log')
    logger.info("Batch Sanskrit Question Annotator (Gemini) - Parallel")
    print("Batch Sanskrit Question Annotator (Gemini) - Parallel")
    print("="*40)
    
    data_folder = pathlib.Path("sanskrit_data")
    out_folder = pathlib.Path("sanskrit_data_annotated")
    out_folder.mkdir(exist_ok=True)
    
    raw_folder = pathlib.Path("sanskrit_data_annotated_raw")
    raw_folder.mkdir(exist_ok=True)
    
    files = list(data_folder.glob("*.json"))
    if not files:
        logger.warning(f"No JSON files found in sanskrit_data/!")
        return
    
    chapters = SANSKRIT_CHAPTERS
    model = utils.get_generative_model(model_name="models/gemini-3-flash-preview")
    
    MAX_WORKERS = 2
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(process_single_file, f, out_folder, raw_folder, chapters, model, logger) for f in files]
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()
