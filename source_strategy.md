# BSEB Class 10 PYQ Collection - Source Strategy

## Overview

This document details the comprehensive collection of Bihar Board (BSEB) Class 10 Previous Year Question Papers (2011-2025) including sources, collection methodology, and gap analysis.

**Collection Stats:**
- **Total Papers:** 150 PDFs
- **Total Size:** ~440 MB
- **Subjects:** 6 (Mathematics, Science, Social Science, Hindi, English, Sanskrit)
- **Years:** 2011-2025
- **Naming Convention:** `{subject_code}_{year}{sitting}.pdf` (e.g., `math_2025i.pdf`)

---

## Subject Codes

| Subject | Code | Folder |
|---------|------|--------|
| Mathematics | `math` | `mathematics/` |
| Science | `sci` | `science/` |
| Social Science | `soc` | `social_science/` |
| Hindi | `hin` | `hindi/` |
| English | `eng` | `english/` |
| Sanskrit | `san` | `sanskrit/` |

---

## Sources Used

### 1. bsebresult.in (Primary Source)
**URL:** `https://bsebresult.in/bihar-board-matric-question-paper/`

**Papers Collected:** 143 PDFs (initial bulk download)

**Coverage:**
- Years: 2011-2025
- Most comprehensive source with both 1st and 2nd sitting papers
- Direct PDF links + Google Drive links for older papers

**Subjects Available:**
- All 6 subjects with good coverage from 2014 onwards
- Limited Math coverage for 2011-2014

---

### 2. biharboardquestionpaper.com (Secondary Source)
**URL:** `https://biharboardquestionpaper.com/bihar-board-10th-question-paper/`

**Papers Collected:** 4 PDFs (filling gaps)

| Paper | Source URL |
|-------|-----------|
| `math_2023ii.pdf` | Direct link from Math section |
| `math_2022ii.pdf` | Direct link |
| `math_2021ii.pdf` | Direct link |
| `math_2017ii.pdf` | Google Drive link |

---

### 3. bsebstudy.com (Tertiary Source)
**URL:** `https://www.bsebstudy.com/papers/`

**Papers Collected:** 3 PDFs (filling specific gaps)

| Paper | Source File |
|-------|-------------|
| `math_2018ii.pdf` | `bihar-board-class-10-mathematics-210-2018.pdf` |
| `soc_2014i.pdf` | `bihar-board-class-10-social-science-set-1-2014.pdf` |
| `san_2021ii.pdf` | `bihar-board-class-10-sanskrit-set-2-2021.pdf` |

**Note:** Many papers on this site are HTML files, not downloadable PDFs.

---

## Collection Scripts

### 1. `scripts/download_pyqs.py`
**Purpose:** Main bulk downloader from bsebresult.in
**Input:** `pdf_sources.json`
**Features:**
- Handles both direct URLs and Google Drive links
- Automatic retry on timeout
- Progress tracking
- Proper file naming

### 2. `scripts/download_missing.py`
**Purpose:** Download additional Math papers from biharboardquestionpaper.com
**Papers Downloaded:** math_2023ii, math_2022ii, math_2021ii, math_2017ii

### 3. `scripts/download_gaps.py`
**Purpose:** Targeted download of specific missing papers from bsebstudy.com
**Papers Downloaded:** math_2018ii, soc_2014i, san_2021ii

### 4. `scripts/check_missing.py`
**Purpose:** Gap analysis - identifies missing papers from complete collection

---

## Collection Summary by Subject

### Mathematics (20 papers)
```
✅ Have: 2015i, 2016i, 2017i/ii, 2018i/ii, 2019i/ii, 2020i/ii, 
         2021i/ii, 2022i/ii, 2023i/ii, 2024i/ii, 2025i/ii

❌ Missing: 2011i, 2012i, 2013i, 2014i/ii, 2015ii, 2016ii
```

