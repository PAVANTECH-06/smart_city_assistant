import streamlit as st
import requests
from googletrans import Translator

st.set_page_config(page_title="Smart City Assistant", layout="centered")

API_URL = "http://localhost:8000"

# -----------------------------
# Translator Setup
# -----------------------------
translator = Translator()

def translate_text(text, target_lang):
    try:
        result = translator.translate(str(text), dest=target_lang)
        return result.text
    except:
        return text


# -----------------------------
# Language Selection
# -----------------------------
language_dict = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te"
}

selected_language = st.selectbox("🌐 Select Language", list(language_dict.keys()))
lang_code = language_dict[selected_language]


# -----------------------------
# Title Section
# -----------------------------
title = "🌱 Sustainable Smart City Assistant"
subtitle = "Empowering cities with AI for smarter, greener living."

st.title(translate_text(title, lang_code))
st.markdown(translate_text(subtitle, lang_code))


# =====================================================
# SIDEBAR MODULE TRANSLATION FIX
# =====================================================

# Internal English Keys
module_dict = {
    "Summarize Policy": "Summarize Policy",
    "Submit Feedback": "Submit Feedback",
    "Forecast KPIs": "Forecast KPIs",
    "Detect Anomalies": "Detect Anomalies",
    "Get Eco Tips": "Get Eco Tips",
    "Ask the Assistant": "Ask the Assistant"
}

# Translate for Display
translated_modules = {
    key: translate_text(value, lang_code)
    for key, value in module_dict.items()
}

selected_translated = st.sidebar.radio(
    translate_text("📊 Choose a Module", lang_code),
    list(translated_modules.values())
)

# Reverse mapping back to English key
reverse_lookup = {v: k for k, v in translated_modules.items()}
option = reverse_lookup[selected_translated]


# =====================================================
# 1️⃣ SUMMARIZE POLICY
# =====================================================
if option == "Summarize Policy":

    st.subheader(translate_text("📄 Summarize a Policy Document", lang_code))
    text = st.text_area(translate_text("Enter full policy or document content", lang_code))

    if st.button(translate_text("Summarize", lang_code)):

        if not text.strip():
            st.warning(translate_text("Please enter some text.", lang_code))
        else:
            res = requests.post(f"{API_URL}/summarize", json={"text": text})

            if res.status_code == 200:
                summary = res.json().get("summary", "No summary returned.")
                st.success(translate_text(summary, lang_code))
            else:
                st.error("Backend error")


# =====================================================
# 2️⃣ SUBMIT FEEDBACK
# =====================================================
elif option == "Submit Feedback":

    st.subheader(translate_text("📝 Citizen Feedback", lang_code))

    name = st.text_input(translate_text("Your Name", lang_code))

    categories = ["Water", "Electricity", "Road", "Pollution", "Other"]
    translated_categories = [translate_text(cat, lang_code) for cat in categories]

    selected_category_translated = st.selectbox(
        translate_text("Category", lang_code),
        translated_categories
    )

    # Map back to English
    category = categories[translated_categories.index(selected_category_translated)]

    message = st.text_area(translate_text("Describe the issue", lang_code))

    if st.button(translate_text("Submit Feedback", lang_code)):

        if name and message:
            payload = {"name": name, "message": message, "category": category}
            res = requests.post(f"{API_URL}/feedback", json=payload)

            st.success(translate_text(res.json().get("message", ""), lang_code))
        else:
            st.warning(translate_text("Please fill in all fields.", lang_code))


# =====================================================
# 3️⃣ FORECAST KPIs
# =====================================================
elif option == "Forecast KPIs":

    st.subheader(translate_text("📈 Upload KPI Data (CSV)", lang_code))
    file = st.file_uploader(translate_text("Upload KPI CSV", lang_code), type=["csv"])

    if file and st.button(translate_text("Forecast", lang_code)):

        res = requests.post(f"{API_URL}/forecast", files={"file": file})
        forecast = res.json().get("forecast", "No forecast returned.")

        st.info(translate_text(f"Forecast: {forecast}", lang_code))


# =====================================================
# 4️⃣ DETECT ANOMALIES (Dashboard Alert Working)
# =====================================================
elif option == "Detect Anomalies":

    st.subheader(translate_text("⚠️ Anomaly Detection", lang_code))
    file = st.file_uploader(translate_text("Upload KPI CSV", lang_code), type=["csv"])

    if file and st.button(translate_text("Detect Anomalies", lang_code)):

        res = requests.post(f"{API_URL}/anomaly", files={"file": file})

        if res.status_code == 200:
            result = res.json()

            if result.get("alert"):

                st.error(translate_text("🚨 ANOMALY DETECTED!", lang_code))

                anomalies = result.get("anomalies", [])

                if anomalies:
                    st.write(translate_text("Detected Anomalies:", lang_code))
                    st.table(anomalies)

            else:
                st.success(translate_text("✅ No anomalies detected.", lang_code))

        else:
            st.error("Backend error")


# =====================================================
# 5️⃣ ECO TIPS
# =====================================================
elif option == "Get Eco Tips":

    st.subheader(translate_text("🌍 Eco Tips Generator", lang_code))
    keyword = st.text_input(translate_text("Enter sustainability topic", lang_code))

    if st.button(translate_text("Get Tips", lang_code)):

        if keyword:
            res = requests.post(f"{API_URL}/tips", json={"keyword": keyword})
            tips = res.json().get("tips", "")

            st.info(translate_text(tips, lang_code))
        else:
            st.warning(translate_text("Please enter a keyword.", lang_code))


# =====================================================
# 6️⃣ CHAT ASSISTANT
# =====================================================
elif option == "Ask the Assistant":

    st.subheader(translate_text("🤖 Chat with Assistant", lang_code))
    query = st.text_input(translate_text("Ask your question", lang_code))

    if st.button(translate_text("Send", lang_code)):

        if not query:
            st.warning(translate_text("Please type a question.", lang_code))
        else:
            res = requests.post(f"{API_URL}/chat", json={"query": query})

            if res.status_code == 200:
                response = res.json().get("response", "")
                st.success(translate_text(response, lang_code))
            else:
                st.error("Backend error")