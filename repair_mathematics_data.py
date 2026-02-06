import json
import pathlib
import re
import utils

def repair_json_string(raw_text):
    """
    Attempts to repair common JSON issues in Gemini's math responses.
    """
    # 1. Clean markdown blocks
    text = utils.clean_json_response(raw_text)
    
    # 2. Fix unescaped backslashes
    # We want to escape backslashes that are NOT part of a valid JSON escape.
    # Valid escapes in JSON: \", \\, \/, \b, \f, \n, \r, \t, \uXXXX
    # In math papers, we often see LaTeX like \theta, \sqrt which need to be \\theta, \\sqrt.
    
    # Simple approach: replace all \ with \\, then fix the resulting \\\\ if they were already escaped.
    text = text.replace('\\', '\\\\')
    # If it was already \\, it became \\\\, we want it to stay \\ or become \\\\?
    # Actually, in the raw file, if we see \theta, it should become \\theta.
    # If we see \\theta, it should stay \\theta (which in python string is \\\\theta).
    # Wait, the raw file is a text file. If I see \theta, the character '\' is there.
    # To be a valid JSON string, it must be \\theta.
    
    # Fix: replace any \\\\ back to \\
    text = text.replace('\\\\\\\\', '\\\\')
    
    # 3. Fix trailing commas in objects and arrays
    text = re.sub(r',\s*}', '}', text)
    text = re.sub(r',\s*]', ']', text)
    
    # 4. Fix missing commas between objects/elements
    text = re.sub(r'}\s*{', '}, {', text)
    text = re.sub(r']\s*\[', '], [', text)
    
    return text

def main():
    logger = utils.setup_logger('repair_mathematics', 'logs/repair_mathematics.log')
    print("Repairing Mathematics Data from Raw API Responses...")
    
    raw_folder = pathlib.Path("mathematics_data_raw")
    out_folder = pathlib.Path("mathematics_data")
    out_folder.mkdir(exist_ok=True)
    
    raw_files = list(raw_folder.glob("*_raw.txt"))
    
    if not raw_files:
        print("No raw files found in mathematics_data_raw/")
        return
    
    recovered_count = 0
    already_done = 0
    failed_count = 0
    
    for raw_path in raw_files:
        # Expected json name: math_2021i.json for math_2021i_raw.txt
        json_name = raw_path.name.replace("_raw.txt", ".json")
        out_path = out_folder / json_name
        
        if out_path.exists():
            already_done += 1
            continue
            
        print(f"Processing: {raw_path.name}...")
        
        try:
            with open(raw_path, 'r', encoding='utf-8') as f:
                raw_content = f.read()
                
            repaired_text = repair_json_string(raw_content)
            
            try:
                data = json.loads(repaired_text)
            except json.JSONDecodeError as e:
                # Try a second approach: find the first '[' and last ']'
                start = repaired_text.find('[')
                end = repaired_text.rfind(']')
                if start != -1 and end != -1:
                    try:
                        data = json.loads(repaired_text[start:end+1])
                    except:
                        raise e
                else:
                    raise e
            
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
                
            print(f"✅ Recovered: {json_name}")
            recovered_count += 1
            
        except Exception as e:
            print(f"❌ Failed to repair {raw_path.name}: {e}")
            failed_count += 1
            
    print("\n" + "="*40)
    print(f"Already exist: {already_done}")
    print(f"Successfully recovered: {recovered_count}")
    print(f"Still failing: {failed_count}")
    print("="*40)

if __name__ == "__main__":
    main()
