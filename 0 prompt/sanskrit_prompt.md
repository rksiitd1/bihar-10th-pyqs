# Sanskrit Data Pipeline Execution

### 🎯 Objective
Execute the complete data processing pipeline for Bihar Board Class 10 Sanskrit Previous Year Questions.

---

### 🚀 Pipeline Execution
> [!IMPORTANT]
> Execute the following commands **sequentially**. Each script depends on the output of the previous one.

```powershell
cd bihar-10th-pyqs
python batch_processing_sanskrit.py
python batch_annotate_sanskrit.py
python merge_sanskrit.py
python split_sanskrit_by_chapter.py
python split_sanskrit_by_type.py
python split_sanskrit_types_by_chapters.py
```

### 📝 Finalization
1. Verify output in `sanskrit_pro/` directory.
2. Stage and commit changes.
