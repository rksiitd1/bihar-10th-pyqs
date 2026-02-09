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
    print("Starting Master Pipeline Runner...")
    print("This script will execute Annotation, Merge, and Split scripts in sequence.")

    # Phase 1: Batch Annotation
    print("\n\n" + "#" * 30)
    print(" PHASE 1: BATCH ANNOTATION ")
    print("#" * 30)
    annotate_scripts = sorted(glob.glob("batch_annotate_*.py"))
    if not annotate_scripts:
        print("No batch_annotate_*.py scripts found.")
    
    for script in annotate_scripts:
        run_script(script)

    # Phase 2: Merge
    print("\n\n" + "#" * 30)
    print(" PHASE 2: MERGE ")
    print("#" * 30)
    merge_scripts = sorted(glob.glob("merge_*.py"))
    if not merge_scripts:
        print("No merge_*.py scripts found.")

    for script in merge_scripts:
        run_script(script)

    # Phase 3: Split
    print("\n\n" + "#" * 30)
    print(" PHASE 3: SPLIT ")
    print("#" * 30)
    # Sorting ensures:
    # 1. split_{subject}_by_chapter.py (c comes first)
    # 2. split_{subject}_by_type.py    (t comes after c)
    # 3. split_{subject}_types_by_chapters.py (types comes after by_type)
    # This dependency order is crucial.
    split_scripts = sorted(glob.glob("split_*.py"))
    if not split_scripts:
        print("No split_*.py scripts found.")

    for script in split_scripts:
        run_script(script)

    print("\n" + "="*60)
    print("🎉 MASTER PIPELINE EXECUTION COMPLETE")
    print("="*60)

if __name__ == "__main__":
    main()
