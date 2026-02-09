"""
Pipeline Audit Script
=====================
Audits the data processing pipeline for all subjects and identifies gaps at each stage.

Pipeline Stages:
  1. Papers       → PDF files in *_papers/
  2. Processing   → JSON files in *_data/
  3. Annotation   → JSON files in *_data_annotated/
  4. Merge        → {subject}_all_years.json in *_pro/
  5. Split        → JSON files in *_pro_types/, *_pro_chapters/, *_pro_type_chapters/
"""

import pathlib
import os

# ANSI color codes for terminal output
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

# Enable ANSI colors on Windows
os.system("")

# Configuration for all subjects
SUBJECTS = {
    "mathematics": {
        "emoji": "🔢",
        "prefix": "math",
        "papers_folder": "mathematics_papers",
        "data_folder": "mathematics_data",
        "annotated_folder": "mathematics_data_annotated",
        "pro_folder": "mathematics_pro",
        "merged_filename": "mathematics_all_years.json",
        "pro_types": "mathematics_pro_types",
        "pro_chapters": "mathematics_pro_chapters",
        "pro_type_chapters": "mathematics_pro_type_chapters",
    },
    "science": {
        "emoji": "🔬",
        "prefix": "sci",
        "papers_folder": "science_papers",
        "data_folder": "science_data",
        "annotated_folder": "science_data_annotated",
        "pro_folder": "science_pro",
        "merged_filename": "science_all_years.json",
        "pro_types": "science_pro_types",
        "pro_chapters": "science_pro_chapters",
        "pro_type_chapters": "science_pro_type_chapters",
    },
    "social_science": {
        "emoji": "🌍",
        "prefix": "soc",
        "papers_folder": "social_science_papers",
        "data_folder": "social_science_data",
        "annotated_folder": "social_science_data_annotated",
        "pro_folder": "social_science_pro",
        "merged_filename": "social_science_all_years.json",
        "pro_types": "social_science_pro_types",
        "pro_chapters": "social_science_pro_chapters",
        "pro_type_chapters": "social_science_pro_type_chapters",
    },
    "hindi": {
        "emoji": "📖",
        "prefix": "hin",
        "papers_folder": "hindi_papers",
        "data_folder": "hindi_data",
        "annotated_folder": "hindi_data_annotated",
        "pro_folder": "hindi_pro",
        "merged_filename": "hindi_all_years.json",
        "pro_types": "hindi_pro_types",
        "pro_chapters": "hindi_pro_chapters",
        "pro_type_chapters": "hindi_pro_type_chapters",
    },
    "english": {
        "emoji": "📝",
        "prefix": "eng",
        "papers_folder": "english_papers",
        "data_folder": "english_data",
        "annotated_folder": "english_data_annotated",
        "pro_folder": "english_pro",
        "merged_filename": "english_all_years.json",
        "pro_types": "english_pro_types",
        "pro_chapters": "english_pro_chapters",
        "pro_type_chapters": "english_pro_type_chapters",
    },
    "sanskrit": {
        "emoji": "🕉️",
        "prefix": "san",
        "papers_folder": "sanskrit_papers",
        "data_folder": "sanskrit_data",
        "annotated_folder": "sanskrit_data_annotated",
        "pro_folder": "sanskrit_pro",
        "merged_filename": "sanskrit_all_years.json",
        "pro_types": "sanskrit_pro_types",
        "pro_chapters": "sanskrit_pro_chapters",
        "pro_type_chapters": "sanskrit_pro_type_chapters",
    },
}

# Expected years and sittings
EXPECTED_PAPERS = []
for year in range(2011, 2026):
    EXPECTED_PAPERS.append(f"{year}i")
    if year >= 2014:
        EXPECTED_PAPERS.append(f"{year}ii")


def get_file_stems(folder_path, extension):
    """Get all file stems from a folder."""
    folder = pathlib.Path(folder_path)
    if not folder.exists():
        return set()
    return {f.stem for f in folder.glob(f"*{extension}")}


def extract_year_sitting(filename, prefix):
    """Extract year+sitting from filename."""
    name = filename.replace(f"{prefix}_", "").replace(".json", "").replace(".pdf", "")
    return name


