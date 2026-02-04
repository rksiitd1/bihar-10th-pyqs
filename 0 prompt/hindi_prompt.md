# Hindi Data Pipeline Execution

### 🎯 Objective
Execute the complete data processing pipeline for Bihar Board Class 10 Hindi Previous Year Questions.

---

### 🚀 Pipeline Execution
> [!IMPORTANT]
> Execute the following commands **sequentially**. Each script depends on the output of the previous one.

```powershell
cd bihar-10th-pyqs
python batch_processing_hindi.py
python batch_annotate_hindi.py
python merge_hindi.py
python split_hindi_by_chapter.py
python split_hindi_by_type.py
python split_hindi_types_by_chapters.py
```

### 📝 Finalization
1. Verify output in `hindi_pro/` directory.
2. Stage and commit changes.
