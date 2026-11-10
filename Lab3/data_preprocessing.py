
# Lab 3: Data Preprocessing and EDA

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split

# Create output folder
os.makedirs("Lab3/outputs", exist_ok=True)

# 1. NumPy operations
numbers = np.array([10, 20, 30, 40, 50])

print("NUMPY OPERATIONS")
print("Array:", numbers)
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

# 2. Load dataset
df = pd.read_csv("datasets/student_placement.csv")

print("\nORIGINAL DATASET")
print(df.head())

print("\nDATASET INFORMATION")
print(df.info())

# 3. Exploratory Data Analysis (EDA)
print("\nDATASET SHAPE:", df.shape)

print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nMISSING VALUES")
print(df.isnull().sum())

print("\nPLACEMENT COUNT")
print(df["Placement"].value_counts())

# 4. Data visualization
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Placement")
plt.title("Student Placement Distribution")
plt.savefig("Lab3/outputs/placement_distribution.png")
plt.close()

plt.figure(figsize=(6, 4))
sns.histplot(df["CGPA"], bins=6, kde=True)
plt.title("CGPA Distribution")
plt.savefig("Lab3/outputs/cgpa_distribution.png")
plt.close()

# 5. Handle missing values
df["CGPA"] = df["CGPA"].fillna(df["CGPA"].median())
df["Internships"] = df["Internships"].fillna(
    df["Internships"].median()
)

df["Gender"] = df["Gender"].fillna(df["Gender"].mode()[0])
df["Course"] = df["Course"].fillna(df["Course"].mode()[0])

print("\nMISSING VALUES AFTER CLEANING")
print(df.isnull().sum())

# 6. Remove unnecessary column
df = df.drop("Student_ID", axis=1)

# 7. Label Encoding
encoder = LabelEncoder()

for column in ["Gender", "Course", "Placement"]:
    df[column] = encoder.fit_transform(df[column])

print("\nENCODED DATA")
print(df.head())

# 8. Feature selection
X = df.drop("Placement", axis=1)
y = df["Placement"]

selector = SelectKBest(score_func=chi2, k=3)
X_selected = selector.fit_transform(X, y)

selected_features = X.columns[selector.get_support()]

print("\nSELECTED FEATURES")
print(list(selected_features))

# 9. Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X_selected,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print("\nTRAINING DATA SHAPE:", X_train.shape)
print("TESTING DATA SHAPE:", X_test.shape)

# 10. Save cleaned dataset
df.to_csv("Lab3/outputs/cleaned_dataset.csv", index=False)

print("\nCleaned dataset saved successfully!")
print("All Lab 3 operations completed.")
