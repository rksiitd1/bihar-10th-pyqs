"""
Master STEM Pipeline Runner for Bihar 10th PYQs.
Sequentially runs Jev annotation for:
1. Science (26 files, 16 BSEB chapters)
2. Mathematics (20 files, 15 BSEB chapters)
3. Social Science (26 files, 35 BSEB chapters across 4 sections)
"""

import sys
import time
import json
import os

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

import jev_annotate_subject

def main():
    print("="*70)
    print("🌟 MASTER STEM PIPELINE RUNNER (JEV / TYPESAFE AI) 🌟")
    print("Subjects: Science -> Mathematics -> Social Science")
    print("Workers: 16 parallel workers per subject")
    print("Threshold: 0.70 confidence (sub-0.70 marked UNCLASSIFIED)")
    print("="*70)
    print()

    subjects = ["science", "mathematics", "social_science"]
    overall_start = time.time()
    summary = {}

    for subj in subjects:
        subj_start = time.time()
        print(f"\n{'#'*70}")
        print(f"👉 STARTING SUBJECT: {subj.upper()}")
        print(f"{'#'*70}\n")
        
        # Run with 16 workers
        jev_annotate_subject.annotate_subject(
            subject=subj,
            conf_threshold=0.7,
            max_workers=16,
            limit_files=None,
            overwrite=False
        )
        
        # Load report
        report_file = f"{subj}_jev_report.json"
        if os.path.exists(report_file):
            with open(report_file, 'r', encoding='utf-8') as f:
                rep = json.load(f)
            summary[subj] = rep

    overall_elapsed = time.time() - overall_start

    print("\n" + "="*70)
    print("🏁 ALL 3 STEM SUBJECTS COMPLETED!")
    print(f"⏱️  Total Duration: {overall_elapsed / 60:.1f} minutes ({overall_elapsed:.1f} seconds)")
    print("="*70)
    print(f"{'Subject':16s} | {'Files':6s} | {'Total Qs':9s} | {'Classified':11s} | {'Unclassified':13s} | {'Accuracy':8s}")
    print("-" * 70)

    total_all_q = 0
    total_all_class = 0
    total_all_unclass = 0

    for subj in subjects:
        rep = summary.get(subj, {})
        tot = rep.get("total_questions", 0)
        cls = rep.get("total_classified", 0)
        unc = rep.get("total_unclassified", 0)
        rate = rep.get("classification_rate", 0.0)
        total_all_q += tot
        total_all_class += cls
        total_all_unclass += unc
        print(f"{subj.upper():16s} | {rep.get('total_files', 0):6d} | {tot:9d} | {cls:11d} | {unc:13d} | {rate:6.1f}%")

    print("-" * 70)
    overall_rate = (100.0 * total_all_class / total_all_q) if total_all_q else 0.0
    print(f"{'TOTAL STEM':16s} | {72:6d} | {total_all_q:9d} | {total_all_class:11d} | {total_all_unclass:13d} | {overall_rate:6.1f}%")
    print("="*70 + "\n")

    # Save master summary
    with open("stem_pipeline_summary.json", "w", encoding="utf-8") as f:
        json.dump({
            "total_questions": total_all_q,
            "total_classified": total_all_class,
            "total_unclassified": total_all_unclass,
            "overall_classification_rate": round(overall_rate, 2),
            "total_time_seconds": round(overall_elapsed, 2),
            "subjects": summary
        }, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
