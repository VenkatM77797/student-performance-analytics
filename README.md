# Student Performance Data Validation and Analysis

## Project Overview
This project analyzes student performance data using Python and pandas.  
It validates assessment scores to ensure data quality and generates basic insights such as subject-wise average scores and pass/fail counts.
cdzvdz
---
## Tech Stack 
![pandas](https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white) ![CSV](https://img.shields.io/badge/CSV-Data%20File-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visualstudiocode&logoColor=white)

---

## 📂 Dataset
The dataset (`StudentsPerformance.csv`) contains student assessment details including:
- Math score
- Reading score
- Writing score
- Demographic/background information (gender, race/ethnicity, parental education, lunch, test preparation)

---

## ✅ Project Features

### 1️⃣ Data Loading
- Loaded student performance data from a CSV file using pandas.

### 2️⃣ Data Validation
- Checked for invalid scores (less than 0 or greater than 100) across math, reading, and writing columns.
- Ensured all assessment scores fall within acceptable ranges before analysis.

### 3️⃣ Data Analysis
- Calculated average Math, Reading, and Writing scores.
- Counted the number of students who passed and failed Math using a pass mark threshold.

---

## 📊 Sample Output
The script prints:
- Invalid rows count (if any invalid scores exist)
- Average Math, Reading, and Writing scores
- Students passed math / failed math counts

---

## ▶️ How to Run the Project

1. Clone the repository:
``` bash
git clone https://github.com/VenkatM77797/student-performance-analytics
```

2. Navigate to the project folder:
``` bash
cd student-performance-analytics
```

3. Install dependencies:
``` bash
python -m pip install pandas
```

4. Run the script:
``` bash
python check_invalid_marks.py
```

👤 Author

Venkat Mandarapu

LinkedIn: https://www.linkedin.com/in/venkat-mandarapu/