### Science (26 papers)
```
✅ Have: 2011i, 2012i, 2013i, 2014i/ii, 2015i/ii, 2016i/ii, 
         2017i/ii, 2018i/ii, 2019i/ii, 2020i/ii, 2021i/ii, 
         2022i/ii, 2023i, 2024i/ii, 2025i/ii

❌ Missing: 2023ii
```

### Social Science (26 papers)
```
✅ Have: 2011i, 2012i, 2013i, 2014i, 2015i/ii, 2016i/ii, 
         2017i/ii, 2018i/ii, 2019i/ii, 2020i/ii, 2021i/ii, 
         2022i/ii, 2023i, 2024i/ii, 2025i/ii

❌ Missing: 2023ii
```

### Hindi (26 papers)
```
✅ Have: 2011i, 2012i, 2013i, 2014i/ii, 2015i/ii, 2016i/ii, 
         2017i/ii, 2018i/ii, 2019i/ii, 2020i/ii, 2021i/ii, 
         2022i/ii, 2023i, 2024i/ii, 2025i/ii

❌ Missing: 2023ii
```

### English (26 papers)
```
✅ Have: 2011i, 2012i, 2013i, 2014i/ii, 2015i/ii, 2016i/ii, 
         2017i/ii, 2018i/ii, 2019i/ii, 2020i/ii, 2021i/ii, 
         2022i/ii, 2023i, 2024i/ii, 2025i/ii

❌ Missing: 2023ii
```

### Sanskrit (26 papers)
```
✅ Have: 2011i, 2012i, 2013i, 2014i/ii, 2015i/ii, 2016i/ii, 
         2017i/ii, 2018i/ii, 2019i/ii, 2020i/ii, 2021i/ii, 
         2022i/ii, 2023i, 2024i/ii, 2025i/ii

❌ Missing: 2023ii
```

---

## Gap Analysis

### Missing Papers (10 total)

| Paper | Reason |
|-------|--------|
| `math_2011i` | Not digitized - single shift year, no PDF found online |
| `math_2012i` | Not digitized - single shift year, no PDF found online |
| `math_2013i` | Not digitized - single shift year, no PDF found online |
| `math_2014i` | Not digitized anywhere online |
| `math_2014ii` | Not digitized anywhere online |
| `math_2015ii` | PDF not found on any source |
| `math_2016ii` | PDF not found on any source |
| `sci_2023ii` | Only HTML available on bsebstudy.com |
| `soc_2023ii` | Only HTML available on bsebstudy.com |
| `hin_2023ii` | Not found as PDF |
| `eng_2023ii` | Not found as PDF |
| `san_2023ii` | Not found as PDF |

### Historical Context

**2011-2013:** Bihar Board conducted Class 10 exams in **single shift only** (morning session). No 2nd sitting papers exist because they never happened.

**2014 onwards:** Two-shift system introduced:
- 1st Shift: 9:30 AM - 12:45 PM
- 2nd Shift: 2:00 PM - 5:15 PM

---

## Git History

```
commit 1: Initial commit - 143 PDFs from bsebresult.in
commit 2: Add 4 additional Math papers (2023ii, 2022ii, 2021ii, 2017ii)
commit 3: Add 3 missing papers from bsebstudy.com (math_2018ii, soc_2014i, san_2021ii)
```

---

## File Structure

```
bseb10th-pyqs/
├── english/        (26 files)
├── hindi/          (26 files)
├── mathematics/    (20 files)
├── sanskrit/       (26 files)
├── science/        (26 files)
└── social_science/ (26 files)
```

---

## Future Collection Opportunities

1. **2023 2nd sitting papers** - Available as HTML on bsebstudy.com, could be scraped and converted
2. **Math 2011-2014** - May become available if sources digitize old papers
3. **Model papers** - Available on multiple sources but not collected (different from PYQs)

---

## Complete PDF Collection with Source URLs

### Mathematics (20 PDFs)

