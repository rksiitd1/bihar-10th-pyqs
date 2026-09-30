"""
Execute all merge and split scripts using the Jev-classified datasets.
Produces:
  {subject}_pro/
  {subject}_pro_chapters/
  {subject}_pro_types/
  {subject}_pro_types_by_chapters/
"""
import sys, os, subprocess, time, glob
sys.stdout.reconfigure(encoding='utf-8')
sys.stderr.reconfigure(encoding='utf-8')

print("=" * 70)
print("🚀 PHASE 1: MERGING ALL JEVIFIED PAPERS INTO *_pro/")
print("=" * 70)

merge_scripts = [
    "merge_science.py",
    "merge_mathematics.py",
    "merge_social_science.py",
    "merge_english.py",
    "merge_hindi.py",
    "merge_sanskrit.py"
]

for s in merge_scripts:
    t0 = time.time()
    res = subprocess.run([sys.executable, s], capture_output=True, text=True)
    el = time.time() - t0
    if res.returncode == 0:
        print(f"  ✅ {s:25s} completed in {el:.2f}s")
    else:
        print(f"  ❌ {s:25s} failed: {res.stderr[:200]}")

print("\n" + "=" * 70)
print("🚀 PHASE 2: SPLITTING DATASETS BY CHAPTER, TYPE & TYPE-BY-CHAPTER")
print("=" * 70)

split_scripts = sorted(glob.glob("split_*.py"))
for s in split_scripts:
    t0 = time.time()
    res = subprocess.run([sys.executable, s], capture_output=True, text=True)
    el = time.time() - t0
    if res.returncode == 0:
        print(f"  ✅ {s:42s} completed in {el:.2f}s")
    else:
        print(f"  ❌ {s:42s} failed: {res.stderr[:200]}")

print("\n" + "=" * 70)
print("🎉 ALL MERGES AND SPLITS COMPLETED SUCCESSFULLY!")
print("=" * 70)
