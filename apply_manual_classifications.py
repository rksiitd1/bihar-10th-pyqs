"""
Apply manual classifications exported from manual_review.html back into {subject}_data_jevified/
and optionally re-run run_final_merge_split.py.

Usage:
    python apply_manual_classifications.py <path_to_export.json> [--no-split]
"""

import os
import sys
import json
import argparse
import subprocess

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

import chapter_config


def main():
    parser = argparse.ArgumentParser(description="Apply manual classifications to jevified files.")
    parser.add_argument("export_file", help="Path to exported manual classifications JSON file")
    parser.add_argument("--no-split", action="store_true", help="Skip running run_final_merge_split.py")
    args = parser.parse_args()

    if not os.path.exists(args.export_file):
        print(f"❌ File not found: {args.export_file}")
        sys.exit(1)

    with open(args.export_file, "r", encoding="utf-8") as f:
        export_data = json.load(f)

    classifications = export_data.get("classifications", [])
    if not classifications:
        print("⚠️ No classifications found in file.")
        sys.exit(0)

    print(f"Loaded {len(classifications)} manual classifications.")

    # Group classifications by (subject, file)
    by_file = {}
    for item in classifications:
        subj = item.get("subject")
        fname = item.get("file")
        if not subj or not fname:
            continue
        key = (subj, fname)
        if key not in by_file:
            by_file[key] = []
        by_file[key].append(item)

    applied_count = 0
    modified_files = set()

    for (subj, fname), items in by_file.items():
        file_path = os.path.join(f"{subj}_data_jevified", fname)
        if not os.path.exists(file_path):
            print(f"⚠️ Target file not found: {file_path}")
            continue

        with open(file_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        is_dict = isinstance(raw_data, dict) and "questions" in raw_data
        questions = raw_data["questions"] if is_dict else raw_data

        subj_data = chapter_config.CHAPTERS.get(subj, {})
        is_multi = subj_data.get("is_multi_section", False)

        for item in items:
            idx = item.get("index")
            if idx is None or idx < 0 or idx >= len(questions):
                print(f"⚠️ Index {idx} out of range in {fname}")
                continue

            q = questions[idx]
            new_section = item.get("section", "")
            new_chapter = item.get("chapter")
            new_chapter_name = item.get("chapter_name", "")

            # Update question metadata
            if is_multi:
                q["section"] = new_section or "UNCLASSIFIED"
            q["chapter"] = new_chapter if new_chapter is not None else "UNCLASSIFIED"
            q["chapter_name"] = new_chapter_name or "UNCLASSIFIED"
            q["confidence"] = 1.0  # Manually verified
            q["raw_choice"] = f"manual_review::{new_chapter_name}"

            applied_count += 1

        # Save back
        output_data = raw_data if not is_dict else dict(raw_data, questions=questions)
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(output_data, f, indent=4, ensure_ascii=False)

        modified_files.add(file_path)

    print(f"✅ Successfully applied {applied_count} classifications across {len(modified_files)} files.")

    if not args.no_split:
        print("\n🔄 Re-running merge and split pipeline...")
        subprocess.run([sys.executable, "run_final_merge_split.py"], check=True)
        print("🎉 Merge and split complete! All pro folders updated.")


if __name__ == "__main__":
    main()