| File | Source | URL |
|------|--------|-----|
| `math_2015i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1WIlB53g6DBJbtlh6fyhzVUMZ1ONxvdXI/view) |
| `math_2016i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-mathematics-813-2016.pdf) |
| `math_2017i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-mathematics-202-2017.pdf) |
| `math_2017ii.pdf` | biharboardquestionpaper.com (GDrive) | [Download](https://drive.google.com/file/d/1PIl5snlmu3-vTqXLp-anoDzcdH7QV40c/view) |
| `math_2018i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-mathematics-210-2018.pdf) |
| `math_2018ii.pdf` | bsebstudy.com | [Download](https://www.bsebstudy.com/papers/bihar-board-class-10-mathematics-210-2018.pdf) |
| `math_2019i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-mathematics-110-b-2019.pdf) |
| `math_2019ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-mathematics-110-set-c-2019.pdf) |
| `math_2020i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-mathematics-110-g-2020.pdf) |
| `math_2020ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-mathematics-210-g-2020.pdf) |
| `math_2021i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/Bihar-Board-Class-10-Mathematics-Question-Paper-2021.pdf) |
| `math_2021ii.pdf` | biharboardquestionpaper.com | [Download](https://biharboardquestionpaper.com/wp-content/uploads/2025/08/BIHAR-BOARD-CLASS-10-MATHEMATICS-210-SET-C-2021.pdf) |
| `math_2022i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-mathematics-question-paper-2022.pdf) |
| `math_2022ii.pdf` | biharboardquestionpaper.com | [Download](https://biharboardquestionpaper.com/wp-content/uploads/2025/10/BIHAR-BOARD-CLASS-10-MATHEMATICS-210-SET-A-2022-Download.pdf) |
| `math_2023i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-mathematics-question-paper-2023.pdf) |
| `math_2023ii.pdf` | biharboardquestionpaper.com | [Download](https://biharboardquestionpaper.com/wp-content/uploads/2025/10/bihar-board-class-10-mathematics-210-b-2023-download.pdf) |
| `math_2024i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-math-question-paper-2024.pdf) |
| `math_2024ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-math-question-paper-2024-set-e.pdf) |
| `math_2025i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-mathematics-110-set-b-2025.pdf) |
| `math_2025ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-mathematics-210-set-c-2025.pdf) |

---

### Science (26 PDFs)

| File | Source | URL |
|------|--------|-----|
| `sci_2011i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/16jS8_uZYY5bN77jlJ0PPw9dSw4W2SVyo/view) |
| `sci_2012i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1FapNY4UjpjI16TVoDVmi_mLn95JZwNH8/view) |
| `sci_2013i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1b2ZvawWV6mAlsQQBpx41jK9TxMh-a08J/view) |
| `sci_2014i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1iYcoR-q2xNuXmgaoIc2UWggcLu1-ePhs/view) |
| `sci_2014ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1YNMZcrfSIZU3603WbzuYXbNNIMaDkrw0/view) |
| `sci_2015i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1io8zk1jr4l6h_6249D1CEMVxAbikTfat/view) |
| `sci_2015ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1_ZE05GEOE2jpuNCf6QeADPxRcz71mCU6/view) |
| `sci_2016i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-science-811-2016.pdf) |
| `sci_2016ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1KeemAIODzuWsL4PzFf-hDPdpYPKoPJ4H/view) |
| `sci_2017i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-science-204-2017.pdf) |
| `sci_2017ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1wWDUfxP5pNCNsMMIa6sOzkemHaUaLrvx/view) |
| `sci_2018i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-science-112-2018.pdf) |
| `sci_2018ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-science-212-2018.pdf.pdf) |
| `sci_2019i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-science-112-set-1-2019.pdf) |
| `sci_2019ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-science-212-d-2019-1.pdf) |
| `sci_2020i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-science-112-j-2020.pdf) |
| `sci_2020ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-science-212-c-2020.pdf) |
| `sci_2021i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1Tk8vhPCyr5uGG6mcz4UjSzQTfWhdq3_q/view) |
| `sci_2021ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1odLV6T5REYPUl4UByVIKJx1tALC6Gnz3/view) |
| `sci_2022i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-science-question-paper-2022.pdf) |
| `sci_2022ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1WssB7u7klIuiRpUom7ep9B51FX8W9xTg/view) |
| `sci_2023i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-science-question-paper-2023.pdf) |
| `sci_2024i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-science-question-paper-2024.pdf) |
| `sci_2024ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-science-question-paper-2024-2nd-sitting.pdf) |
| `sci_2025i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-science-112-set-d-2025.pdf) |
| `sci_2025ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-science-212-set-f-2025.pdf) |

---

### Social Science (26 PDFs)

| File | Source | URL |
|------|--------|-----|
| `soc_2011i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1uJs7ie84nJEtjwOj-1Zsge4CmAxm6-4X/view) |
| `soc_2012i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1S1_xMx55JBJ_RCz9PvgewseZl9gFhCPw/view) |
| `soc_2013i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1s9S6jYMduj0AnUBoX4M2PzbQy7lBliNv/view) |
| `soc_2014i.pdf` | bsebstudy.com | [Download](https://www.bsebstudy.com/papers/bihar-board-class-10-social-science-set-1-2014.pdf) |
| `soc_2014ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/12bKomDDaHdzIOVOcBhCrDKZu7nzbIPWk/view) |
| `soc_2015i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1eiH7x1_fbZEIEGmIlJkJRhK5I1KtwSNo/view) |
| `soc_2015ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1j8SMqvY4_6dfm_zQ3JrSTttd-qsg1ZPU/view) |
| `soc_2016i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-social-science-812-2016.pdf) |
| `soc_2016ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1ZhprJXu8aAS5BFexqMgiB3cdX4MpDUEy/view) |
| `soc_2017i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-social-science-203-2017.pdf) |
| `soc_2017ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1fT0F45nP2nQYpQKgyWwdKL6y1WXvkTxE/view) |
| `soc_2018i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/18UeNFkelderzA462OAIcX1M15SNRKeHs/view) |
| `soc_2018ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-social-science-211-2018.pdf) |
| `soc_2019i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-social-science-111-e-2019.pdf) |
| `soc_2019ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-social-science-211-a-2019.pdf) |
| `soc_2020i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-social-science-111-h-2020.pdf) |
| `soc_2020ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-social-science-211-c-2020.pdf) |
| `soc_2021i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1c9bFJQ47kL_MFi5tqmxEIiJtM-JX8ivD/view) |
| `soc_2021ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1RiTjLYnBbSQLdKwi5_d8B_ovvwFg6MCG/view) |
| `soc_2022i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10-social-science-question-paper-2022.pdf) |
| `soc_2022ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/10lqtkiI5VVEZe9TnzU7wwv1jS3_Kclty/view) |
| `soc_2023i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-social-science-question-paper-2023.pdf) |
| `soc_2024i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-social-science-question-paper-2024.pdf) |
| `soc_2024ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-social-science-question-paper-2024-2nd-shift.pdf) |
| `soc_2025i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-social-science-111-set-b-2025.pdf) |
| `soc_2025ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-social-science-111-set-e-2025.pdf) |

