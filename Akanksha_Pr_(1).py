import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the dataset
df = pd.read_csv("C:\\Users\\akank\\Downloads\\archive (8)\\student-scores.csv")

# 2. Quick data check
print("Checking for missing values...")
print(df.isnull().sum())  # Shows count of null values per column

print("\nChecking data types...")
print(df.dtypes)

# 3. Select only subject score columns
subject_cols = [
    'math_score', 'history_score', 'physics_score',
    'chemistry_score', 'biology_score', 'english_score',
    'geography_score'
]

# 4. Total and average marks of each student
df['Total'] = df[subject_cols].sum(axis=1)
df['Average'] = df[subject_cols].mean(axis=1)
df['Average'] = df['Average'].round(2)

# 5. Grade assignment
def assign_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 75:
        return 'B'
    elif avg >= 60:
        return 'C'
    elif avg >= 40:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Average'].apply(assign_grade)

# 6. Class-level analysis
class_average = df['Average'].mean()
topper = df.loc[df['Average'].idxmax()]
topper_name = f"{topper['first_name']} {topper['last_name']}"
topper_score = topper['Average']

print("\nClass Average Marks:", round(class_average, 2))
print("Topper:", topper_name, "with Average:", round(topper_score, 2))

# 7. Display student summary
print("\nSample Student Summary (First 5 students):")
print(df[['id', 'first_name', 'last_name', 'Total', 'Average', 'Grade']].head())

# 8. Bar chart: Subject-wise average
subject_avg = df[subject_cols].mean()
plt.figure(figsize=(10, 5))
subject_avg.plot(kind='bar', color='skyblue')
plt.title('Subject-wise Average Marks')
plt.xlabel('Subjects')
plt.ylabel('Average Marks')
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

# 9. Pie chart: Grade distribution
grade_dist = df['Grade'].value_counts()
print("\nGrade Distribution:\n", grade_dist)
plt.figure(figsize=(6, 6))
plt.pie(grade_dist, labels=grade_dist.index, autopct='%1.1f%%', startangle=90, colors=['gold', 'lightgreen', 'skyblue', 'orange', 'red'])
plt.title('Grade Distribution')
grade_dist = grade_dist.sort_index()
plt.title(f'Grade Distribution (Total Students: {len(df)})')
plt.ylabel('')
plt.tight_layout()
plt.show()

# 10. Save processed results (optional)
df.to_csv('student_summary_output.csv', index=False)

top_3 = df.sort_values(by='Average', ascending=False).head(3)
print("\nTop 3 Performers:\n", top_3[['first_name', 'last_name', 'Average', 'Grade']])

