"""
Master Merge & Split Runner (Version 0)
========================================
Runs all merge and split operations for all subjects.
All output folders will have a "0" suffix (e.g., mathematics_pro0, english_pro_types0)

Pipeline:
1. Merge → *_pro0/
2. Split by Type → *_pro_types0/
3. Split by Chapter → *_pro_chapters0/
4. Split Types by Chapters → *_pro_type_chapters0/
"""

import os
import json
import glob
import re
import time
from typing import Dict, List, Any

# ANSI color codes
class Colors:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

# Enable ANSI on Windows
os.system("")

# ===== Configuration =====
SUBJECTS = {
    "mathematics": {
        "prefix": "math",
        "annotated_folder": "mathematics_data_annotated",
        "pro_folder": "mathematics_pro0",
        "pro_types": "mathematics_pro_types0",
        "pro_chapters": "mathematics_pro_chapters0",
        "pro_type_chapters": "mathematics_pro_type_chapters0",
        "merged_filename": "mathematics_all_years.json",
        "types": ["objective", "short", "long"]
    },
    "science": {
        "prefix": "sci",
        "annotated_folder": "science_data_annotated",
        "pro_folder": "science_pro0",
        "pro_types": "science_pro_types0",
        "pro_chapters": "science_pro_chapters0",
        "pro_type_chapters": "science_pro_type_chapters0",
        "merged_filename": "science_all_years.json",
        "types": ["objective", "short", "long"]
    },
    "social_science": {
        "prefix": "soc",
        "annotated_folder": "social_science_data_annotated",
        "pro_folder": "social_science_pro0",
        "pro_types": "social_science_pro_types0",
        "pro_chapters": "social_science_pro_chapters0",
        "pro_type_chapters": "social_science_pro_type_chapters0",
        "merged_filename": "social_science_all_years.json",
        "types": ["objective", "short", "long"]
    },
    "hindi": {
        "prefix": "hin",
        "annotated_folder": "hindi_data_annotated",
        "pro_folder": "hindi_pro0",
        "pro_types": "hindi_pro_types0",
        "pro_chapters": "hindi_pro_chapters0",
        "pro_type_chapters": "hindi_pro_type_chapters0",
        "merged_filename": "hindi_all_years.json",
        "types": ["objective", "short", "long", "comprehension", "letter_writing", "essay", "translation"]
    },
    "english": {
        "prefix": "eng",
        "annotated_folder": "english_data_annotated",
        "pro_folder": "english_pro0",
        "pro_types": "english_pro_types0",
        "pro_chapters": "english_pro_chapters0",
        "pro_type_chapters": "english_pro_type_chapters0",
        "merged_filename": "english_all_years.json",
        "types": ["objective", "short", "long", "comprehension", "letter_writing", "essay", "translation"]
    },
    "sanskrit": {
        "prefix": "san",
        "annotated_folder": "sanskrit_data_annotated",
        "pro_folder": "sanskrit_pro0",
        "pro_types": "sanskrit_pro_types0",
        "pro_chapters": "sanskrit_pro_chapters0",
        "pro_type_chapters": "sanskrit_pro_type_chapters0",
        "merged_filename": "sanskrit_all_years.json",
        "types": ["objective", "short", "long", "comprehension", "letter_writing", "essay", "translation"]
    },
}


# ===== Helper Functions =====

def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\-\_\s]", "", value)
    value = re.sub(r"[\s\-]+", "-", value)
    return value or "unknown"


def normalize_type(type_value: str) -> str:
    if not type_value:
        return "unknown"
    type_lower = type_value.lower().strip()
    
    if type_lower in ["objective", "mcq", "multiple choice", "multiple_choice"]:
        return "objective"
    elif type_lower in ["short", "short answer", "short_answer", "sa"]:
        return "short"
    elif type_lower in ["long", "long answer", "long_answer", "la", "descriptive"]:
        return "long"
    elif type_lower in ["comprehension", "passage", "gadyansh", "poem", "poetry"]:
        return "comprehension"
    elif type_lower in ["letter_writing", "letter", "patra_lekhan", "patra"]:
        return "letter_writing"
    elif type_lower in ["essay", "nibandh", "anuched", "paragraph"]:
        return "essay"
    elif type_lower in ["translation", "anuvad"]:
        return "translation"
    else:
        return "unknown"


