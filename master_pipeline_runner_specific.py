import subprocess
import glob
import sys
import os
import time

def run_script(script_name):
    """Runs a python script and checking for errors."""
    print(f"\n{'='*60}")
    print(f"🚀 RUNNING: {script_name}")
    print(f"{'='*60}")
    
    start_time = time.time()
    try:
        # Run the script and let it print to the console
        result = subprocess.run([sys.executable, script_name], check=False)
        
        duration = time.time() - start_time
        if result.returncode == 0:
            print(f"\n✅ FINISHED: {script_name} (Time: {duration:.2f}s)")
            return True
        else:
            print(f"\n❌ FAILED: {script_name} (Return Code: {result.returncode})")
            return False
    except Exception as e:
        print(f"\n❌ ERROR execution {script_name}: {e}")
        return False

def main():
    print("Starting TARGETED Pipeline Runner for Hindi & English...")
    print("This script will execute Extraction, Annotation, Merging, and Splitting for Hindi & English only.")

    # Phase 1: Batch Extraction (Targeted)
    print("\n\n" + "#" * 30)
    print(" PHASE 1: TARGETED EXTRACTION ")
    print("#" * 30)
    
    extraction_scripts = [
        "batch_processing_english_all.py",
        "batch_processing_hindi_filtered.py"
    ]
    
    for script in extraction_scripts:
        if os.path.exists(script):
            run_script(script)
        else:
             print(f"❌ Script not found: {script}")

    # Phase 2: Batch Annotation
    print("\n\n" + "#" * 30)
    print(" PHASE 2: BATCH ANNOTATION ")
    print("#" * 30)
    
    annotation_scripts = [
        "batch_annotate_english.py",
        "batch_annotate_hindi.py"
    ]
    
    for script in annotation_scripts:
        if os.path.exists(script):
            run_script(script)
        else:
             print(f"❌ Script not found: {script}")

    # Phase 3: Merge (Hindi & English only)
    print("\n\n" + "#" * 30)
    print(" PHASE 3: MERGE ")
    print("#" * 30)
    
    merge_scripts = [
        "merge_english.py",
        "merge_hindi.py"
    ]

    for script in merge_scripts:
        if os.path.exists(script):
            run_script(script)
        else:
             print(f"❌ Script not found: {script}")

    # Phase 4: Split (Hindi & English only)
    print("\n\n" + "#" * 30)
    print(" PHASE 4: SPLIT ")
    print("#" * 30)
    
    # Sorting ensures order: by_chapter -> by_type -> types_by_chapters
    all_split_scripts = sorted(glob.glob("split_*.py"))
    
    target_split_scripts = [
        s for s in all_split_scripts 
        if "english" in s or "hindi" in s
    ]
    
    if not target_split_scripts:
        print("No split scripts found for English/Hindi.")
    
    for script in target_split_scripts:
        run_script(script)

    print("\n" + "="*60)
    print("🎉 TARGETED PIPELINE EXECUTION COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()
