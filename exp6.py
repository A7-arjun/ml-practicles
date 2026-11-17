#python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"

# Import required libraries
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

# Import boosting and voting algorithms
from sklearn.ensemble import (
    AdaBoostClassifier, #creates adaboost model (incorrely classified data corrected importance)
    GradientBoostingClassifier, #cretae gradient boosting model ( predict error sequensilly and fix them)
    VotingClassifier #combines both model
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

# Create three boosting models and stored in list
estimators = [
    ("Ada", AdaBoostClassifier(n_estimators=50, random_state=42)),

    ("GBM", GradientBoostingClassifier(
        n_estimators=100, random_state=42
    )),

    ("XGB", XGBClassifier(
        n_estimators=100,
        random_state=42,
        eval_metric="mlogloss", #multiclass logless eval matrix
        n_jobs=1 #use one cpu thread
    ))
]

# Store individual models in a dictionary
models = dict(estimators)

# Create Hard Voting Classifier (max vote)
models["Hard voting"] = VotingClassifier(
    estimators=estimators, voting="hard"
)

# Create Soft Voting Classifier (combine probalbilty)
models["Soft voting"] = VotingClassifier(
    estimators=estimators, voting="soft"
)

# Print output headings
print("Model Accuracy Precision Recall F1")

# Train and evaluate each model takes each model from dict
for name, model in models.items():

    # Train the model
    model.fit(X_train, y_train)

    # Predict results using testing data
    y_pred = model.predict(X_test)

    # Calculate accuracy
    accuracy = accuracy_score(y_test, y_pred)

    # Calculate precision
    precision = precision_score(                         #avrges metric of 3 metrics
        y_test, y_pred, average="macro", zero_division=0 #avoid error if class has no predicted samples
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
