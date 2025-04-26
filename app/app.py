import streamlit as st
import pandas as pd
import numpy as np
import joblib
import requests
from streamlit_lottie import st_lottie

# Function to load Lottie Animation
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load Animation
lottie_stock = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")  # Animation Link

# Page config
st.set_page_config(page_title="Tesla Stock Predictor 🚗", page_icon="🚗", layout="centered")

# Main Title
st.title("🚗 Tesla Stock Close Price Predictor")
st.subheader("Welcome to a Smarter Stock Forecasting App 📈✨")

# Animation Section
st_lottie(lottie_stock, height=300, key="stock")

st.markdown("---")

# Sidebar
st.sidebar.header("Input Stock Features:")

open_price = st.sidebar.number_input("Open Price (USD)", min_value=0.0, step=0.1)
high_price = st.sidebar.number_input("High Price (USD)", min_value=0.0, step=0.1)
low_price = st.sidebar.number_input("Low Price (USD)", min_value=0.0, step=0.1)
volume = st.sidebar.number_input("Volume", min_value=0)
daily_change = st.sidebar.number_input("Daily % Change", step=0.1)
ma7 = st.sidebar.number_input("7-Day Moving Average", min_value=0.0, step=0.1)
ma30 = st.sidebar.number_input("30-Day Moving Average", min_value=0.0, step=0.1)
high_low_diff = st.sidebar.number_input("High-Low Difference", min_value=0.0, step=0.1)

# Load the model
model = joblib.load("./models/linear_model.pkl")

# Prediction Button
if st.sidebar.button("Predict Close Price"):
    input_data = np.array([[open_price, high_price, low_price, volume, daily_change, ma7, ma30, high_low_diff]])
    prediction = model.predict(input_data)[0]
    st.success(f"📈 Predicted Close Price: **${prediction:.2f}**")
    
st.markdown("---")
st.caption("Made  by Mariam Maysara")
st.caption("Data Science & Machine Learning Enthusiast")