def read_items_from_file(file_path: str) -> List[Dict[str, Any]]:
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        for key in ("questions", "data", "items", "records"):
            value = data.get(key)
            if isinstance(value, list):
                return value
    return []


# ===== Phase Functions =====

def merge_subject(subject_name: str, config: Dict) -> bool:
    """Merge all annotated JSON files for a subject."""
    source_dir = config["annotated_folder"]
    output_dir = config["pro_folder"]
    prefix = config["prefix"]
    
    if not os.path.exists(source_dir):
        return False
    
    os.makedirs(output_dir, exist_ok=True)
    
    input_files = sorted(glob.glob(os.path.join(source_dir, f"{prefix}_*.json")))
    if not input_files:
        return False
    
    grouped_by_year: Dict[str, List[Dict[str, Any]]] = {}
    
    for file_path in input_files:
        try:
            items = read_items_from_file(file_path)
        except (json.JSONDecodeError, OSError):
            continue
        
        base = os.path.basename(file_path)
        year = "".join(ch for ch in base if ch.isdigit())
        if not year:
            year = base
        grouped_by_year.setdefault(year, []).extend(items)
    
    def year_sort_key(k: str):
        try:
            return int(k)
        except ValueError:
            return k
    
    ordered_years = sorted(grouped_by_year.keys(), key=year_sort_key)
    ordered_obj = {y: grouped_by_year[y] for y in ordered_years}
    
    # Also save all_questions.json for compatibility
    all_questions_path = os.path.join(output_dir, "all_questions.json")
    with open(all_questions_path, "w", encoding="utf-8") as f:
        json.dump(ordered_obj, f, ensure_ascii=False, indent=2)
    
    output_path = os.path.join(output_dir, config["merged_filename"])
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(ordered_obj, f, ensure_ascii=False, indent=2)
    
    total_items = sum(len(v) for v in grouped_by_year.values())
    return True


