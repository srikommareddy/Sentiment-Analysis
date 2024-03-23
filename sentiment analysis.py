#!/usr/bin/env python
# coding: utf-8

# In[4]:


#!pip install textblob


# In[3]:


import streamlit as st
from textblob import TextBlob
import logging

# Setup logging
logging.basicConfig(filename='highly_sentimental_words.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def analyze_sentiment(review):
    analysis = TextBlob(review)
    # For simplicity, considering sentiment polarity > 0.5 as highly positive and < -0.5 as highly negative
    if analysis.sentiment.polarity > 0.5:
        logging.info(f"Highly Positive: {review}")
    elif analysis.sentiment.polarity < -0.5:
        logging.info(f"Highly Negative: {review}")
    return analysis.sentiment

st.title('Review Sentiment Analysis')

review = st.text_area("Enter Review:", "Type Here")

if st.button("Analyze"):
    sentiment = analyze_sentiment(review)
    st.write(f"Sentiment Score: {sentiment.polarity}")
    if sentiment.polarity > 0:
        st.markdown("### Positive 😊")
    elif sentiment.polarity < 0:
        st.markdown("### Negative 😠")
    else:
        st.markdown("### Neutral 😐")


# In[ ]:




