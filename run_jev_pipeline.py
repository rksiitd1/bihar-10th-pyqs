"""
Master Pipeline Runner for Jev Classification (Bihar 10th PYQs).
Runs Jev annotation across all 6 subjects using TypeSafe AI's Jev model.
Automatically skips already-classified files, processing only new/unclassified data.
"""

import sys
import time
import os
import json

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

import jev_annotate_subject

def main():
    print("="*70)
    print("🌟 MASTER JEV CLASSIFICATION PIPELINE (TYPESAFE AI) 🌟")
    print("Subjects: Science, Mathematics, Social Science, English, Hindi, Sanskrit")
    print("Workers: 16 parallel workers per subject")
    print("Threshold: 0.50 confidence (sub-0.50 marked UNCLASSIFIED)")
    print("="*70)
    print()

    subjects = [
        "science", 
        "mathematics", 
        "social_science", 
        "english", 
        "hindi", 
        "sanskrit"
    ]
    
    overall_start = time.time()
    summary = {}

    for subject in subjects:
        print(f"\n{'#'*60}")
        print(f"👉 PROCESSING SUBJECT: {subject.upper()}")
        print(f"{'#'*60}")
        
        start_time = time.time()
        
        # Max workers set to 16 for blazing fast throughput
        stats = jev_annotate_subject.annotate_subject(
            subject=subject,
            conf_threshold=0.5,
            max_workers=16,
            overwrite=False
        )
        
        elapsed = time.time() - start_time
        summary[subject] = stats
        print(f"✅ Finished {subject.upper()} in {elapsed:.1f}s")
        time.sleep(2) # Brief cooldown between subjects

    print("\n" + "="*70)
    print("🎉 ALL SUBJECTS COMPLETED!")
    print("="*70)
    
    total_time = time.time() - overall_start
    print(f"Total Pipeline Time: {total_time:.2f} seconds ({total_time/60:.2f} mins)")
    
    # Save overall summary report
    with open("jev_pipeline_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=4, ensure_ascii=False)
        
    print("Overall summary saved to jev_pipeline_summary.json")

if __name__ == "__main__":
    main()
