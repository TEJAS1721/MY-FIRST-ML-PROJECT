import pandas as pd
import streamlit as st
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Page Configuration
st.set_page_config(page_title="Sentiment Classifier", page_icon="🤖")
st.title("🤖 Live AI Sentiment Classifier")
st.write("Type any review or statement below to test the trained machine learning model in real time.")

# Train Model (Cached to run only once)
@st.cache_resource
def train_sentiment_model():
    data = {
        "text": [
            "I love this product, it works amazingly well!",
            "Fantastic experience, highly recommend to everyone.",
            "Great quality and super fast delivery.",
            "Terrible quality, broke on the very first day.",
            "Worst purchase ever. Absolutely useless waste of money.",
            "Horrible customer service, very disappointed."
        ],
        "sentiment": ["Positive", "Positive", "Positive", "Negative", "Negative", "Negative"]
    }
    df = pd.DataFrame(data)
    
    pipeline = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('classifier', LogisticRegression())
    ])
    pipeline.fit(df['text'], df['sentiment'])
    return pipeline

model = train_sentiment_model()

# User Input Field
user_input = st.text_input("Enter text to analyze:", value="This product is fantastic!")

# Prediction Action
if st.button("Predict Sentiment"):
    if user_input.strip():
        prediction = model.predict([user_input])[0]
        if prediction == "Positive":
            st.success(f"**Predicted Sentiment:** {prediction} 😄")
        else:
            st.error(f"**Predicted Sentiment:** {prediction} 😞")
    else:
        st.warning("Please enter some text before analyzing.")
