import streamlit as st
from textblob import TextBlob
from newspaper import Article

def analyze_article(url):
    try:
        article = Article(url)
        article.download()
        article.parse()
        
        text = article.text
        
        blob = TextBlob(text)
        sentiment = blob.sentiment  
        
        return text, sentiment.polarity, sentiment.subjectivity
    except Exception as e:
        return None, None, None

# Streamlit 
st.title("Text Sentiment Analyzer")

url = st.text_input("Enter Article URL", "")

if st.button("Analyze"):
    if url:
        text, polarity, subjectivity = analyze_article(url)
        
        if text:
            st.subheader("Sentiment Analysis Results:")
            st.write(f"**Polarity:** {polarity:.2f}  (-1 = Negative, 1 = Positive)")
            st.write(f"**Subjectivity:** {subjectivity:.2f}  (0 = Objective, 1 = Subjective)")
            
            st.subheader("Extracted Article Text:")
            st.write(text[:1000] + "...")  # Limit display length
        else:
            st.error("Failed to fetch or analyze the article. Please check the URL.")
    else:
        st.warning("Please enter a valid URL.")
