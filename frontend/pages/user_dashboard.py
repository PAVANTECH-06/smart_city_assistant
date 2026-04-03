def run():
    import streamlit as st
    import requests

    API_URL = "http://localhost:8000"

    # ==============================
    # 🎨 HIDE PAGE NAV ONLY
    # ==============================
    st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {display:none;}
    </style>
    """, unsafe_allow_html=True)

    # ==============================
    # 🔐 SESSION CHECK
    # ==============================
    if not st.session_state.get("logged_in"):
        st.warning("Please login first")
        st.stop()

    if st.session_state.role != "user":
        st.error("Unauthorized access")
        st.stop()

    # ==============================
    # 🔥 TRANSLATION FUNCTION
    # ==============================
    @st.cache_data(show_spinner=False)
    def translate_batch(texts, target_lang):
        if target_lang == "English":
            return texts

        try:
            res = requests.post(
                f"{API_URL}/translate",
                json={"texts": texts, "target_lang": target_lang}
            )
            return res.json().get("translated", texts)
        except:
            return texts

    # ==============================
    # 🌐 LANGUAGE SELECTOR
    # ==============================
    language_dict = {
        "English": "English",
        "Hindi": "Hindi",
        "Telugu": "Telugu"
    }

    selected_language = st.selectbox("🌐 Select Language", list(language_dict.keys()))
    lang_code = language_dict[selected_language]

    # ==============================
    # 🔥 UI TEXT TRANSLATION
    # ==============================
    ui_texts = [
        "🌱 Smart City Assistant",
        "Welcome",
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
        welcome_text,
        sidebar_title,
        m1, m2, m3, m4, m5, m6
    ) = translated

    # ==============================
    # 🏷️ HEADER
    # ==============================
    st.title(title)
    st.success(f"{welcome_text} {st.session_state.username} 👋")

    if st.button("🚪 Logout"):
        st.session_state.clear()
        st.rerun()

    # ==============================
    # 📊 SIDEBAR MODULES
    # ==============================
    st.sidebar.title("🌆 Smart City")
    st.sidebar.markdown("---")

    modules = [m1, m2, m3, m4, m5, m6]

    selected = st.sidebar.radio(sidebar_title, modules)

    # Map back to English
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
    # 🔁 HELPER
    # ==============================
    def t(text):
        return translate_batch([text], lang_code)[0]

    # ==============================
    # 📊 ACTIVITY TRACKING
    # ==============================
    def track(module):
        requests.post(f"{API_URL}/activity/track", json={
            "user_id": st.session_state.user_id,
            "module_name": module
        })

    # =====================================================
    # 1️⃣ SUMMARIZE POLICY
    # =====================================================
    if option == "Summarize Policy":
        track("summarize")

        st.subheader(t("📄 Summarize Policy"))
        text = st.text_area(t("Enter document"))

        if st.button(t("Summarize")):
            res = requests.post(f"{API_URL}/summarize", json={"text": text})
            st.success(t(res.json().get("summary", "")))

    # =====================================================
    # 2️⃣ FEEDBACK (WITH CATEGORY)
    # =====================================================
    elif option == "Submit Feedback":
        track("feedback")

        st.subheader(t("📝 Feedback"))

        name = st.text_input(t("Your Name"))

        categories = ["Water", "Electricity", "Road", "Pollution", "Other"]
        translated_categories = translate_batch(categories, lang_code)

        selected_category = st.selectbox(t("Category"), translated_categories)
        category = categories[translated_categories.index(selected_category)]

        message = st.text_area(t("Describe issue"))

        if st.button(t("Submit")):
            res = requests.post(f"{API_URL}/feedback/", json={
                "user_id": st.session_state.user_id,
                "message": message,
                "category": category
            })
            st.success(t(res.json().get("message", "")))

    # =====================================================
    # 3️⃣ FORECAST KPIs
    # =====================================================
    elif option == "Forecast KPIs":
        track("forecast")

        file = st.file_uploader(t("Upload CSV"), type=["csv"])

        if file and st.button(t("Forecast")):
            res = requests.post(f"{API_URL}/forecast", files={"file": file})
            st.info(t(res.json().get("forecast", "")))

    # =====================================================
    # 4️⃣ ANOMALY DETECTION
    # =====================================================
    elif option == "Detect Anomalies":
        track("anomaly")

        file = st.file_uploader(t("Upload CSV"), type=["csv"])

        if file and st.button(t("Detect")):
            res = requests.post(f"{API_URL}/anomaly", files={"file": file})

            if res.status_code == 200:
                result = res.json()

                if result.get("alert"):
                    st.error(t("🚨 Anomaly Detected"))

                    anomalies = result.get("anomalies", [])
                    if anomalies:
                        st.table(anomalies)
                else:
                    st.success(t("No anomalies found"))

    # =====================================================
    # 5️⃣ ECO TIPS
    # =====================================================
    elif option == "Get Eco Tips":
        track("eco")

        keyword = st.text_input(t("Enter topic"))

        if st.button(t("Get Tips")):
            res = requests.post(f"{API_URL}/tips", json={"keyword": keyword})
            st.info(t(res.json().get("tips", "")))

    # =====================================================
    # 6️⃣ CHAT
    # =====================================================
    elif option == "Ask the Assistant":
        track("chat")

        query = st.text_input(t("Ask question"))

        if st.button(t("Send")):
            res = requests.post(f"{API_URL}/chat", json={"query": query})
            st.success(t(res.json().get("response", "")))