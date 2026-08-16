import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# 1. Training Dataset (Text + Labels)
data = {
    "text": [
        "I love this product, it works amazingly well!",
        "Fantastic experience, highly recommend to everyone.",
        "Terrible quality, broke on the very first day.",
        "Worst purchase ever. Absolutely useless and waste of money.",
        "Decent value for the price, satisfied overall.",
        "Horrible customer service and slow delivery."
    ],
    "sentiment": ["positive", "positive", "negative", "negative", "positive", "negative"]
}

df = pd.DataFrame(data)

# 2. Create Machine Learning Pipeline (TF-IDF Vectorizer + Logistic Regression)
model_pipeline = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

# 3. Train the Model
model_pipeline.fit(df['text'], df['sentiment'])

# 4. Test Model on New, Unseen Text
new_sentences = [
    "The item arrived fast and works great!",
    "Extremely disappointed with the cheap material."
]

predictions = model_pipeline.predict(new_sentences)

# 5. Output Results
print("--- Machine Learning Sentiment Classifier Results ---")
for text, label in zip(new_sentences, predictions):
    print(f"Text: '{text}' --> Predicted Sentiment: {label.upper()}")
