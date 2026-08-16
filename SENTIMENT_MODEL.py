import streamlit as st
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer

# Page Configuration
st.set_page_config(page_title="AI Sentiment Classifier", page_icon="🤖")
st.title("🤖 Production AI Sentiment Classifier")
st.write("Analyze **any** sentence using a pre-trained Natural Language Processing model.")

# Download pre-trained lexicon once
@st.cache_resource
def load_sentiment_analyzer():
    nltk.download('vader_lexicon')
    return SentimentIntensityAnalyzer()

sia = load_sentiment_analyzer()

# User Input
user_input = st.text_input("Enter text to analyze:", value="This app works surprisingly well!")

if st.button("Predict Sentiment"):
    if user_input.strip():
        # Get sentiment scores
        scores = sia.polarity_scores(user_input)
        compound = scores['compound']
        
        # Display Results
        if compound >= 0.05:
            st.success(f"**Predicted Sentiment:** Positive 😄 (Confidence Score: {compound:.2f})")
        elif compound <= -0.05:
            st.error(f"**Predicted Sentiment:** Negative 😞 (Confidence Score: {compound:.2f})")
        else:
            st.info(f"**Predicted Sentiment:** Neutral 😐 (Confidence Score: {compound:.2f})")
    else:
        st.warning("Please enter some text before analyzing.")
