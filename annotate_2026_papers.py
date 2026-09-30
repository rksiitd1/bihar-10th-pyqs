"""
Annotates all 12 remaining 2026 papers using Jev into their respective *_data_jevified directories.
"""
import sys, os, time
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from jev_annotate_subject import annotate_file

subjects = [
    "science",
    "mathematics",
    "social_science",
    "english",
    "hindi",
    "sanskrit"
]

print("=" * 70, flush=True)
print("🚀 CLASSIFYING ALL 2026 PAPERS WITH JEV (16 WORKERS)", flush=True)
print("=" * 70, flush=True)

total_start = time.time()
results = []

for subj in subjects:
    raw_dir = f"{subj}_data"
    jev_dir = f"{subj}_data_jevified"
    os.makedirs(jev_dir, exist_ok=True)
    
    # Target 2026 papers
    pfx = "math" if subj == "mathematics" else ("soc" if subj == "social_science" else subj[:3])
    for shift in ["i", "ii"]:
        fname = f"{pfx}_2026{shift}.json"
        raw_path = os.path.join(raw_dir, fname)
        jev_path = os.path.join(jev_dir, fname)
        
        if not os.path.exists(raw_path):
            print(f"⚠️  Missing raw file: {raw_path}", flush=True)
            continue
            
        if os.path.exists(jev_path):
            print(f"⏭️  Already exists: {jev_path}", flush=True)
            continue
            
        print(f"\n👉 Annotating {subj.upper()}: {fname}...", flush=True)
        t0 = time.time()
        res = annotate_file(raw_path, jev_dir, subj, conf_threshold=0.7, max_workers=16, overwrite=False)
        el = time.time() - t0
        tot = res.get("total", 0)
        unclass = res.get("unclassified", 0)
        conf = res.get("avg_confidence", 0.0)
        print(f"  ✅ Finished {fname} in {el:.1f}s | {tot - unclass}/{tot} classified (conf: {conf:.2f})", flush=True)
        results.append(res)

total_elapsed = time.time() - total_start
print("\n" + "=" * 70, flush=True)
print(f"🏁 ALL 2026 PAPERS CLASSIFIED IN {total_elapsed:.1f}s ({total_elapsed/60:.2f} min)", flush=True)
print("=" * 70, flush=True)
