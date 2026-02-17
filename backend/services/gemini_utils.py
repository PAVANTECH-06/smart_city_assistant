import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("❌ GEMINI_API_KEY is not set in .env")

# Configure Gemini
genai.configure(api_key=GEMINI_API_KEY)

# Initialize model ONCE
model = genai.GenerativeModel("models/gemini-flash-latest")


def summarize_text(text: str) -> str:
    try:
        response = model.generate_content(
            f"Summarize the following policy:\n{text}"
        )
        return response.text if response and hasattr(response, "text") else "No summary generated."
    except Exception as e:
        return f"Gemini error: {str(e)}"


def gentip(keyword: str) -> str:
    try:
        response = model.generate_content(
            f"Give 5 eco-friendly tips related to {keyword}."
        )
        return response.text if response and hasattr(response, "text") else "No tips generated."
    except Exception as e:
        return f"Gemini error: {str(e)}"


def answer_q(prompt: str) -> str:
    try:
        response = model.generate_content(prompt)
        return response.text if response and hasattr(response, "text") else "No answer generated."
    except Exception as e:
        return f"Gemini error: {str(e)}"


def forecast_kpi_description(summary: str) -> str:
    prompt = f"Based on this KPI data summary, predict the future trend:\n\n{summary}"
    response = model.generate_content(prompt)
    return response.text.strip()

def detect_anomalies_description(summary: str) -> str:
    prompt = f"Find anomalies in this KPI data:\n\n{summary}"
    response = model.generate_content(prompt)
    return response.text.strip()
