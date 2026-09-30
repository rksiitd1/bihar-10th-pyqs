"""
Run Jev chapter classification on all pending papers across all 6 subjects.
Skips all already completed papers automatically.
"""
import sys, os, time
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from jev_annotate_subject import annotate_subject

subjects = [
    "science",
    "mathematics",
    "social_science",
    "english",
    "hindi",
    "sanskrit"
]

print("=" * 70, flush=True)
print("🚀 STARTING JEV CHAPTER CLASSIFICATION PIPELINE", flush=True)
print("=" * 70, flush=True)

total_start = time.time()
overall_stats = {}

for subj in subjects:
    print(f"\n{'#' * 60}", flush=True)
    print(f"👉 SUBJECT: {subj.upper()}", flush=True)
    print(f"{'#' * 60}", flush=True)
    
    t0 = time.time()
    # 16 workers for high throughput
    stats = annotate_subject(subj, conf_threshold=0.7, max_workers=16, overwrite=False)
    elapsed = time.time() - t0
    overall_stats[subj] = stats
    print(f"✅ Completed {subj.upper()} in {elapsed:.2f}s", flush=True)

total_elapsed = time.time() - total_start
print("\n" + "=" * 70, flush=True)
print(f"🏁 ALL 6 SUBJECTS JEVIFIED IN {total_elapsed:.2f}s ({total_elapsed/60:.2f} min)", flush=True)
print("=" * 70, flush=True)

for subj, s in overall_stats.items():
    tot = s.get("total_questions", 0)
    unclass = s.get("total_unclassified", 0)
    classified = tot - unclass
    pct = (classified / tot * 100) if tot > 0 else 100
    print(f"  {subj.upper():16s}: {classified}/{tot} classified ({pct:.1f}%) | {s.get('total_files', 0)} files", flush=True)
