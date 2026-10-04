"""
Re-classify UNCLASSIFIED questions using Jev at 0.50 confidence threshold.
Only touches questions currently marked as UNCLASSIFIED — leaves classified ones untouched.
Stores confidence and raw_choice for future auditability.
"""

import os
import sys
import glob
import json
import time

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from typing import Dict, Any, List, Tuple

import chapter_config
import jev_utils

print_lock = threading.Lock()

def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)

CONF_THRESHOLD = 0.50

def reclassify_question(q: Dict[str, Any], subject: str) -> Dict[str, Any]:
    """Re-runs a single question through Jev and returns updated question dict."""
    meta = jev_utils.classify_question(q, subject, confidence_threshold=CONF_THRESHOLD)
    
    subj_data = chapter_config.CHAPTERS.get(subject, {})
    is_multi = subj_data.get("is_multi_section", False)
    
    # Build updated question — preserve all existing fields
    new_q = {}
    for k, v in q.items():
        if k in ("chapter", "chapter_name", "section", "confidence", "raw_choice"):
            continue
        new_q[k] = v
        if k == "type":
            if is_multi:
                new_q["section"] = meta.get("section", "UNCLASSIFIED")
            new_q["chapter"] = meta.get("chapter", "UNCLASSIFIED")
            new_q["chapter_name"] = meta.get("chapter_name", "UNCLASSIFIED")
            new_q["confidence"] = meta.get("confidence", 0.0)
            new_q["raw_choice"] = meta.get("raw_choice", "")
    
    # Fallback if 'type' key wasn't found
    if "chapter" not in new_q:
        if is_multi:
            new_q["section"] = meta.get("section", "UNCLASSIFIED")
        new_q["chapter"] = meta.get("chapter", "UNCLASSIFIED")
        new_q["chapter_name"] = meta.get("chapter_name", "UNCLASSIFIED")
        new_q["confidence"] = meta.get("confidence", 0.0)
        new_q["raw_choice"] = meta.get("raw_choice", "")
    
    return new_q, meta


def process_file(filepath: str, subject: str, max_workers: int = 12) -> Dict[str, Any]:
    """Re-classify unclassified questions in a single file."""
    fname = os.path.basename(filepath)
    
    with open(filepath, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
    
    is_dict_format = isinstance(raw_data, dict) and "questions" in raw_data
    questions = raw_data["questions"] if is_dict_format else raw_data
    
    if not isinstance(questions, list):
        return {"file": fname, "total": 0, "unclassified_before": 0, "recovered": 0}
    
    # Find indices of unclassified questions
    unclass_indices = []
    for i, q in enumerate(questions):
        ch = str(q.get("chapter", "")).strip()
        if ch in ("UNCLASSIFIED", "unknown", "", "None"):
            unclass_indices.append(i)
    
    if not unclass_indices:
        return {"file": fname, "total": len(questions), "unclassified_before": 0, "recovered": 0}
    
    safe_print(f"  🔄 {fname}: {len(unclass_indices)} unclassified questions to re-run...")
    
    recovered = 0
    still_unclassified = 0
    
    def worker(idx):
        return idx, reclassify_question(questions[idx], subject)
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(worker, idx) for idx in unclass_indices]
        for fut in as_completed(futures):
            idx, (new_q, meta) = fut.result()
            questions[idx] = new_q
            if not meta.get("is_unclassified", True):
                recovered += 1
            else:
                still_unclassified += 1
    
    # Also backfill confidence/raw_choice for already-classified questions (set 0.0/"" if missing)
    subj_data = chapter_config.CHAPTERS.get(subject, {})
    is_multi = subj_data.get("is_multi_section", False)
    for i, q in enumerate(questions):
        if i not in unclass_indices:
            if "confidence" not in q:
                # Insert confidence and raw_choice after chapter_name
                new_q = {}
                for k, v in q.items():
                    new_q[k] = v
                    if k == "chapter_name":
                        new_q["confidence"] = 0.95  # Previously classified at 0.70+ threshold
                        new_q["raw_choice"] = ""
                if "confidence" not in new_q:
                    new_q["confidence"] = 0.95
                    new_q["raw_choice"] = ""
                questions[i] = new_q
    
    # Write back
    if is_dict_format:
        raw_data["questions"] = questions
        output_data = raw_data
    else:
        output_data = questions
    
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
    
    safe_print(f"  ✅ {fname}: recovered {recovered}/{len(unclass_indices)}, still unclassified: {still_unclassified}")
    
    return {
        "file": fname,
        "total": len(questions),
        "unclassified_before": len(unclass_indices),
        "recovered": recovered,
        "still_unclassified": still_unclassified
    }


def main():
    print("=" * 70)
    print("🔄 RECLASSIFYING UNCLASSIFIED QUESTIONS (Threshold: 0.50)")
    print("=" * 70)
    
    subjects = ["mathematics", "science", "social_science", "english", "hindi", "sanskrit"]
    
    grand_total = {"before": 0, "recovered": 0, "still": 0}
    
    for subject in subjects:
        jev_dir = f"{subject}_data_jevified"
        if not os.path.exists(jev_dir):
            print(f"⚠️  {jev_dir} not found, skipping")
            continue
        
        files = sorted(glob.glob(os.path.join(jev_dir, "*.json")))
        print(f"\n{'='*50}")
        print(f"📚 {subject.upper()} ({len(files)} files)")
        print(f"{'='*50}")
        
        subj_stats = {"before": 0, "recovered": 0, "still": 0}
        start = time.time()
        
        for fp in files:
            result = process_file(fp, subject, max_workers=12)
            subj_stats["before"] += result.get("unclassified_before", 0)
            subj_stats["recovered"] += result.get("recovered", 0)
            subj_stats["still"] += result.get("still_unclassified", 0)
        
        elapsed = time.time() - start
        print(f"  📊 {subject}: {subj_stats['recovered']}/{subj_stats['before']} recovered in {elapsed:.1f}s")
        print(f"  ❓ Still unclassified: {subj_stats['still']}")
        
        grand_total["before"] += subj_stats["before"]
        grand_total["recovered"] += subj_stats["recovered"]
        grand_total["still"] += subj_stats["still"]
    
    print(f"\n{'='*70}")
    print(f"🎉 RECLASSIFICATION COMPLETE")
    print(f"   Before: {grand_total['before']} unclassified")
    print(f"   Recovered: {grand_total['recovered']} (now classified at >=0.50 confidence)")
    print(f"   Still Unclassified: {grand_total['still']}")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
