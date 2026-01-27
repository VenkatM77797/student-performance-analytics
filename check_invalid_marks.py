import pandas as pd

# -------------------------------
# Part 1: Load the dataset
# -------------------------------
data = pd.read_csv("StudentsPerformance.csv")

# -------------------------------
# Part 2: Data Validation
# Check for invalid scores (<0 or >100)
# -------------------------------
invalid_rows = data[
    (data["math score"] < 0) | (data["math score"] > 100) |
    (data["reading score"] < 0) | (data["reading score"] > 100) |
    (data["writing score"] < 0) | (data["writing score"] > 100)
]

print("Invalid rows count:", len(invalid_rows))
print(invalid_rows.head())

# -------------------------------
# Part 3: Data Analysis
# Calculate average scores
# -------------------------------
avg_math = data["math score"].mean()
avg_reading = data["reading score"].mean()
avg_writing = data["writing score"].mean()

print("Average Math Score:", avg_math)
print("Average Reading Score:", avg_reading)
print("Average Writing Score:", avg_writing)

# -------------------------------
# Part 4: Pass / Fail Analysis
# -------------------------------
passed_math = data[data["math score"] >= 40].shape[0]
failed_math = data[data["math score"] < 40].shape[0]

print("Students passed math:", passed_math)
print("Students failed math:", failed_math)
