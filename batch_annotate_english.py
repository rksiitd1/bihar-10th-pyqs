import json
import pathlib
import textwrap
import utils

# Bihar Board Class 10 English Syllabus (Panorama Part 2)
ENGLISH_CHAPTERS = [
    # Prose
    "The Pace for Living",
    "Me and the Ecology Bit",
    "Gillu",
    "What is Wrong with Indian Films",
    "Acceptance Speech",
    "Once Upon A Time",
    "The Unity of Indian Culture",
    "Little Girls Wiser Than Men",

    # Poetry
    "God Made the Country",
    "Ode on Solitude",
    "Polythene Bag",
    "Thinner Than a Crescent",
    "The Empty Heart",
    "Koel (The Black Cuckoo)",
    "The Sleeping Porter",
    "Martha",

    # Panorama English Reader Part 2 (Supplementary)
    "January Night",
    "Allergy",
    "The Bet",
    "Quality",
    "Sun and Moon",
    "Two Horizons",
    "Love Defiled",

    # General
    "General"
]

def generate_english_annotation_prompt(chapters, questions):
    chapter_lines = [f"{ch}" for ch in chapters]
    prompt = textwrap.dedent(f"""
    You are an expert in educational content classification.
    You will receive a JSON array of questions from a Bihar Board Class 10 English question paper.
    Your task is to annotate each question with the correct chapter name from the official Bihar Board Class 10 English (Panorama Part 2) syllabus chapters below.
    - Insert the field "chapter_name": "<name>" immediately after the "type" field in each question object.
    - Only use the exact chapter names from the list below.
    - If a question does not belong to any specific chapter (e.g., Grammar, Unseen Passage, Essay, Letter), set "chapter_name" to "General".
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

def main():
    logger = utils.setup_logger('batch_annotate_english', 'logs/batch_annotate_english.log')
    logger.info("Batch English Question Annotator (Gemini)")
    print("Batch English Question Annotator (Gemini)")
    print("="*40)
    
    data_folder = pathlib.Path("english_data")
    out_folder = pathlib.Path("english_data_annotated")
    out_folder.mkdir(exist_ok=True)
    
    # Raw response folder
    raw_folder = pathlib.Path("english_data_annotated_raw")
    raw_folder.mkdir(exist_ok=True)

    files = list(data_folder.glob("*.json"))
    if not files:
        logger.warning(f"No JSON files found in english_data/!")
        return
    
    chapters = ENGLISH_CHAPTERS
    model = utils.get_generative_model(model_name="models/gemini-3-flash-preview")

    for fpath in files:
        out_path = out_folder / fpath.name
        if out_path.exists():
            print(f"⏭️  Skipping {fpath.name} (already annotated)")
            continue
            
        logger.info(f"Processing: {fpath.name}")
        print(f"Processing: {fpath.name}")
        
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                questions = json.load(f)
        except Exception as e:
            logger.error(f"Failed to read input file {fpath.name}: {e}")
            continue

        prompt = generate_english_annotation_prompt(chapters, questions)
        logger.info("Sending questions to Gemini for annotation...")
        
        response = utils.generate_content_with_retry(model, prompt, logger=logger)
        
        if not response:
            logger.error(f"Failed to process {fpath.name}.")
            continue
        
        # Save raw response
        raw_path = raw_folder / f"{fpath.stem}_raw.txt"
        with open(raw_path, 'w', encoding='utf-8') as f:
            f.write(response.text)
        logger.info(f"Raw response saved: {raw_path}")

        logger.info("Gemini response received. Parsing...")
        try:
            cleaned_json_string = utils.clean_json_response(response.text)
            annotated = json.loads(cleaned_json_string)
        except Exception as e:
            logger.error(f"Failed to parse Gemini's response for {fpath.name}.")
            logger.error(f"Error details: {e}")
            logger.info(f"Raw response preserved in: {raw_path}")
            continue
            
        # Reorder fields
        for i, q in enumerate(annotated):
            if "type" in q and "chapter_name" in q:
                new_q = {}
                for k, v in q.items():
                    new_q[k] = v
                    if k == "type":
                        new_q["chapter_name"] = q["chapter_name"]
                annotated[i] = new_q
                
        with open(out_path, 'w', encoding='utf-8') as f:
            json.dump(annotated, f, indent=4, ensure_ascii=False)
        logger.info(f"Annotated data saved to: {out_path}")
        print(f"✓ Annotated data saved to: {out_path}")

if __name__ == "__main__":
    main()
