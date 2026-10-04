"""
Batch annotator using Jev for Bihar 10th PYQ questions.
Classifies each question into the official BSEB syllabus chapters.
Outputs to {subject}_data_jevified/
"""

import os
import sys
import glob
import json
import time
import argparse

sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')
from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
from typing import Dict, Any, List, Tuple, Optional

import chapter_config
import jev_utils

print_lock = threading.Lock()

def safe_print(*args, **kwargs):
    with print_lock:
        print(*args, **kwargs)

def reorder_question(q: Dict[str, Any], meta: Dict[str, Any], is_multi: bool) -> Dict[str, Any]:
    """Inserts section (if multi), chapter, chapter_name, confidence, raw_choice right after 'type'."""
    new_q = {}
    inserted = False
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
            inserted = True
            
    if not inserted:
        if is_multi:
            new_q["section"] = meta.get("section", "UNCLASSIFIED")
        new_q["chapter"] = meta.get("chapter", "UNCLASSIFIED")
        new_q["chapter_name"] = meta.get("chapter_name", "UNCLASSIFIED")
        new_q["confidence"] = meta.get("confidence", 0.0)
        new_q["raw_choice"] = meta.get("raw_choice", "")
        
    return new_q

def process_single_question(item: Tuple[int, Dict[str, Any]], subject: str, conf_threshold: float) -> Tuple[int, Dict[str, Any], Dict[str, Any]]:
    idx, q = item
    meta = jev_utils.classify_question(q, subject, confidence_threshold=conf_threshold)
    return idx, q, meta

def annotate_file(
    filepath: str,
    output_dir: str,
    subject: str,
    conf_threshold: float = 0.7,
    max_workers: int = 8,
    overwrite: bool = False
) -> Dict[str, Any]:
    """Annotates all questions in a single JSON file."""
    fname = os.path.basename(filepath)
    out_path = os.path.join(output_dir, fname)
    
    # Check if already completed and valid
    if not overwrite and os.path.exists(out_path):
        try:
            with open(out_path, 'r', encoding='utf-8') as f:
                cached = json.load(f)
            cached_qs = cached["questions"] if isinstance(cached, dict) and "questions" in cached else cached
            if isinstance(cached_qs, list) and len(cached_qs) > 0:
                unclass = sum(1 for q in cached_qs if q.get("chapter") == "UNCLASSIFIED")
                safe_print(f"⏭️  Skipping {fname} (already annotated: {len(cached_qs) - unclass}/{len(cached_qs)} classified)")
                return {
                    "file": fname,
                    "total": len(cached_qs),
                    "unclassified": unclass,
                    "avg_confidence": 0.95,
                    "elapsed_seconds": 0.0
                }
        except Exception:
            pass

    with open(filepath, 'r', encoding='utf-8') as f:
        raw_data = json.load(f)
        
    is_dict = isinstance(raw_data, dict) and "questions" in raw_data
    questions = raw_data["questions"] if is_dict else raw_data
    if not isinstance(questions, list):
        safe_print(f"⚠️  Skipping {fname}: unrecognized data structure.")
        return {"file": fname, "total": 0, "success": False}

    subj_data = chapter_config.CHAPTERS.get(subject, {})
    is_multi = subj_data.get("is_multi_section", False)
    
    total = len(questions)
    annotated = [None] * total
    unclassified_count = 0
    confidence_sum = 0.0
    
    safe_print(f"🚀 Annotating {fname} ({total} questions) with Jev [workers={max_workers}]...")
    start_time = time.time()
    
    items = list(enumerate(questions))
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(process_single_question, item, subject, conf_threshold) for item in items]
        for fut in as_completed(futures):
            idx, orig_q, meta = fut.result()
            new_q = reorder_question(orig_q, meta, is_multi)
            annotated[idx] = new_q
            if meta.get("is_unclassified", False):
                unclassified_count += 1
            confidence_sum += meta.get("confidence", 0.0)

    elapsed = time.time() - start_time
    avg_conf = (confidence_sum / total) if total > 0 else 0.0
    
    output_data = raw_data if not is_dict else dict(raw_data, questions=annotated)
    if not is_dict:
        output_data = annotated
        
    os.makedirs(output_dir, exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=4, ensure_ascii=False)
        
    safe_print(f"✅ Finished {fname} in {elapsed:.1f}s | Avg Conf: {avg_conf:.2f} | Unclassified: {unclassified_count}/{total}")
    
    return {
        "file": fname,
        "total": total,
        "unclassified": unclassified_count,
        "avg_confidence": round(avg_conf, 3),
        "elapsed_seconds": round(elapsed, 2)
    }