def split_by_type(subject_name: str, config: Dict) -> bool:
    """Split merged data by question type."""
    source_path = os.path.join(config["pro_folder"], "all_questions.json")
    output_dir = config["pro_types"]
    
    if not os.path.exists(source_path):
        return False
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(source_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if not isinstance(data, dict):
        return False
    
    types_data: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
    
    for year, items in data.items():
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            question_type = normalize_type(item.get("type", ""))
            if question_type not in types_data:
                types_data[question_type] = {}
            types_data[question_type].setdefault(year, []).append(item)
    
    manifest = []
    for type_name, year_map in types_data.items():
        try:
            ordered_years = sorted(year_map.keys(), key=lambda y: int(y))
        except ValueError:
            ordered_years = sorted(year_map.keys())
        ordered_obj = {y: year_map[y] for y in ordered_years}
        
        filename = f"type-{type_name}.json"
        out_path = os.path.join(output_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(ordered_obj, f, ensure_ascii=False, indent=2)
        
        total = sum(len(v) for v in year_map.values())
        manifest.append({"type": type_name, "file": filename, "total_items": total, "years": len(year_map)})
    
    with open(os.path.join(output_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    return True


def split_by_chapter(subject_name: str, config: Dict) -> bool:
    """Split merged data by chapter."""
    source_path = os.path.join(config["pro_folder"], "all_questions.json")
    output_dir = config["pro_chapters"]
    
    if not os.path.exists(source_path):
        return False
    
    os.makedirs(output_dir, exist_ok=True)
    
    with open(source_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    if not isinstance(data, dict):
        return False
    
    chapters: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
    
    for year, items in data.items():
        if not isinstance(items, list):
            continue
        for item in items:
            if not isinstance(item, dict):
                continue
            chapter_id = item.get("chapter")
            if chapter_id is None or chapter_id == "":
                chapter_id = item.get("chapter_name")
            if chapter_id is None or chapter_id == "":
                chapter_id = "unknown"
            
            chapter_key = str(chapter_id)
            if chapter_key not in chapters:
                chapters[chapter_key] = {}
            chapters[chapter_key].setdefault(year, []).append(item)
    
    manifest = []
    for chapter_key, year_map in chapters.items():
        try:
            ordered_years = sorted(year_map.keys(), key=lambda y: int(y))
        except ValueError:
            ordered_years = sorted(year_map.keys())
        ordered_obj = {y: year_map[y] for y in ordered_years}
        
        filename = f"chapter-{slugify(chapter_key)}.json"
        out_path = os.path.join(output_dir, filename)
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(ordered_obj, f, ensure_ascii=False, indent=2)
        
        total = sum(len(v) for v in year_map.values())
        manifest.append({"chapter": chapter_key, "file": filename, "total_items": total, "years": len(year_map)})
    
    with open(os.path.join(output_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, ensure_ascii=False, indent=2)
    
    return True


def split_types_by_chapters(subject_name: str, config: Dict) -> bool:
    """Split each type file by chapters."""
    types_dir = config["pro_types"]
    base_output_dir = config["pro_type_chapters"]
    types_list = config["types"]
    
    if not os.path.exists(types_dir):
        return False
    
    os.makedirs(base_output_dir, exist_ok=True)
    
    overall_manifest = []
    
    for type_name in types_list:
        source_file = os.path.join(types_dir, f"type-{type_name}.json")
        if not os.path.exists(source_file):
            continue
        
        output_dir = os.path.join(base_output_dir, f"{type_name}_chapters")
        os.makedirs(output_dir, exist_ok=True)
        
        with open(source_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        
        if not isinstance(data, dict):
            continue
        
        chapters: Dict[str, Dict[str, List[Dict[str, Any]]]] = {}
        
        for year, items in data.items():
            if not isinstance(items, list):
                continue
            for item in items:
                if not isinstance(item, dict):
                    continue
                chapter_id = item.get("chapter")
                if chapter_id is None or chapter_id == "":
                    chapter_id = item.get("chapter_name")
                if chapter_id is None or chapter_id == "":
                    chapter_id = "unknown"
                
                chapter_key = str(chapter_id)
                if chapter_key not in chapters:
                    chapters[chapter_key] = {}
                chapters[chapter_key].setdefault(year, []).append(item)
        
        manifest = []
        for chapter_key, year_map in chapters.items():
            try:
                ordered_years = sorted(year_map.keys(), key=lambda y: int(y))
            except ValueError:
                ordered_years = sorted(year_map.keys())
            ordered_obj = {y: year_map[y] for y in ordered_years}
            
            filename = f"chapter-{slugify(chapter_key)}.json"
            out_path = os.path.join(output_dir, filename)
            with open(out_path, "w", encoding="utf-8") as f:
                json.dump(ordered_obj, f, ensure_ascii=False, indent=2)
            
            total = sum(len(v) for v in year_map.values())
            manifest.append({"chapter": chapter_key, "file": filename, "total_items": total, "years": len(year_map)})
        
        manifest_path = os.path.join(output_dir, "manifest.json")
        with open(manifest_path, "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, indent=2)
        
        overall_manifest.append({
            "type": type_name,
            "total_chapters": len(chapters),
            "total_items": sum(e["total_items"] for e in manifest)
        })
    
    overall_manifest_path = os.path.join(base_output_dir, "overall_manifest.json")
    with open(overall_manifest_path, "w", encoding="utf-8") as f:
        json.dump(overall_manifest, f, ensure_ascii=False, indent=2)
    
    return True


# ===== UI Functions =====

def print_header(text, color=Colors.CYAN):
    width = 70
    print()
    print(f"  {color}{Colors.BOLD}╔{'═' * (width - 4)}╗{Colors.RESET}")
    print(f"  {color}{Colors.BOLD}║{Colors.RESET}  {Colors.WHITE}{Colors.BOLD}{text:^{width - 8}}{Colors.RESET}  {color}{Colors.BOLD}║{Colors.RESET}")
    print(f"  {color}{Colors.BOLD}╚{'═' * (width - 4)}╝{Colors.RESET}")
    print()


def print_phase(phase_num, phase_name, emoji, output_suffix):
    print()
    print(f"  {Colors.MAGENTA}{'─' * 66}{Colors.RESET}")
    print(f"  {Colors.MAGENTA}{Colors.BOLD}  {emoji} Phase {phase_num}: {phase_name}{Colors.RESET}")
    print(f"  {Colors.DIM}  Output: *_{output_suffix}{Colors.RESET}")
    print(f"  {Colors.MAGENTA}{'─' * 66}{Colors.RESET}")
    print()


def run_phase(phase_func, phase_name):
    success = 0
    failed = 0
    
    for i, (subj_name, config) in enumerate(SUBJECTS.items(), 1):
        display_name = subj_name.replace("_", " ").title()
        print(f"  {Colors.CYAN}🔄 [{i}/6] {display_name:<20}{Colors.RESET}", end="", flush=True)
        
        start = time.time()
        try:
            result = phase_func(subj_name, config)
            duration = time.time() - start
            
            if result:
                print(f"\r  {Colors.GREEN}✅ [{i}/6] {display_name:<20} {Colors.DIM}({duration:.1f}s){Colors.RESET}")
                success += 1
            else:
                print(f"\r  {Colors.YELLOW}⚠️  [{i}/6] {display_name:<20} {Colors.DIM}(Skipped - no input){Colors.RESET}")
        except Exception as e:
            print(f"\r  {Colors.RED}❌ [{i}/6] {display_name:<20} Error: {str(e)[:40]}{Colors.RESET}")
            failed += 1
    
    return success, failed


def main():
    print_header("MASTER MERGE & SPLIT RUNNER (v0)", Colors.BLUE)
    
    print(f"  {Colors.DIM}All output folders will have '0' suffix.{Colors.RESET}")
    print(f"  {Colors.WHITE}Subjects: {', '.join(s.replace('_', ' ').title() for s in SUBJECTS)}{Colors.RESET}")
    
    total_success = 0
    total_failed = 0
    
    # Phase 1: Merge
    print_phase(1, "MERGE", "📦", "pro0")
    s, f = run_phase(merge_subject, "Merge")
    total_success += s
    total_failed += f
    
    # Phase 2: Split by Type
    print_phase(2, "SPLIT BY TYPE", "📂", "pro_types0")
    s, f = run_phase(split_by_type, "Split by Type")
    total_success += s
    total_failed += f
    
    # Phase 3: Split by Chapter
    print_phase(3, "SPLIT BY CHAPTER", "📚", "pro_chapters0")
    s, f = run_phase(split_by_chapter, "Split by Chapter")
    total_success += s
    total_failed += f
    
    # Phase 4: Split Types by Chapters
    print_phase(4, "SPLIT TYPES BY CHAPTERS", "🗂️", "pro_type_chapters0")
    s, f = run_phase(split_types_by_chapters, "Split Types by Chapters")
    total_success += s
    total_failed += f
    
    # Summary
    print()
    print(f"  {Colors.BLUE}{'═' * 66}{Colors.RESET}")
    print()
    
    if total_failed == 0:
        print(f"  {Colors.GREEN}{Colors.BOLD}🎉 ALL OPERATIONS COMPLETE!{Colors.RESET}")
        print(f"  {Colors.GREEN}   {total_success} operations executed successfully{Colors.RESET}")
    else:
        print(f"  {Colors.YELLOW}{Colors.BOLD}⚠️  COMPLETED WITH SOME ISSUES{Colors.RESET}")
        print(f"  {Colors.CYAN}   Success: {total_success} | Failed: {total_failed}{Colors.RESET}")
    
    print()
    print(f"  {Colors.DIM}Output folders created with '0' suffix:{Colors.RESET}")
    print(f"  {Colors.WHITE}   *_pro0, *_pro_types0, *_pro_chapters0, *_pro_type_chapters0{Colors.RESET}")
    print()


if __name__ == "__main__":
    main()
