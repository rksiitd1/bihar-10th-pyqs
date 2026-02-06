import json
import pathlib
import textwrap
import utils
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading

# NCERT Class 10 Hindi Chapters (Combined Godhuli and Varnika)
HINDI_CHAPTERS = [
    "Shram Vibhajan aur Jati Pratha (श्रम विभाजन और जाति प्रथा)",
    "Vish ke Dant (विष के दाँत)",
    "Bharat se ham kya seekhein (भारत से हम क्या सीखें)",
    "Nakhun Kyon Badhte Hain (नाखून क्यों बढ़ते हैं)",
    "Nagari Lipi (नागरी लिपि)",
    "Bahadur (बहादुर)",
    "Parampara ka Mulyankan (परम्परा का मूल्यांकन)",
    "Jeet-Jeet Main Nirakhat Hun (जीत-जीत मैं निरखत हूँ)",
    "Avinyo (आविन्यों)",
    "Machhali (मछली)",
    "Naubatkhane Mein Ibadat (नौबतखाने में इबादत)",
    "Shiksha aur Sanskriti (शिक्षा और संस्कृति)",
    "Ram Naam Binu Birthe Jagi Janma (राम नाम बिनु बिरथे जगि जनमा)",
    "Prem Ayani Shri Radhika (प्रेम अयनि श्री राधिका)",
    "Ati Sudho Sneh ko Marag Hai (अति सूधो स्नेह को मारग है)",
    "Swadeshi (स्वदेशी)",
    "Bharat Mata (भारत माता)",
    "Janatantra ka Janma (जनतंत्र का जन्म)",
    "Hiroshima (हिरोशिमा)",
    "Ek Vriksh ki Hatya (एक वृक्ष की हत्या)",
    "Hamari Neend (हमारी नींद)",
    "Akshar Gyaan (अक्षर ज्ञान)",
    "Lautkar Aaunga Phir (लौटकर आऊँगा फिर)",
    "Mere Bina Tum Prabhu (मेरे बिना तुम प्रभु)",
    "Magamma (ममगम्मा - दही वाली मगम्मा)",
    "Dhate Vishwas (ढहते विश्वास)",
    "Maa (माँ)",
    "Nagar (नगर)",
    "Dharti Kab Tak Ghumegi (धरती कब तक घूमेगी)"
]

print_lock = threading.Lock()

def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)

def generate_hindi_annotation_prompt(chapters, questions):
    chapter_lines = [f"{i+1}. {ch}" for i, ch in enumerate(chapters)]
    prompt = textwrap.dedent(f"""
    You are an expert in educational content classification.
    You will receive a JSON array of questions from a Class 10 Hindi question paper.
    Your task is to annotate each question with the correct chapter number and chapter name from the official NCERT Class 10 Hindi chapters below.
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

    prompt = generate_hindi_annotation_prompt(chapters, questions)
    
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
    logger = utils.setup_logger('batch_annotate_hindi', 'logs/batch_annotate_hindi.log')
    logger.info("Batch Hindi Question Annotator (Gemini) - Parallel")
    print("Batch Hindi Question Annotator (Gemini) - Parallel")
    print("="*40)
    
    data_folder = pathlib.Path("hindi_data")
    out_folder = pathlib.Path("hindi_data_annotated")
    out_folder.mkdir(exist_ok=True)
    
    raw_folder = pathlib.Path("hindi_data_annotated_raw")
    raw_folder.mkdir(exist_ok=True)
    
    files = list(data_folder.glob("*.json"))
    if not files:
        logger.warning(f"No JSON files found in hindi_data/!")
        return
    
    chapters = HINDI_CHAPTERS
    model = utils.get_generative_model(model_name="models/gemini-3-flash-preview")
    
    MAX_WORKERS = 20
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = [executor.submit(process_single_file, f, out_folder, raw_folder, chapters, model, logger) for f in files]
        for future in as_completed(futures):
            future.result()

if __name__ == "__main__":
    main()
