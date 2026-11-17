#python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"

import pandas as pd #handles dataset
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import OneHotEncoder #text --> numbers
from sklearn.pipeline import make_pipeline #combines preprocessing and model
from sklearn.ensemble import RandomForestClassifier #creates random forest model
from sklearn.metrics import accuracy_score, confusion_matrix 
from sklearn.metrics import classification_report #precision recall and f1 score

#DEFINING column names
columns = ["buying", "maint", "doors", "persons",
           "lug_boot", "safety", "class"]

#read the dataset
df = pd.read_csv("car_evaluation.csv", header=None, names=columns) #csv not containg column names assign ours

X = df.drop(columns="class") #input column except class
y = df["class"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y) #maintain class proportions

model = make_pipeline(
    OneHotEncoder(handle_unknown="ignore"), #text --> numbers low-0,high-1 like
    RandomForestClassifier(n_estimators=100, random_state=42)) #create model of 100 d.trees

model.fit(X_train, y_train)

y_pred = model.predict(X_test) #predict class using trained data

print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion matrix:\n", confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, zero_division=0))
