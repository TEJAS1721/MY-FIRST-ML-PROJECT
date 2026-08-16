# My First ML Project: Sentiment Classifier

A beginner-friendly Natural Language Processing (NLP) pipeline written in Python that analyzes text and classifies its sentiment as **Positive**, **Negative**, or **Neutral**.

## 🚀 Project Overview
- **Language:** Python
- **Topic:** Natural Language Processing (NLP) / Sentiment Analysis
- **Status:** Completed

## 📄 Repository Files
- `sentiment_model.py`: The core script with text processing logic and rule-based sentiment classification.
- `README.md`: Project documentation.

## 🧠 What I Learned
- Structuring a basic Python ML script.
- Version control and repository setup on GitHub

# 🤖 Real-Time AI Sentiment Classifier

An interactive Natural Language Processing (NLP) web application built with Python, NLTK, and Streamlit that predicts text sentiment in real time.

## 🚀 Live App
[Click here to test the live app](https://my-first-ml-project-dhydncqjqysbpk3bsh5qxi.streamlit.app/)

## 💡 What I Built & Key Learnings
- **Pre-trained NLP Lexicon:** Upgraded from a baseline prototype to NLTK's VADER model (9,000+ words) to handle Out-of-Vocabulary (OOV) words, negations, and context.
- **Resource Optimization:** Used Streamlit's `@st.cache_resource` decorator to load the model into memory once, preventing redundant re-downloads on user interactions.
- **Continuous Deployment:** Integrated GitHub directly with Streamlit Community Cloud for automated CI/CD builds on every push.

## 🛠️ Tech Stack
- **Language:** Python 3.14
- **NLP Library:** NLTK (VADER Sentiment Intensity Analyzer)
- **UI & Cloud:** Streamlit & Streamlit Cloud
