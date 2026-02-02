import os
import google.generativeai as genai
import json
import pathlib
import textwrap
import re
from dotenv import load_dotenv

def clean_json_response(raw_text: str) -> str:
    match = re.search(r'```json\s*([\s\S]*?)\s*```', raw_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_text.strip()

# Bihar Board Class 10 Hindi Syllabus (Godhuli Bhag 2 & Varnika Bhag 2)
HINDI_CHAPTERS = [
    # Godhuli Bhag 2 - Prose (Gadh Khand)
    "Shram Vibhajan aur Jati Pratha",
    "Vish ke Daant",
    "Bharat se Hum Kya Seekhe",
    "Nakhun Kyon Badhte Hain",
    "Nagari Lipi",
    "Bahadur",
    "Parampara ka Mulyankan",
    "Jit-Jit Main Nirakhat Hoon",
    "Aavinyon",
    "Machhli",
    "Naubatkhaane Mein Ibadat",
    "Shiksha aur Sanskriti",

    # Godhuli Bhag 2 - Poetry (Padya Khand)
    "Ram Binu Birthe Jagi Janma",
    "Prem Ayni Shri Radhika",
    "Ati Sudho Sneh ko Marag Hai",
    "Swadeshi",
    "Bharat Mata",
    "Janatantra ka Janm",
    "Hiroshima",
    "Ek Vriksha ki Hatya",
    "Hamari Neend",
    "Akshar-Gyan",
    "Lautkar Aaunga Phir",
    "Mere Bina Tum Prabhu",

    # Varnika Bhag 2 (Supplementary)
    "Dahi Wali Mangamma",
    "Dhahate Vishwas",
    "Maa",
    "Nagar",
    "Dharti Kab Tak Ghumegi",

    # Grammar
    "Vyakaran"
]

def generate_hindi_annotation_prompt(chapters, questions):
    chapter_lines = [f"{ch}" for ch in chapters]
    prompt = textwrap.dedent(f"""
    You are an expert in educational content classification.
    You will receive a JSON array of questions from a Bihar Board Class 10 Hindi question paper.
    Your task is to annotate each question with the correct chapter name from the official Bihar Board Class 10 Hindi (Godhuli & Varnika) syllabus chapters below.

    Crucial Instructions:
    1. **Textbook Questions**: Map questions clearly from the textbook Prose/Poetry/Supplementary sections to their respective chapters.
    2. **Grammar Questions**: Map ALL grammar-related questions (Sandhi, Samas, Upsarg, Pratyay, Ling, Vachan, Karak, etc.) to the chapter "Vyakaran".
    3. **General Questions**: Essay (Nibandh), Letter Writing (Patra Lekhan), Comprehension (Gadyansh), Translation (Anuvad), etc., if they don't fit a specific book chapter, should also be mapped to "Vyakaran".

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
    print("Batch Hindi Question Annotator (Gemini)")
    print("="*40)
    data_folder = pathlib.Path("hindi_data")
    out_folder = pathlib.Path("hindi_data_annotated")
    out_folder.mkdir(exist_ok=True)
    files = list(data_folder.glob("*.json"))
    if not files:
        print(f"No JSON files found in hindi_data/!")
        return
    chapters = HINDI_CHAPTERS
    model = genai.GenerativeModel(model_name="models/gemini-2.5-pro")
    
    for fpath in files:
        out_path = out_folder / fpath.name
        if out_path.exists():
            print(f"⏭️  Skipping {fpath.name} (already annotated)")
            continue
            
        print(f"\nProcessing: {fpath.name}")
        with open(fpath, 'r', encoding='utf-8') as f:
            questions = json.load(f)
        
        prompt = generate_hindi_annotation_prompt(chapters, questions)
        print("Sending questions to Gemini for annotation...")
        
        # Adding retry logic for robustness
        retries = 3
        while retries > 0:
            try:
                response = model.generate_content(prompt)
                print("Gemini response received. Parsing...")
                cleaned_json_string = clean_json_response(response.text)
                annotated = json.loads(cleaned_json_string)
                break
            except Exception as e:
                print(f"Error: {e}. Retrying... ({retries} left)")
                retries -= 1
                if retries == 0:
                    print(f"❌ Failed to annotate {fpath.name}")
                    annotated = None

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
            print(f"✓ Annotated data saved to: {out_path}")

if __name__ == "__main__":
    load_dotenv()
    GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')
    if not GOOGLE_API_KEY:
        raise ValueError("Gemini API key not found. Please set the GOOGLE_API_KEY environment variable.")
    genai.configure(api_key=GOOGLE_API_KEY)
    main()