def audit_subject(subject_name, config, base_path):
    """Audit a single subject."""
    prefix = config["prefix"]
    
    papers = get_file_stems(base_path / config["papers_folder"], ".pdf")
    data = get_file_stems(base_path / config["data_folder"], ".json")
    annotated = get_file_stems(base_path / config["annotated_folder"], ".json")
    
    # Check for merged file (using correct filename)
    pro_folder = base_path / config["pro_folder"]
    merged_file = pro_folder / config["merged_filename"]
    merged_exists = merged_file.exists()
    
    # Check split folders
    pro_types = base_path / config["pro_types"]
    pro_chapters = base_path / config["pro_chapters"]
    pro_type_chapters = base_path / config["pro_type_chapters"]
    
    # Count actual JSON files (excluding manifest.json)
    def count_data_files(folder):
        if not folder.exists():
            return 0
        return len([f for f in folder.glob("*.json") if f.name != "manifest.json"])
    
    types_count = count_data_files(pro_types)
    chapters_count = count_data_files(pro_chapters)
    type_chapters_count = sum(
        count_data_files(subfolder) 
        for subfolder in pro_type_chapters.iterdir() 
        if subfolder.is_dir()
    ) if pro_type_chapters.exists() else 0
    
    papers_normalized = {extract_year_sitting(p, prefix) for p in papers}
    data_normalized = {extract_year_sitting(d, prefix) for d in data}
    annotated_normalized = {extract_year_sitting(a, prefix) for a in annotated}
    
    gaps = {
        "1_papers_missing": sorted([e for e in EXPECTED_PAPERS if e not in papers_normalized]),
        "2_not_processed": sorted([p for p in papers_normalized if p not in data_normalized]),
        "3_not_annotated": sorted([d for d in data_normalized if d not in annotated_normalized]),
        "4_not_merged": len(annotated_normalized) > 0 and not merged_exists,
        "5_not_split": {
            "types": merged_exists and types_count == 0,
            "chapters": merged_exists and chapters_count == 0,
            "type_chapters": merged_exists and types_count > 0 and type_chapters_count == 0,
        }
    }
    
    stats = {
        "papers": len(papers),
        "processed": len(data),
        "annotated": len(annotated),
        "merged": merged_exists,
        "types_count": types_count,
        "chapters_count": chapters_count,
        "type_chapters_count": type_chapters_count,
    }
    
    return gaps, stats


def status_badge(ok, ok_text="✓", fail_text="✗"):
    """Return a colored status badge."""
    if ok:
        return f"{Colors.GREEN}[{ok_text}]{Colors.RESET}"
    else:
        return f"{Colors.RED}[{fail_text}]{Colors.RESET}"


def progress_bar(current, total, width=20):
    """Create a visual progress bar."""
    if total == 0:
        pct = 0
    else:
        pct = current / total
    filled = int(width * pct)
    empty = width - filled
    bar = f"{Colors.GREEN}{'█' * filled}{Colors.DIM}{'░' * empty}{Colors.RESET}"
    return f"{bar} {current}/{total}"


