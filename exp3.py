#python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"

import pandas as pd #manage dataset and manipulation
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC #to create svm model
from sklearn.metrics import accuracy_score 

# Step 1: Load dataset
df = pd.read_csv("emails.csv")

# Step 2: Separate input and output
X = df.iloc[:, 1:-1] #selects rows and columns from thier positions
y = df.iloc[:, -1]

# Step 3: Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y  #maintains class proportions
)

# Step 4: Create SVM model
model = SVC(kernel="linear", C=1.0) #c regulation parameter high c overfitting

# Step 5: Train the model
model.fit(X_train, y_train)

# Step 6: Predict results
y_pred = model.predict(X_test)

# Step 7: Display results
print("Actual:", y_test.values)
print("Predicted:", y_pred)
print("Accuracy:", accuracy_score(y_test, y_pred)) #correct predictions/total predictions
