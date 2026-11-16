#python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Create dataset
data = {
    'message': [
        'Win a free prize',
        'Claim your free money',
        'Meeting at 5 pm',
        'Project submission tomorrow',
        'Win cash now',
        'Lets go for lunch'
    ],
    'label': [
        'Spam',
        'Spam',
        'Not Spam',
        'Not Spam',
        'Spam',
        'Not Spam'
    ]
}

# Step 2: Convert data into DataFrame
df = pd.DataFrame(data)

# Step 3: Separate input and output
X = df['message']
y = df['label']

# Step 4: Convert text into numerical form
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Step 5: Create Naive Bayes model
model = MultinomialNB()

# Step 6: Train the model
model.fit(X, y)

# Step 7: Test with new message
new_message = ["virat kohli is cricketer"]
new_counts = vectorizer.transform(new_message)

prediction = model.predict(new_counts)

print("Prediction:", prediction[0])
