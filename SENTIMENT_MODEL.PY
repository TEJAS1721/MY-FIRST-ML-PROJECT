# Simple Sentiment Classifier

# Text input to analyze
sample_text = "I love learning artificial intelligence!"

# Key word lists
positive_words = ["love", "great", "awesome", "fantastic", "good"]
negative_words = ["hate", "bad", "terrible", "awful", "worst"]

#process text
words = sample_text.lower().split()

#  Predict sentiment
if any(word in positive_words for word in words):
    print(f"Text: '{sample_text}'")
    print("Result: Positive Sentiment")
elif any(word in negative_words for word in words):
    print(f"Text: '{sample_text}'")
    print("Result: Negative Sentiment")
else:
    print(f"Text: '{sample_text}'")
    print("Result: Neutral Sentiment")
