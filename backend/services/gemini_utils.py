import google.generativeai as genai
import os

# Load API key from .env (recommended)
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel('gemini-1.5-flash')

def gentip(keyword: str) -> str:
    prompt = f"Give one practical eco-friendly tip related to: {keyword}"
    response = model.generate_content(prompt)
    return response.text.strip()

def answer_q(query: str) -> str:
    prompt = f"Answer this question clearly and concisely: {query}"
    response = model.generate_content(prompt)
    return response.text.strip()

def summarize_text(text: str) -> str:
    prompt = f"Summarize the following policy/document:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

def forecast_kpi_description(summary: str) -> str:
    prompt = f"Based on this KPI data summary, predict the future trend:\n\n{summary}"
    response = model.generate_content(prompt)
    return response.text.strip()

def detect_anomalies_description(summary: str) -> str:
    prompt = f"Find anomalies in this KPI data:\n\n{summary}"
    response = model.generate_content(prompt)
    return response.text.strip()