def print_subject_report(subject_name, config, gaps, stats):
    """Print a beautiful report for a subject."""
    emoji = config["emoji"]
    display_name = subject_name.replace("_", " ").title()
    
    # Header
    print()
    print(f"  {Colors.BOLD}{Colors.MAGENTA}╔{'═' * 66}╗{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.MAGENTA}║{Colors.RESET}  {emoji} {Colors.BOLD}{Colors.WHITE}{display_name:^60}{Colors.RESET}  {Colors.MAGENTA}║{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.MAGENTA}╚{'═' * 66}╝{Colors.RESET}")
    
    # Pipeline Progress Table
    print()
    print(f"  {Colors.CYAN}┌{'─' * 20}┬{'─' * 12}┬{'─' * 30}┐{Colors.RESET}")
    print(f"  {Colors.CYAN}│{Colors.BOLD} {'Stage':<18} │ {'Status':^10} │ {'Details':<28} │{Colors.RESET}")
    print(f"  {Colors.CYAN}├{'─' * 20}┼{'─' * 12}┼{'─' * 30}┤{Colors.RESET}")
    
    # Stage 1: Papers
    missing_papers = len(gaps["1_papers_missing"])
    total_expected = len(EXPECTED_PAPERS)
    papers_ok = missing_papers == 0
    papers_status = status_badge(papers_ok, "✓", f"-{missing_papers}")
    papers_detail = progress_bar(stats["papers"], total_expected)
    print(f"  {Colors.CYAN}│{Colors.RESET} {'1. Papers':<18} │ {papers_status:^21} │ {papers_detail:<39} {Colors.CYAN}│{Colors.RESET}")
    
    # Stage 2: Processing
    not_processed = len(gaps["2_not_processed"])
    proc_ok = not_processed == 0
    proc_status = status_badge(proc_ok, "✓", f"-{not_processed}")
    proc_detail = progress_bar(stats["processed"], stats["papers"])
    print(f"  {Colors.CYAN}│{Colors.RESET} {'2. Processing':<18} │ {proc_status:^21} │ {proc_detail:<39} {Colors.CYAN}│{Colors.RESET}")
    
    # Stage 3: Annotation
    not_annotated = len(gaps["3_not_annotated"])
    ann_ok = not_annotated == 0
    ann_status = status_badge(ann_ok, "✓", f"-{not_annotated}")
    ann_detail = progress_bar(stats["annotated"], stats["processed"])
    print(f"  {Colors.CYAN}│{Colors.RESET} {'3. Annotation':<18} │ {ann_status:^21} │ {ann_detail:<39} {Colors.CYAN}│{Colors.RESET}")
    
    # Stage 4: Merge
    merge_ok = stats["merged"]
    merge_status = status_badge(merge_ok, "✓", "✗")
    merge_detail = config["merged_filename"] if merge_ok else "Not created"
    print(f"  {Colors.CYAN}│{Colors.RESET} {'4. Merge':<18} │ {merge_status:^21} │ {merge_detail:<28} {Colors.CYAN}│{Colors.RESET}")
    
    # Stage 5: Split
    split_ok = stats["merged"] and stats["types_count"] > 0 and stats["chapters_count"] > 0
    split_status = status_badge(split_ok, "✓", "✗")
    split_parts = []
    split_parts.append(f"T:{stats['types_count']}")
    split_parts.append(f"C:{stats['chapters_count']}")
    split_parts.append(f"TC:{stats['type_chapters_count']}")
    split_detail = " │ ".join(split_parts)
    print(f"  {Colors.CYAN}│{Colors.RESET} {'5. Split':<18} │ {split_status:^21} │ {split_detail:<28} {Colors.CYAN}│{Colors.RESET}")
    
    print(f"  {Colors.CYAN}└{'─' * 20}┴{'─' * 12}┴{'─' * 30}┘{Colors.RESET}")
    
    # Show gaps if any
    has_gaps = (gaps["1_papers_missing"] or gaps["2_not_processed"] or 
                gaps["3_not_annotated"] or gaps["4_not_merged"] or 
                any(gaps["5_not_split"].values()))
    
    if has_gaps:
        print()
        print(f"  {Colors.YELLOW}⚠ Gaps Found:{Colors.RESET}")
        
        if gaps["1_papers_missing"]:
            print(f"    {Colors.RED}• Missing Papers:{Colors.RESET} {', '.join(gaps['1_papers_missing'][:10])}", end="")
            if len(gaps["1_papers_missing"]) > 10:
                print(f" (+{len(gaps['1_papers_missing']) - 10} more)")
            else:
                print()
        
        if gaps["2_not_processed"]:
            print(f"    {Colors.RED}• Not Processed:{Colors.RESET} {', '.join(gaps['2_not_processed'])}")
        
        if gaps["3_not_annotated"]:
            print(f"    {Colors.RED}• Not Annotated:{Colors.RESET} {', '.join(gaps['3_not_annotated'])}")
        
        if gaps["4_not_merged"]:
            print(f"    {Colors.RED}• Merge Pending:{Colors.RESET} Run merge_{subject_name}.py")
        
        split_pending = []
        if gaps["5_not_split"]["types"]:
            split_pending.append("by_type")
        if gaps["5_not_split"]["chapters"]:
            split_pending.append("by_chapter")
        if gaps["5_not_split"]["type_chapters"]:
            split_pending.append("types_by_chapters")
        if split_pending:
            print(f"    {Colors.RED}• Split Pending:{Colors.RESET} {', '.join(split_pending)}")