---

### Hindi (26 PDFs)

| File | Source | URL |
|------|--------|-----|
| `hin_2011i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1-oWzuZOlO0ATCi1oZl5VApkiKdiZzLWx/view) |
| `hin_2012i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/17GBPnAW0o1zvOeAR4FeSDdvuBfMTTBfR/view) |
| `hin_2013i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1RVwwXgo_UGDX3XRS-04hPfD8u_t72icL/view) |
| `hin_2014i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1O_MYrAdxC8ktIiqiQNuY7mZi_IFk6B6Y/view) |
| `hin_2014ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/13VE3ltH3GvmA1f-nu1aet1x5OXVE61Tx/view) |
| `hin_2015i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1HrOpvB3Ua7qN_NneA-XhxlKTlnVIeADk/view) |
| `hin_2015ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1H408ypeB3t4SoKyxEe6AnaUmAi4OBc7v/view) |
| `hin_2016i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-hindi-801-2016.pdf) |
| `hin_2016ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1wEceBzGRKRSV142JX5UaKXTZ8DLPbRh8/view) |
| `hin_2017i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-hindi-211-2017.pdf) |
| `hin_2017ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1s8vwkPBGPkhCp3dRyGkCljxpVGm4xFYV/view) |
| `hin_2018i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/14vcDBEDjs-MNxnlmZO2e4WCY0uqOdgOg/view) |
| `hin_2018ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-hindi-nlh-206-2018.pdf) |
| `hin_2019i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-hindi-101-b-2019-1.pdf) |
| `hin_2019ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-nlh-hindi-sil-106-set-a-2019.pdf) |
| `hin_2020i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-hindi-101-f-2020.pdf) |
| `hin_2020ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-hindi-201-d-2020.pdf) |
| `hin_2021i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1i0_6M0psff4cUt8meyGZI7ZXHEhJp4AZ/view) |
| `hin_2021ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1jlmcxz6-9qkYDZMAtwaZ78sh6Di8bhZk/view) |
| `hin_2022i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-hindi-mt-101-set-b-2022.pdf) |
| `hin_2022ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-hindi-mt-201-c-2022.pdf) |
| `hin_2023i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-hindi-question-paper-2023.pdf) |
| `hin_2024i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-hindi-mt-question-paper-2024.pdf) |
| `hin_2024ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-hindi-question-paper-2024-2nd-shift.pdf) |
| `hin_2025i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-hindi-mt-101-set-h-2025.pdf) |
| `hin_2025ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-hindi-mt-201-set-c-2025.pdf) |

