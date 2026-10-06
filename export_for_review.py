"""
Export all UNCLASSIFIED questions and chapter options for the manual review UI.
Produces manual_review_data.json consumed by manual_review.html.
"""

import os
import sys
import glob
import json

sys.stdout.reconfigure(encoding='utf-8')

import chapter_config

def main():
    subjects = ["mathematics", "science", "social_science", "english", "hindi", "sanskrit"]
    
    export = {
        "subjects": {},
        "chapter_options": {},
        "corpus_total": 0
    }
    
    # Build chapter options for each subject
    for subj in subjects:
        subj_data = chapter_config.CHAPTERS.get(subj, {})
        is_multi = subj_data.get("is_multi_section", False)
        sections = {}
        for sec_name, ch_list in subj_data.get("sections", {}).items():
            sections[sec_name] = [
                {
                    "number": ch["number"],
                    "name_en": ch["name_en"],
                    "name_hi": ch["name_hi"]
                }
                for ch in ch_list
            ]
        export["chapter_options"][subj] = {
            "is_multi_section": is_multi,
            "sections": sections
        }
    
    # Collect unclassified questions
    total_unclass = 0
    for subj in subjects:
        jev_dir = f"{subj}_data_jevified"
        if not os.path.exists(jev_dir):
            continue
        
        subj_questions = []
        files = sorted(glob.glob(os.path.join(jev_dir, "*.json")))
        
        for fp in files:
            fname = os.path.basename(fp)
            # Extract year from filename pattern like eng_2021i.json, sci_2024ii.json
            year = ""
            for part in fname.replace(".json", "").split("_"):
                if part[:4].isdigit():
                    year = part[:4]
                    break
            
            with open(fp, 'r', encoding='utf-8') as f:
                raw_data = json.load(f)
            
            questions = raw_data.get("questions", raw_data) if isinstance(raw_data, dict) else raw_data
            if not isinstance(questions, list):
                continue

            export["corpus_total"] += len(questions)
            
            for i, q in enumerate(questions):
                ch = str(q.get("chapter", "")).strip()
                if ch.upper() in ("UNCLASSIFIED", "UNKNOWN", "", "NONE"):
                    entry = {
                        "file": fname,
                        "index": i,
                        "year": year,
                        "id": q.get("id", ""),
                        "type": q.get("type", ""),
                        "question": q.get("question", ""),
                        "prashna": q.get("prashna", ""),
                        "context": q.get("context", ""),
                        "instructions": q.get("instructions", ""),
                        "confidence": q.get("confidence", 0.0),
                        "raw_choice": q.get("raw_choice", ""),
                    }
                    # Include options if present
                    if q.get("options"):
                        entry["options"] = q["options"]
                    if q.get("vikalpa"):
                        entry["vikalpa"] = q["vikalpa"]
                    # Include sub-questions if present
                    if q.get("sub_questions"):
                        subs = []
                        for sq in q["sub_questions"]:
                            if isinstance(sq, dict):
                                subs.append({
                                    "question": sq.get("question", ""),
                                    "prashna": sq.get("prashna", "")
                                })
                        if subs:
                            entry["sub_questions"] = subs
                    
                    subj_questions.append(entry)
        
        export["subjects"][subj] = subj_questions
        total_unclass += len(subj_questions)
        print(f"{subj}: {len(subj_questions)} unclassified questions")
    
    out_path = "manual_review_data.json"
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(export, f, ensure_ascii=False, indent=2)
    
    # Also generate manual_review_data.js for instant browser zero-drop loading
    js_path = "manual_review_data.js"
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write("window.INITIAL_REVIEW_DATA = " + json.dumps(export, ensure_ascii=False) + ";\n")
    
    print(f"\nTotal unclassified: {total_unclass}")
    print(f"Exported to {out_path} and {js_path}")


if __name__ == "__main__":
    main()
