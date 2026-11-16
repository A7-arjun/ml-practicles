#python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"

# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Import boosting and voting algorithms
from sklearn.ensemble import (
    AdaBoostClassifier,
    GradientBoostingClassifier,
    VotingClassifier
)

# Import XGBoost algorithm
from xgboost import XGBClassifier

# Import evaluation metrics
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# Load the built-in Iris dataset
X, y = load_iris(return_X_y=True)

# Split dataset into 80% training and 20% testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Create three boosting models
estimators = [
    ("Ada", AdaBoostClassifier(n_estimators=50, random_state=42)),

    ("GBM", GradientBoostingClassifier(
        n_estimators=100, random_state=42
    )),

    ("XGB", XGBClassifier(
        n_estimators=100,
        random_state=42,
        eval_metric="mlogloss",
        n_jobs=1
    ))
]

# Store individual models in a dictionary
models = dict(estimators)

# Create Hard Voting Classifier
models["Hard voting"] = VotingClassifier(
    estimators=estimators, voting="hard"
)

# Create Soft Voting Classifier
models["Soft voting"] = VotingClassifier(
    estimators=estimators, voting="soft"
)

# Print output headings
print("Model Accuracy Precision Recall F1")

# Train and evaluate each model
for name, model in models.items():

    # Train the model
    model.fit(X_train, y_train)

    # Predict results using testing data
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Calculate precision
    precision = precision_score(
        y_test, y_pred, average="macro", zero_division=0
    )

    # Calculate recall
    recall = recall_score(
        y_test, y_pred, average="macro", zero_division=0
    )

    # Calculate F1-score
    f1 = f1_score(
        y_test, y_pred, average="macro", zero_division=0
    )

    # Display evaluation results
    print(f"{name:14} {accuracy:.3f}    {precision:.3f}    "
          f"{recall:.3f} {f1:.3f}")
    
return_X_y=True
