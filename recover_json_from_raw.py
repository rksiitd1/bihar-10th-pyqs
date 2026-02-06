import json
import pathlib
import sys
import utils

def recover_subject(subject):
    raw_folder = pathlib.Path(f"{subject}_data_raw")
    out_folder = pathlib.Path(f"{subject}_data")
    
    if not raw_folder.exists():
        print(f"❌ Raw folder not found: {raw_folder}")
        return

    out_folder.mkdir(exist_ok=True)
    raw_files = list(raw_folder.glob("*_raw.txt"))
    
    print(f"🔍 Checking {len(raw_files)} raw files for {subject}...")
    
    recovered = 0
    skipped = 0
    failed = 0
    
    for raw_path in raw_files:
        # standard mapping: soc_2023i_raw.txt -> soc_2023i.json
        json_name = raw_path.name.replace("_raw.txt", ".json")
        out_path = out_folder / json_name
        
        if out_path.exists():
            skipped += 1
            continue
            
        print(f"🔄 Recovering {json_name}...", end=" ", flush=True)
        
        try:
            with open(raw_path, 'r', encoding='utf-8') as f:
                raw_text = f.read()
            
            # Use the new robust cleaning logic from utils.py
            cleaned_text = utils.clean_json_response(raw_text)
            data = json.loads(cleaned_text)
            
            with open(out_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            print("✅ DONE")
            recovered += 1
        except Exception as e:
            print(f"❌ FAIL: {e}")
            failed += 1
            
    print(f"\n📊 {subject.upper()} Recovery Summary")
    print(f"   Recovered: {recovered}")
    print(f"   Already exist: {skipped}")
    print(f"   Failed: {failed}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        subjects = sys.argv[1:]
    else:
        # Default to all known subjects if none specified
        subjects = ['science', 'mathematics', 'social_science', 'hindi', 'english', 'sanskrit']
    
    for sub in subjects:
        recover_subject(sub)
        print("-" * 30)
