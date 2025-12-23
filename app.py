# -*- coding: utf-8 -*-
"""
Created on Tue Dec 23 16:22:51 2025

@author: GITAA029
"""

import streamlit as st
import pickle

# Load the trained model
with open("best_model.pkl", "rb") as f:
    model = pickle.load(f)

# Prediction function
def predict_spam_ham(sentence):
    prediction = model.predict([sentence])[0]
    return prediction

# Streamlit UI
st.set_page_config(page_title="Spam Detection App", page_icon="📩")

st.title("📩 Spam Message Detection")
st.write("Enter a message below to check whether it is **Spam** or **Ham**.")

# Text input
user_input = st.text_area("Enter your message here:")

# Predict button
if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message.")
    else:
        result = predict_spam_ham(user_input)

        if result.lower() == "spam":
            st.error("🚨 This message is **SPAM**")
        else:
            st.success("✅ This message is **HAM (Not Spam)**")
