#python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
df = pd.read_csv("emails.csv")

# Step 2: Separate input and output
X = df.iloc[:, 1:-1]
y = df.iloc[:, -1]

# Step 3: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Step 4: Create SVM model
model = SVC(kernel="linear", C=1.0)

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Predict results
y_pred = model.predict(X_test)

# Step 7: Display results
print("Actual:", y_test.values)
print("Predicted:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred))
