# Social Science Data Pipeline Execution

### 🎯 Objective
Execute the complete data processing pipeline for Bihar Board Class 10 Social Science Previous Year Questions.

---

### 🚀 Pipeline Execution
> [!IMPORTANT]
> Execute the following commands **sequentially**. Each script depends on the output of the previous one.

```powershell
cd bihar-10th-pyqs
python batch_processing_social_science.py
python batch_annotate_social_science.py
python merge_social_science.py
python split_social_science_by_chapter.py
python split_social_science_by_type.py
python split_social_science_types_by_chapters.py
```

### 📝 Finalization
1. Verify output in `social_science_pro/` directory.
2. Stage and commit changes.