---

### English (26 PDFs)

| File | Source | URL |
|------|--------|-----|
| `eng_2011i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1OakP_G221mcNa1NK6QWYqP4bLNceBaYa/view) |
| `eng_2012i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/16-cEVQoqhE7no46jMn9Vh_VWz3vSFkFT/view) |
| `eng_2013i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1Q-0RHrc4TJyuMKJ73MktVkmUF_9qIoYY/view) |
| `eng_2014i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1Upn6vKODNSZ8CxWk5j8HcpIExbGAVYov/view) |
| `eng_2014ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1jQvNQxYmyWekWJAqtPJNRmWx5HRhjTNP/view) |
| `eng_2015i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1HbFsjpLcMNmVql6IcCv3xwYidysr1pPg/view) |
| `eng_2015ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1HyepO4FxVAMBSiPlWVJA_qyMP3-llKJq/view) |
| `eng_2016i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-english-compulsory-810-2016.pdf) |
| `eng_2016ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1dCl_nKhvzFUrkpMkYXwslb_JtKHzrnZi/view) |
| `eng_2017i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-english-201-2017.pdf) |
| `eng_2017ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1b56RPkoo1Uvr862QR99VHj7w69YfznKx/view) |
| `eng_2018i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1AKBBMOtcFhDZhjchLzwhOtvvWDV4w8xD/view) |
| `eng_2018ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-english-213-2018.pdf) |
| `eng_2019i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-english-113-f-2019-1.pdf) |
| `eng_2019ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-english-213-g-2019.pdf) |
| `eng_2020i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1IhVP13GgzrCyq1uoKBmOJ6GEsIHpRXLZ/view) |
| `eng_2020ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-english-213-d-2020.pdf) |
| `eng_2021i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1DMhD8Frw8oNCMYhcWfpGrxuGD1t7clzK/view) |
| `eng_2021ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1THGJGzOHpqPv9BPcJl5oOpGDV17tujJZ/view) |
| `eng_2022i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10th-english-question-paper-first-sitting-2022.pdf) |
| `eng_2022ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10th-english-question-paper-second-sitting-2022.pdf) |
| `eng_2023i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-english-question-paper-2023.pdf) |
| `eng_2024i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-english-question-paper-2024.pdf) |
| `eng_2024ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-english-question-paper-2024-set-e.pdf) |
| `eng_2025i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-english-113-set-g-2025.pdf) |
| `eng_2025ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-english-113-set-j-2025.pdf) |

---