def annotate_subject(
    subject: str,
    conf_threshold: float = 0.7,
    max_workers: int = 12,
    limit_files: Optional[int] = None,
    overwrite: bool = False
):
    """Processes all files for a subject."""
    in_dir = f"{subject}_data_annotated"
    if not os.path.exists(in_dir):
        in_dir = f"{subject}_data"
    if not os.path.exists(in_dir):
        print(f"❌ Input directory not found: {in_dir}")
        return

    out_dir = f"{subject}_data_jevified"
    os.makedirs(out_dir, exist_ok=True)
    
    files = sorted(glob.glob(os.path.join(in_dir, "*.json")))
    if limit_files:
        files = files[:limit_files]
        
    print(f"\n{'='*60}")
    print(f"📚 STARTING JEV ANNOTATION: {subject.upper()}")
    print(f"📂 Input: {in_dir} ({len(files)} files)")
    print(f"📁 Output: {out_dir}")
    print(f"⚙️  Confidence Threshold: {conf_threshold} | Workers: {max_workers} | Overwrite: {overwrite}")
    print(f"{'='*60}\n")
    
    results = []
    total_questions = 0
    total_unclassified = 0
    
    subj_start = time.time()
    for idx, fp in enumerate(files):
        print(f"[{idx+1}/{len(files)}] ", end="", flush=True)
        res = annotate_file(fp, out_dir, subject, conf_threshold, max_workers, overwrite)
        results.append(res)
        total_questions += res.get("total", 0)
        total_unclassified += res.get("unclassified", 0)
        
    subj_elapsed = time.time() - subj_start
    
    report = {
        "subject": subject,
        "total_files": len(files),
        "total_questions": total_questions,
        "total_classified": total_questions - total_unclassified,
        "total_unclassified": total_unclassified,
        "classification_rate": round(100.0 * (total_questions - total_unclassified) / total_questions, 2) if total_questions else 0.0,
        "total_time_seconds": round(subj_elapsed, 2),
        "file_reports": results
    }
    
    report_path = f"{subject}_jev_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(report, f, indent=2, ensure_ascii=False)
        
    print(f"\n{'='*60}")
    print(f"🎉 COMPLETED: {subject.upper()}")
    print(f"📊 Total Questions: {total_questions}")
    print(f"✅ Classified: {total_questions - total_unclassified} ({report['classification_rate']}%)")
    print(f"❓ Unclassified: {total_unclassified}")
    print(f"⏱️  Total Time: {subj_elapsed:.1f}s")
    print(f"📝 Report saved to: {report_path}")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Jev Annotator for Bihar 10th PYQs")
    parser.add_argument("--subject", choices=["mathematics", "science", "social_science", "english", "hindi", "sanskrit", "all"], default="all")
    parser.add_argument("--file", type=str, help="Specific file path to annotate")
    parser.add_argument("--threshold", type=float, default=0.7, help="Confidence threshold (default: 0.7)")
    parser.add_argument("--workers", type=int, default=12, help="Concurrent workers (default: 12)")
    parser.add_argument("--limit", type=int, default=None, help="Limit number of files per subject")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing annotated files")
    args = parser.parse_args()
    
    if args.file and args.subject != "all":
        out_dir = f"{args.subject}_data_jevified"
        annotate_file(args.file, out_dir, args.subject, args.threshold, args.workers, args.overwrite)
    elif args.subject == "all":
        for subj in ["science", "mathematics", "social_science"]:
            annotate_subject(subj, args.threshold, args.workers, args.limit, args.overwrite)
    else:
        annotate_subject(args.subject, args.threshold, args.workers, args.limit, args.overwrite)
