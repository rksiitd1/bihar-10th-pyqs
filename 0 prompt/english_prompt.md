# English Data Pipeline Execution

### 🎯 Objective
Execute the complete data processing pipeline for Bihar Board Class 10 English Previous Year Questions.

---

### 🚀 Pipeline Execution
> [!IMPORTANT]
> Execute the following commands **sequentially**. Each script depends on the output of the previous one.

```powershell
cd bihar-10th-pyqs
python batch_processing_english.py
python batch_annotate_english.py
python merge_english.py
python split_english_by_chapter.py
python split_english_by_type.py
python split_english_types_by_chapters.py
```

### 📝 Finalization
1. Verify output in `english_pro/` directory.
2. Stage and commit changes.
