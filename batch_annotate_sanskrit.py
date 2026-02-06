import json
import pathlib
import textwrap
import utils

# Bihar Board Class 10 Sanskrit Syllabus (Piyusham)
SANSKRIT_CHAPTERS = [
    # Piyusham Bhag 2 (Main)
    "Mangalam",
    "Patliputra Vaibhavam",
    "Alaskatha",
    "Sanskrit Sahitye Lekhika",
    "Bharatmahima",
    "Bharatiya Sanskarah",
    "Nitishlokah",
    "Karmveer Katha",
    "Swami Dayanand",
    "Mandakini Varnanam",
    "Vyaghrapathik Katha",
    "Karnasya Danvirta",
    "Vishvashantih",
    "Shastrakarah",

    # Piyusham Drutpathay (Supplementary)
    "Bhavani Ashtakam",
    "Jayadevasya Audaryam",
    "Achyutashtakam",
    "Hasyakanikah",
    "Sansaramohah",
    "Madhurashtakam",
    "Bhishma Pratigya",
    "Vrikshaih Samam Bhavatu Me Jivanam",
    "Aho Saundaryasya Asthirata",
    "Sanskrtena Jivanam",
    "Paryatanam",
    "Swaminah Vivekanandasya Vyatha",
    "Shukeshwarashtakam",
    "Vanijah Kripanata",
    "Jayatu Sanskrtam",
    "Kanyayah Patinirnayah",
    "Rashtrastutih",
    "Satyapriyata",
    "Jagaran Geetam",
    "Samayaprajnah",
    "Bharatabhusha Sanskrtabhasha",
    "Priyam Bharatam",
    "Kriyatam Etat",
    "Narasya",
    "Dhruvopakhyanam",

    # Grammar
    "Vyakaran"
]

def generate_sanskrit_annotation_prompt(chapters, questions):
    chapter_lines = [f"{ch}" for ch in chapters]
    prompt = textwrap.dedent(f"""
    You are an expert in educational content classification.
    You will receive a JSON array of questions from a Bihar Board Class 10 Sanskrit question paper.
    Your task is to annotate each question with the correct chapter name from the official Bihar Board Class 10 Sanskrit (Piyusham) syllabus chapters below.

    Crucial Instructions:
    1. **Textbook Questions**: Map questions clearly from the textbook to their respective chapters.
    2. **Grammar Questions**: Map ALL grammar-related questions (Sandhi, Samas, Pratyay, Vibhakti, Karak, etc.) to the chapter "Vyakaran".
    3. **General Questions**: Translation, Comprehension, Essay type questions that don't fit a specific chapter should be mapped to "Vyakaran".

    - Insert the field "chapter_name": "<name>" immediately after the "type" field in each question object.
    - Only use the exact chapter names from the list below.
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
    logger = utils.setup_logger('batch_annotate_sanskrit', 'logs/batch_annotate_sanskrit.log')
    logger.info("Batch Sanskrit Question Annotator (Gemini)")
    print("Batch Sanskrit Question Annotator (Gemini)")
    print("="*40)
    
    data_folder = pathlib.Path("sanskrit_data")
    out_folder = pathlib.Path("sanskrit_data_annotated")
    out_folder.mkdir(exist_ok=True)
    
    files = list(data_folder.glob("*.json"))
    if not files:
        logger.warning(f"No JSON files found in sanskrit_data/!")
        return
        
    chapters = SANSKRIT_CHAPTERS
    model = utils.get_generative_model(model_name="models/gemini-2.5-pro")

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
            
        prompt = generate_sanskrit_annotation_prompt(chapters, questions)
        logger.info("Sending questions to Gemini for annotation...")
        
        response = utils.generate_content_with_retry(model, prompt, logger=logger)
        
        if not response:
            logger.error(f"Failed to annotate {fpath.name}")
            continue

        print("Gemini response received. Parsing...")
        try:
            cleaned_json_string = utils.clean_json_response(response.text)
            annotated = json.loads(cleaned_json_string)
        except Exception as e:
            logger.error(f"Failed to parse Gemini's response for {fpath.name}.")
            logger.error(f"Error details: {e}")
            continue

        if annotated:
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
