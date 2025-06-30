import google.generativeai as genai
import os

# ✅ Configure Gemini
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

# ✅ Generate Eco Tips
def gentip(keyword: str) -> str:
    prompt = f"Give one practical eco-friendly tip related to: {keyword}"
    response = model.generate_content(prompt)
    return response.text.strip()

# ✅ Answer General Query
def answer_q(query: str) -> str:
    prompt = f"Answer this question concisely: {query}"
    response = model.generate_content(prompt)
    return response.text.strip()

# ✅ Summarize Text
def summarize_text(text: str) -> str:
    prompt = f"Summarize the following policy/document:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text.strip()

# ✅ Forecast KPI (based on natural language)
def forecast_kpi_description(kpi_csv_summary: str) -> str:
    prompt = f"Given this KPI trend summary, predict the next logical value or trend:\n\n{kpi_csv_summary}"
    response = model.generate_content(prompt)
    return response.text.strip()

# ✅ Detect Anomalies Description
def detect_anomalies_description(kpi_csv_summary: str) -> str:
    prompt = f"Analyze the following KPI data and highlight any potential anomalies:\n\n{kpi_csv_summary}"
    response = model.generate_content(prompt)
    return response.text.strip()
