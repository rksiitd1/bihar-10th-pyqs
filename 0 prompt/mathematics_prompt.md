# Mathematics Data Pipeline Execution

### 🎯 Objective
Execute the complete data processing pipeline for Bihar Board Class 10 Mathematics Previous Year Questions.

---

### 🚀 Pipeline Execution
> [!IMPORTANT]
> Execute the following commands **sequentially**. Each script depends on the output of the previous one.

```powershell
cd bihar-10th-pyqs
python batch_processing_mathematics.py
python batch_annotate_mathematics.py
python merge_mathematics.py
python split_mathematics_by_chapter.py
python split_mathematics_by_type.py
python split_mathematics_types_by_chapters.py
```

### 📝 Finalization
1. Verify output in `mathematics_pro/` directory.
2. Stage and commit changes.
