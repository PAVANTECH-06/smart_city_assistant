import os
import requests
import ssl
from dotenv import load_dotenv

ssl._create_default_https_context = ssl._create_unverified_context

load_dotenv()
WATSONX_API_KEY = os.getenv("WATSONX_API_KEY")
HEADERS = {"Authorization": f"Bearer {WATSONX_API_KEY}"}

# Dummy endpoints for illustration
WATSONX_URL = "https://au-syd.ml.cloud.ibm.com"

def summarize_text(text):
    return f"Summary of: {text[:50]}..."

def generate_eco_tips(keyword):
    return f"Eco tips for {keyword}: Avoid plastic, go solar."

def chat_with_assistant(query):
    return f"AI response for: {query}"

# ----------------------------------------
# 📦 backend/services/ml_utils.py
from sklearn.linear_model import LinearRegression
import numpy as np

def forecast_kpi(df):
    X = np.arange(len(df)).reshape(-1, 1)
    y = df.iloc[:, 1].values
    model = LinearRegression().fit(X, y)
    prediction = model.predict([[len(df)]])
    return prediction.tolist()

def detect_anomalies(df):
    values = df.iloc[:, 1]
    mean, std = values.mean(), values.std()
    threshold = 2
    anomalies = df[abs(values - mean) > threshold * std]
    return anomalies.to_dict(orient="records")