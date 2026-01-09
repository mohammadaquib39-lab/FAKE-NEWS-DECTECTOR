# app.py

import streamlit as st
import joblib

# Load saved model and vectorizer
model = joblib.load("model/fake_news_model.joblib")
vectorizer = joblib.load("model/tfidf_vectorizer.joblib")

# App layout
st.set_page_config(page_title="📰 Fake News Detector", layout="centered")
st.title("📰 Fake News Detector")
st.markdown("Enter a news article below to classify it as **Fake** or **Real**.")

# User input
news_text = st.text_area("📝 Paste a news article:", height=250)

# Predict button
if st.button("🔍 Detect"):
    if news_text.strip() == "":
        st.warning("Please enter some text to analyze.")
    else:
        text_vector = vectorizer.transform([news_text])
        prediction = model.predict(text_vector)[0]

        if prediction == 1:
            st.error("🚨 This news is likely **FAKE**.")
        else:
            st.success("✅ This news appears to be **REAL**.")

