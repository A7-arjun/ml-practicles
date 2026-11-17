#python -m pip install numpy pandas matplotlib scikit-learn xgboost "gymnasium[toy-text]"

import pandas as pd  #text,tabular,csv data
from sklearn.feature_extraction.text import CountVectorizer #text--> numerical values
from sklearn.naive_bayes import MultinomialNB  #to create navive baies model

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

# Step 2: Converting ditonary --> tables
df = pd.DataFrame(data)

# Step 3: Separate input(x) and output(y)
X = df['message']
y = df['label']

# Step 4: Convert text into numerical values (comp dont unerstand words)
vectorizer = CountVectorizer() #count unique words in give numbers.
X = vectorizer.fit_transform(X)  #training and converting words to numbers

# Step 5: Create Naive Bayes model
model = MultinomialNB()

# Step 6: Train the model
model.fit(X, y)

# Step 7: Test with new message
new_message = ["virat kohli is cricketer"]
new_counts = vectorizer.transform(new_message) #converting msg text to numerical form

prediction = model.predict(new_counts)

print("Prediction:", prediction[0])
