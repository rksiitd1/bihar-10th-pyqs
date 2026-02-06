import json
import pathlib
import os

def dummy_annotate_questions(questions):
    """Adds dummy chapter fields to each question while maintaining order."""
    annotated = []
    for q in questions:
        new_q = {}
        # Ensure type exists to anchor the insertion
        if "type" in q:
            for k, v in q.items():
                new_q[k] = v
                if k == "type":
                    new_q["chapter"] = "0"
                    new_q["chapter_name"] = "0000"
        else:
            # Fallback if type is missing (though it shouldn't be)
            new_q = q.copy()
            new_q["chapter"] = "0"
            new_q["chapter_name"] = "0000"
        annotated.append(new_q)
    return annotated

def main():
    subjects = ["mathematics", "science", "social_science", "sanskrit", "hindi", "english"]
    
    print("🚀 Starting Dummy Annotation for all subjects...")
    print("="*50)
    
    for subject in subjects:
        data_dir = pathlib.Path(f"{subject}_data")
        out_dir = pathlib.Path(f"{subject}_data_annotated")
        
        if not data_dir.exists():
            print(f"⚠️  Skipping {subject}: {data_dir} not found.")
            continue
            
        out_dir.mkdir(exist_ok=True)
        files = list(data_dir.glob("*.json"))
        print(f"📂 Processing {subject} ({len(files)} files)...")
        
        for fpath in files:
            try:
                with open(fpath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                
                # Check if it's a list or a dict containing a list
                if isinstance(data, list):
                    annotated_data = dummy_annotate_questions(data)
                elif isinstance(data, dict) and "questions" in data:
                    data["questions"] = dummy_annotate_questions(data["questions"])
                    annotated_data = data
                else:
                    # Generic handling
                    annotated_data = data
                
                out_path = out_dir / fpath.name
                with open(out_path, 'w', encoding='utf-8') as f:
                    json.dump(annotated_data, f, indent=4, ensure_ascii=False)
                    
            except Exception as e:
                print(f"  ❌ Error processing {fpath.name}: {e}")
                
    print("="*50)
    print("✅ Dummy annotation completed for all available subjects.")

if __name__ == "__main__":
    main()
