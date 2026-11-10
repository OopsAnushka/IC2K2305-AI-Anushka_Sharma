
import os
import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

# Create output and model folders
os.makedirs("Lab5/outputs", exist_ok=True)
os.makedirs("models", exist_ok=True)

# 1. Load dataset
df = pd.read_csv("datasets/student_placement.csv")

print("Original Dataset:")
print(df.head())

# 2. Handle missing values
df["CGPA"] = df["CGPA"].fillna(df["CGPA"].median())
df["Internships"] = df["Internships"].fillna(
    df["Internships"].median()
)
df["Gender"] = df["Gender"].fillna(
    df["Gender"].mode()[0]
)
df["Course"] = df["Course"].fillna(
    df["Course"].mode()[0]
)

# 3. Separate input features and target
y = df["Placement"].map({"No": 0, "Yes": 1})

X = df.drop(columns=["Student_ID", "Placement"])

# Convert categorical data into numerical columns
X = pd.get_dummies(
    X,
    columns=["Gender", "Course"],
    dtype=int
)

# 4. Split dataset into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

print("\nTraining Records:", len(X_train))
print("Testing Records:", len(X_test))

# 5. Create and train Decision Tree model
model = DecisionTreeClassifier(
    criterion="entropy",
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

# 6. Make predictions
y_pred = model.predict(X_test)

print("\nPredictions:", y_pred)

# 7. Evaluate model
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", round(accuracy * 100, 2), "%")

cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)

report = classification_report(
    y_test,
    y_pred,
    labels=[0, 1],
    target_names=["Not Placed", "Placed"],
    zero_division=0
)

print("\nClassification Report:")
print(report)

# Save classification report
with open(
    "Lab5/outputs/classification_report.txt", "w"
) as file:
    file.write(report)

# 8. Visualize confusion matrix
display = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Not Placed", "Placed"]
)

display.plot(cmap="Blues")
plt.title("Student Placement Confusion Matrix")
plt.savefig("Lab5/outputs/confusion_matrix.png")
plt.show()

# 9. Visualize Decision Tree
plt.figure(figsize=(16, 9))

plot_tree(
    model,
    feature_names=X.columns,
    class_names=["Not Placed", "Placed"],
    filled=True,
    rounded=True
)

plt.title("Decision Tree Classifier")
plt.savefig("Lab5/outputs/decision_tree.png")
plt.show()

# 10. Save trained model
joblib.dump(model, "models/decision_tree.pkl")

print("\nModel saved successfully!")
print("Lab 5 completed.")
