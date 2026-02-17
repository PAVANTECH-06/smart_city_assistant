import streamlit as st
import requests

st.set_page_config(page_title="Smart City Assistant", layout="centered")

API_URL = "http://localhost:8000"

st.title("🌱 Sustainable Smart City Assistant")
st.markdown("Empowering cities with AI for smarter, greener living.")

option = st.sidebar.radio("📊 Choose a Module", [
    "Summarize Policy",
    "Submit Feedback",
    "Forecast KPIs",
    "Detect Anomalies",
    "Get Eco Tips",
    "Ask the Assistant"
])

if option == "Summarize Policy":
    st.subheader("📄 Summarize a Policy Document")
    text = st.text_area("Enter full policy or document content")

    if st.button("Summarize"):
        if not text.strip():
            st.warning("Please enter some text to summarize.")
        else:
            try:
                res = requests.post(
                    f"{API_URL}/summarize",
                    json={"text": text},
                    timeout=30
                )

                if res.status_code == 200:
                    data = res.json()
                   # print(data)
                    st.success(data.get("summary", "No summary returned"))
                else:
                    st.error("Backend error occurred")
                    st.text(res.text)

            except requests.exceptions.RequestException as e:
                st.error("Could not connect to backend")
                st.text(str(e))


elif option == "Submit Feedback":
    st.subheader("📝 Citizen Feedback")
    name = st.text_input("Your Name")
    category = st.selectbox("Category", ["Water", "Electricity", "Road", "Pollution", "Other"])
    message = st.text_area("Describe the issue")
    if st.button("Submit Feedback"):
        if name and message:
            payload = {"name": name, "message": message, "category": category}
            res = requests.post(f"{API_URL}/feedback", json=payload)
            st.success(res.json()["message"])
        else:
            st.warning("Please fill in all fields.")

elif option == "Forecast KPIs":
    st.subheader("📈 Upload KPI Data (CSV)")
    file = st.file_uploader("Upload KPI CSV", type=["csv"])
    if file and st.button("Forecast"):
        res = requests.post(f"{API_URL}/forecast", files={"file": file})
        forecast = res.json().get("forecast", "No forecast returned.")
        st.info(f"📊 Forecast: {forecast}")


elif option == "Detect Anomalies":
    st.subheader("⚠️ Anomaly Detection")
    file = st.file_uploader("Upload KPI CSV", type=["csv"])
    if file and st.button("Detect Anomalies"):
        res = requests.post(f"{API_URL}/anomaly", files={"file": file})
        analysis = res.json().get("anomalies", "No anomalies found.")
        st.markdown(f"### 📋 Analysis:\n{analysis}")


elif option == "Get Eco Tips":
    st.subheader("🌍 Eco Tips Generator")
    keyword = st.text_input("Enter a sustainability topic (e.g., plastic, energy, solar)")
    if st.button("Get Tips"):
        if keyword:
            res = requests.post(f"{API_URL}/tips", json={"keyword": keyword})
            tip = res.json()["tips"]
            st.info(tip)

        else:
            st.warning("Enter a keyword to get eco tips.")

elif option == "Ask the Assistant":
    st.subheader("🤖 Chat with the Smart City Assistant")
    query = st.text_input("Ask your question")

    if st.button("Send"):
        if not query:
            st.warning("Please type a question.")
        else:
            try:
                res = requests.post(
                    f"{API_URL}/chat",
                    json={"query": query},
                    timeout=30
                )

                if res.status_code == 200:
                    st.success(res.json().get("response", "No response"))
                else:
                    st.error("Backend error")
                    st.text(res.text)

            except requests.exceptions.RequestException as e:
                st.error("Server not reachable")
                st.text(str(e))

