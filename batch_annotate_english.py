import json
import pathlib
import textwrap
import utils
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# NCERT Class 10 English (First Flight and Footprints Without Feet) Chapters
ENGLISH_CHAPTERS = [
    "A Letter to God",
    "Nelson Mandela: Long Walk to Freedom",
    "Two Stories about Flying",
    "From the Diary of Anne Frank",
    "Glimpses of India",
    "Mijbil the Otter",
    "Madam Rides the Bus",
    "The Sermon at Benares",
    "The Proposal",
    "Dust of Snow (Poem)",
    "Fire and Ice (Poem)",
    "A Tiger in the Zoo (Poem)",
    "How to Tell Wild Animals (Poem)",
    "The Ball Poem (Poem)",
    "Amanda! (Poem)",
    "The Trees (Poem)",
    "Fog (Poem)",
    "The Tale of Custard the Dragon (Poem)",
    "For Anne Gregory (Poem)",
    "A Triumph of Surgery",
    "The Thief's Story",
    "The Midnight Visitor",
    "A Question of Trust",
    "Footprints without Feet",
    "The Making of a Scientist",
    "The Necklace",
    "Bholi",
    "The Book That Saved the Earth"
]

print_lock = threading.Lock()

def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)

def generate_english_annotation_prompt(chapters, questions):
    chapter_lines = [f"{i+1}. {ch}" for i, ch in enumerate(chapters)]
    prompt = textwrap.dedent(f"""
    You are an expert in educational content classification.
    You will receive a JSON array of questions from a Class 10 English question paper.
    Your task is to annotate each question with the correct chapter number and chapter name from the official NCERT Class 10 English chapters below.
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

    prompt = generate_english_annotation_prompt(chapters, questions)
    
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
    logger = utils.setup_logger('batch_annotate_english', 'logs/batch_annotate_english.log')
    logger.info("Batch English Question Annotator (Gemini) - Parallel")
    print("Batch English Question Annotator (Gemini) - Parallel")
    print("="*40)
    
    data_folder = pathlib.Path("english_data")
    out_folder = pathlib.Path("english_data_annotated")
    out_folder.mkdir(exist_ok=True)
    
    raw_folder = pathlib.Path("english_data_annotated_raw")
    raw_folder.mkdir(exist_ok=True)
    
    files = list(data_folder.glob("*.json"))
    if not files:
        logger.warning(f"No JSON files found in english_data/!")
        return
    
    chapters = ENGLISH_CHAPTERS
    model = utils.get_generative_model(model_name="models/gemini-3-flash-preview")
    
    MAX_WORKERS = 4
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(process_single_file, f, out_folder, raw_folder, chapters, model, logger) for f in files]
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()