def print_summary(all_gaps, all_stats):
    """Print overall summary."""
    print()
    print(f"  {Colors.BOLD}{Colors.BLUE}╔{'═' * 66}╗{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.BLUE}║{Colors.RESET}  📊 {Colors.BOLD}{Colors.WHITE}{'OVERALL SUMMARY':^58}{Colors.RESET}  {Colors.BLUE}║{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.BLUE}╚{'═' * 66}╝{Colors.RESET}")
    
    # Calculate totals
    total_papers = sum(s["papers"] for s in all_stats.values())
    total_processed = sum(s["processed"] for s in all_stats.values())
    total_annotated = sum(s["annotated"] for s in all_stats.values())
    total_merged = sum(1 for s in all_stats.values() if s["merged"])
    total_split = sum(1 for s in all_stats.values() if s["merged"] and s["types_count"] > 0 and s["chapters_count"] > 0)
    
    total_missing = sum(len(g["1_papers_missing"]) for g in all_gaps.values())
    total_not_proc = sum(len(g["2_not_processed"]) for g in all_gaps.values())
    total_not_ann = sum(len(g["3_not_annotated"]) for g in all_gaps.values())
    
    print()
    print(f"  {Colors.CYAN}┌{'─' * 32}┬{'─' * 32}┐{Colors.RESET}")
    print(f"  {Colors.CYAN}│{Colors.BOLD} {'Metric':<30} │ {'Value':^30} │{Colors.RESET}")
    print(f"  {Colors.CYAN}├{'─' * 32}┼{'─' * 32}┤{Colors.RESET}")
    print(f"  {Colors.CYAN}│{Colors.RESET} {'Total Papers Collected':<30} │ {Colors.GREEN}{total_papers:^30}{Colors.RESET} {Colors.CYAN}│{Colors.RESET}")
    print(f"  {Colors.CYAN}│{Colors.RESET} {'Total Processed':<30} │ {Colors.GREEN}{total_processed:^30}{Colors.RESET} {Colors.CYAN}│{Colors.RESET}")
    print(f"  {Colors.CYAN}│{Colors.RESET} {'Total Annotated':<30} │ {Colors.GREEN}{total_annotated:^30}{Colors.RESET} {Colors.CYAN}│{Colors.RESET}")
    print(f"  {Colors.CYAN}│{Colors.RESET} {'Subjects Merged (6 total)':<30} │ {Colors.GREEN}{total_merged:^30}{Colors.RESET} {Colors.CYAN}│{Colors.RESET}")
    print(f"  {Colors.CYAN}│{Colors.RESET} {'Subjects Fully Split (6 total)':<30} │ {Colors.GREEN}{total_split:^30}{Colors.RESET} {Colors.CYAN}│{Colors.RESET}")
    print(f"  {Colors.CYAN}├{'─' * 32}┼{'─' * 32}┤{Colors.RESET}")
    
    missing_color = Colors.GREEN if total_missing == 0 else Colors.RED
    not_proc_color = Colors.GREEN if total_not_proc == 0 else Colors.RED
    not_ann_color = Colors.GREEN if total_not_ann == 0 else Colors.RED
    
    print(f"  {Colors.CYAN}│{Colors.RESET} {'Missing Papers (All Subjects)':<30} │ {missing_color}{total_missing:^30}{Colors.RESET} {Colors.CYAN}│{Colors.RESET}")
    print(f"  {Colors.CYAN}│{Colors.RESET} {'Not Processed':<30} │ {not_proc_color}{total_not_proc:^30}{Colors.RESET} {Colors.CYAN}│{Colors.RESET}")
    print(f"  {Colors.CYAN}│{Colors.RESET} {'Not Annotated':<30} │ {not_ann_color}{total_not_ann:^30}{Colors.RESET} {Colors.CYAN}│{Colors.RESET}")
    print(f"  {Colors.CYAN}└{'─' * 32}┴{'─' * 32}┘{Colors.RESET}")
    
    # Final verdict
    all_complete = (total_missing == 0 and total_not_proc == 0 and 
                    total_not_ann == 0 and total_merged == 6 and total_split == 6)
    
    print()
    if all_complete:
        print(f"  {Colors.GREEN}{Colors.BOLD}🎉 ALL SUBJECTS FULLY PROCESSED! Pipeline is complete.{Colors.RESET}")
    else:
        print(f"  {Colors.YELLOW}{Colors.BOLD}⚠️  Some gaps exist in the pipeline. Review subject reports above.{Colors.RESET}")
    print()


def main():
    base_path = pathlib.Path(".")
    
    # Title
    print()
    print(f"  {Colors.BOLD}{Colors.WHITE}╔{'═' * 66}╗{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.WHITE}║{Colors.RESET}  🔍 {Colors.BOLD}{Colors.CYAN}{'BIHAR BOARD CLASS 10 - PIPELINE AUDIT':^56}{Colors.RESET}  {Colors.WHITE}║{Colors.RESET}")
    print(f"  {Colors.BOLD}{Colors.WHITE}╚{'═' * 66}╝{Colors.RESET}")
    
    all_gaps = {}
    all_stats = {}
    
    for subject_name, config in SUBJECTS.items():
        gaps, stats = audit_subject(subject_name, config, base_path)
        all_gaps[subject_name] = gaps
        all_stats[subject_name] = stats
        print_subject_report(subject_name, config, gaps, stats)
    
    print_summary(all_gaps, all_stats)


if __name__ == "__main__":
    main()
