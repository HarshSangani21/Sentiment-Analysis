from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import cleantext
import streamlit as st


st.title("User Input Analysis")
analyzer = SentimentIntensityAnalyzer()

st.subheader("Analyze Your Own Text")

def classify_sentiment(score):
    if score > 0.8:
        return "Highly Positive"
    elif score > 0.4:
        return "Positive"
    elif -0.4 <= score <= 0.4:
        return "Neutral"
    elif score > -0.8:
        return "Negative"
    else:
        return "Highly Negative"

user_input = st.text_area("Enter customer feedback:")
if user_input:
    blob = TextBlob(user_input)
    user_sentiment_score = analyzer.polarity_scores(user_input)["compound"]
    user_sentiment_class = classify_sentiment(user_sentiment_score)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**VADER Sentiment Analysis:**")
        st.write(f"Sentiment Class: {user_sentiment_class}")
        st.write(f"Sentiment Score: {user_sentiment_score:.2f}")
    
    with col2:
        st.write("**TextBlob Analysis:**")
        st.write(f"Polarity: {blob.sentiment.polarity:.2f}")
        st.write(f"Subjectivity: {blob.sentiment.subjectivity:.2f}")

    st.subheader("Cleaned Text")
    cleaned_text = cleantext.clean(user_input, clean_all=False, extra_spaces=True, 
                                stopwords=True, lowercase=True, numbers=True, punct=True)
    st.write(cleaned_text)
else:
    st.write("Please enter some text to analyze.")