### Sanskrit (26 PDFs)

| File | Source | URL |
|------|--------|-----|
| `san_2011i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1ESafrUd4xDh1hhsqJwq8Du8le7b84o7y/view) |
| `san_2012i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1ShayxiKZiVway2WANNH3jMNQTotrjTAC/view) |
| `san_2013i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1KoXMyMLCaWzHYmIq1dnAg11HSU-0jaDY/view) |
| `san_2014i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1dfy_l0A1lDNOvtXWRx5mAr3kczncTKvm/view) |
| `san_2014ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1c2yvH0Xxbv8CLBepBTjNodCbcPi-wz4L/view) |
| `san_2015i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1lHEB_jo9YYaBX2phntK_fUOblSLCuajJ/view) |
| `san_2015ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1FnEt2U78TCmNBvntEh8fvz5QydIqPcKg/view) |
| `san_2016i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1R5zQzNR0Y22US62m0ols5KAD6Hsn9SIr/view) |
| `san_2016ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/13tuFfKIP_BE_tKsOfdUjQIWGoQClUUi8/view) |
| `san_2017i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1q5UFE1IBdL1-bklayfTM-cBeYauFDB1z/view) |
| `san_2017ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1idAX5uYMU3mOBl1RECCBXxGfVhfDsA_j/view) |
| `san_2018i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-sanskrit-set-1-2018.pdf) |
| `san_2018ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1gdOBtpYp0VUdkoRl8QTcA3jvJr8Sn7TY/view) |
| `san_2019i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-english-113-f-2019-1.pdf) |
| `san_2019ii.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1exPd5Sfl6LgdDzJd3s3OUuKZYqO6j9ZZ/view) |
| `san_2020i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-sanskrit-105-I-2020.pdf) |
| `san_2020ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-sanskrit-205-b-2020.pdf) |
| `san_2021i.pdf` | bsebresult.in (GDrive) | [Download](https://drive.google.com/file/d/1z0IbggLPIafh9cFDXkOtXmdqkaq6ecNF/view) |
| `san_2021ii.pdf` | bsebstudy.com | [Download](https://www.bsebstudy.com/papers/bihar-board-class-10-sanskrit-set-2-2021.pdf) |
| `san_2022i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-sanskrit-1st-shift-2022.pdf) |
| `san_2022ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-class-10-sanskrit-2nd-shift-2022.pdf) |
| `san_2023i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-sanskrit-question-paper-2023.pdf) |
| `san_2024i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-sanskrit-question-paper-2024.pdf) |
| `san_2024ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2024/12/bihar-board-10th-205-sanskrit-question-paper-2024.pdf) |
| `san_2025i.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-sanskrit-sil-105-set-b-2025.pdf) |
| `san_2025ii.pdf` | bsebresult.in | [Download](https://bsebresult.in/wp-content/uploads/2025/02/bihar-board-class-10-sanskrit-sil-105-set-h-2025.pdf) |

---

## Missing Papers Summary

| Paper | Status | Notes |
|-------|--------|-------|
| `math_2011i` | ❌ Not Available | Single-shift year, Math not digitized |
| `math_2012i` | ❌ Not Available | Single-shift year, Math not digitized |
| `math_2013i` | ❌ Not Available | Single-shift year, Math not digitized |
| `math_2014i` | ❌ Not Available | Not found on any source |
| `math_2014ii` | ❌ Not Available | Not found on any source |
| `math_2015ii` | ❌ Not Available | PDF not found online |
| `math_2016ii` | ❌ Not Available | PDF not found online |
| `sci_2023ii` | ❌ Not Available | Only HTML on bsebstudy.com |
| `soc_2023ii` | ❌ Not Available | Only HTML on bsebstudy.com |
| `hin_2023ii` | ❌ Not Available | PDF not found |
| `eng_2023ii` | ❌ Not Available | PDF not found |
| `san_2023ii` | ❌ Not Available | PDF not found |

---

*Document created: 2026-02-03*
*Last updated: 2026-02-03*
