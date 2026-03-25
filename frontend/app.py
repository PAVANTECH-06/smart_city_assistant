import streamlit as st
import requests

st.set_page_config(page_title="Smart City Assistant", layout="centered")

API_URL = "http://localhost:8000"

# ==============================
# 🔥 Batch Translation Function
# ==============================
@st.cache_data(show_spinner=False)
def translate_batch(texts, target_lang):
    if target_lang == "English":
        return texts

    try:
        res = requests.post(
            f"{API_URL}/translate",
            json={
                "texts": texts,
                "target_lang": target_lang
            }
        )
        return res.json().get("translated", texts)
    except:
        return texts


# ==============================
# 🌐 Language Selection
# ==============================
language_dict = {
    "English": "English",
    "Hindi": "Hindi",
    "Telugu": "Telugu"
}

selected_language = st.selectbox("🌐 Select Language", list(language_dict.keys()))
lang_code = language_dict[selected_language]


# ==============================
# 🔥 FULL UI TRANSLATION
# ==============================
ui_texts = [
    "🌱 Sustainable Smart City Assistant",
    "Empowering cities with AI for smarter, greener living.",
    "📊 Choose a Module",
    "Summarize Policy",
    "Submit Feedback",
    "Forecast KPIs",
    "Detect Anomalies",
    "Get Eco Tips",
    "Ask the Assistant"
]

translated = translate_batch(ui_texts, lang_code)

(
    title,
    subtitle,
    sidebar_title,
    m1, m2, m3, m4, m5, m6
) = translated

# ==============================
# 🏷️ Title Section
# ==============================
st.title(title)
st.markdown(subtitle)

# ==============================
# 📊 Sidebar Modules
# ==============================
modules = [m1, m2, m3, m4, m5, m6]

selected = st.sidebar.radio(sidebar_title, modules)

# Map back to original English
original_modules = [
    "Summarize Policy",
    "Submit Feedback",
    "Forecast KPIs",
    "Detect Anomalies",
    "Get Eco Tips",
    "Ask the Assistant"
]

mapping = dict(zip(modules, original_modules))
option = mapping[selected]


# ==============================
# 🔁 Helper (single text translate)
# ==============================
def t(text):
    return translate_batch([text], lang_code)[0]


# =====================================================
# 1️⃣ SUMMARIZE POLICY
# =====================================================
if option == "Summarize Policy":

    st.subheader(t("📄 Summarize a Policy Document"))
    text = st.text_area(t("Enter full policy or document content"))

    if st.button(t("Summarize")):

        if not text.strip():
            st.warning(t("Please enter some text."))
        else:
            res = requests.post(f"{API_URL}/summarize", json={"text": text})

            if res.status_code == 200:
                summary = res.json().get("summary", "")
                st.success(t(summary))
            else:
                st.error("Backend error")


# =====================================================
# 2️⃣ SUBMIT FEEDBACK
# =====================================================
elif option == "Submit Feedback":

    st.subheader(t("📝 Citizen Feedback"))

    name = st.text_input(t("Your Name"))

    categories = ["Water", "Electricity", "Road", "Pollution", "Other"]
    translated_categories = translate_batch(categories, lang_code)

    selected_category = st.selectbox(t("Category"), translated_categories)

    category = categories[translated_categories.index(selected_category)]

    message = st.text_area(t("Describe the issue"))

    if st.button(t("Submit Feedback")):

        if name and message:
            payload = {"name": name, "message": message, "category": category}
            res = requests.post(f"{API_URL}/feedback", json=payload)

            st.success(t(res.json().get("message", "")))
        else:
            st.warning(t("Please fill in all fields."))


# =====================================================
# 3️⃣ FORECAST KPIs
# =====================================================
elif option == "Forecast KPIs":

    st.subheader(t("📈 Upload KPI Data (CSV)"))
    file = st.file_uploader(t("Upload KPI CSV"), type=["csv"])

    if file and st.button(t("Forecast")):

        res = requests.post(f"{API_URL}/forecast", files={"file": file})
        forecast = res.json().get("forecast", "")

        st.info(t(f"Forecast: {forecast}"))


# =====================================================
# 4️⃣ DETECT ANOMALIES
# =====================================================
elif option == "Detect Anomalies":

    st.subheader(t("⚠️ Anomaly Detection"))
    file = st.file_uploader(t("Upload KPI CSV"), type=["csv"])

    if file and st.button(t("Detect Anomalies")):

        res = requests.post(f"{API_URL}/anomaly", files={"file": file})

        if res.status_code == 200:
            result = res.json()

            if result.get("alert"):
                st.error(t("🚨 ANOMALY DETECTED!"))

                anomalies = result.get("anomalies", [])
                if anomalies:
                    st.write(t("Detected Anomalies:"))
                    st.table(anomalies)
            else:
                st.success(t("✅ No anomalies detected."))
        else:
            st.error("Backend error")


# =====================================================
# 5️⃣ ECO TIPS
# =====================================================
elif option == "Get Eco Tips":

    st.subheader(t("🌍 Eco Tips Generator"))
    keyword = st.text_input(t("Enter sustainability topic"))

    if st.button(t("Get Tips")):

        if keyword:
            res = requests.post(f"{API_URL}/tips", json={"keyword": keyword})
            tips = res.json().get("tips", "")

            st.info(t(tips))
        else:
            st.warning(t("Please enter a keyword."))


# =====================================================
# 6️⃣ CHAT ASSISTANT
# =====================================================
elif option == "Ask the Assistant":

    st.subheader(t("🤖 Chat with Assistant"))
    query = st.text_input(t("Ask your question"))

    if st.button(t("Send")):

        if not query:
            st.warning(t("Please type a question."))
        else:
            res = requests.post(f"{API_URL}/chat", json={"query": query})

            if res.status_code == 200:
                response = res.json().get("response", "")
                st.success(t(response))
            else:
                st.error("Backend error")
