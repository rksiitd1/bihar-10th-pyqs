import json
import pathlib
import textwrap
import utils

# NCERT Class 10 Science Chapters
SCIENCE_CHAPTERS = [
    "Chemical Reactions and Equations",
    "Acids, Bases and Salts",
    "Metals and Non-metals",
    "Carbon and its Compounds",
    "Life Processes",
    "Control and Coordination",
    "How do Organisms Reproduce?",
    "Heredity",
    "Light - Reflection and Refraction",
    "The Human Eye and the Colourful World",
    "Electricity",
    "Magnetic Effects of Electric Current",
    "Our Environment"
]

def generate_science_annotation_prompt(chapters, questions):
    chapter_lines = [f"{i+1}. {ch}" for i, ch in enumerate(chapters)]
    prompt = textwrap.dedent(f"""
    You are an expert in educational content classification.
    You will receive a JSON array of questions from a Class 10 Science question paper.
    Your task is to annotate each question with the correct chapter number and chapter name from the official NCERT Class 10 Science chapters below.
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

def main():
    logger = utils.setup_logger('batch_annotate_science', 'logs/batch_annotate_science.log')
    logger.info("Batch Science Question Annotator (Gemini)")
    print("Batch Science Question Annotator (Gemini)")
    print("="*40)
    
    data_folder = pathlib.Path("science_data")
    out_folder = pathlib.Path("science_data_annotated")
    out_folder.mkdir(exist_ok=True)
    
    # Raw response folder
    raw_folder = pathlib.Path("science_data_annotated_raw")
    raw_folder.mkdir(exist_ok=True)
    
    files = list(data_folder.glob("*.json"))
    if not files:
        logger.warning(f"No JSON files found in science_data/!")
        return
    
    chapters = SCIENCE_CHAPTERS
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

        prompt = generate_science_annotation_prompt(chapters, questions)
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
        logger.info(f"Annotated data saved to: {out_path}")
        print(f"✓ Annotated data saved to: {out_path}")

if __name__ == "__main__":
    main()
