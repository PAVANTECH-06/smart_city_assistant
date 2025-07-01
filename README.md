# 🌱 Sustainable Smart City Assistant

An AI-powered assistant designed to help municipalities and citizens manage urban sustainability using IBM Watsonx Granite LLM and Google Gemini. Built with FastAPI, Streamlit, and ML tools for forecasting and anomaly detection.

---

## 🚀 Features

### 🧠 AI Modules (Gemini & Watsonx)
- **Summarization**: Upload policy documents and get concise summaries.
- **Chat Assistant**: Ask sustainability-related questions, get smart city solutions.
- **Eco Tips**: Receive actionable eco-friendly tips based on topics like plastic or solar.

### 📊 Data Intelligence
- **KPI Forecasting**: Upload `.csv` with historical data and predict future trends.
- **Anomaly Detection**: Highlight unusual spikes in KPIs (like electricity or water).

### 📢 Civic Engagement
- **Citizen Feedback**: Submit reports about urban issues (water leaks, road damage).

---

## 🖼️ Project Architecture

```

smart\_city\_assistant/
├── backend/
│   ├── main.py               # FastAPI entry point
│   ├── routes/               # API route modules
│   ├── services/             # Gemini + ML utility functions
│   ├── models/               # Pydantic schemas
│   └── utils/
├── frontend/
│   └── app.py                # Streamlit UI
├── .env                      # API keys (not committed)
├── requirements.txt
└── README.md

````

---

## 📸 Screenshots

| Summarization | Forecast | Tips |
|---------------|----------|------|
| ![Summary](https://github.com/PAVANTECH-06/smart_city_assistant/blob/main/screenshots/summarize.png) | ![Forecast](https://github.com/PAVANTECH-06/smart_city_assistant/blob/main/screenshots/forecast.png) | ![Tips](https://github.com/PAVANTECH-06/smart_city_assistant/blob/main/screenshots/tips.png) |

## 🎥 Demo Video

▶️ [![Demo Video](https://github.com/PAVANTECH-06/smart_city_assistant/blob/main/screenshots/demo.png)](https://drive.google.com/file/d/1u453N7XaYV_FV89H-ollSnzUNxIVnzgy/view)


---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/PAVANTECH-06/smart_city_assistant.git
cd smart_city_assistant
````

2. **Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate   # Windows
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add your API keys to `.env`**

```ini
GOOGLE_API_KEY=your_gemini_key
WATSONX_API_KEY=your_ibm_key
```

---

## 🧪 Run the Project

### 🟢 Run Backend

```bash
cd backend
uvicorn main:app --reload
```

Test API at: [http://localhost:8000/docs](http://localhost:8000/docs)

### 🎨 Run Frontend (Streamlit)

```bash
cd frontend
streamlit run app.py
```

Open: [http://localhost:8501](http://localhost:8501)

---

## 🧠 Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* [Streamlit](https://streamlit.io/)
* [Google Gemini (via `google-generativeai`)](https://ai.google.dev/)
* [IBM Watsonx Granite LLM](https://www.ibm.com/products/watsonx-llm)
* [Pandas / scikit-learn](https://scikit-learn.org/)
* [Pinecone](https://www.pinecone.io/) *(optional module for semantic search)*

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you’d like to change.

---

## 📜 License

MIT License — use it freely, just give credit.

---

## 🙋 Author

**Pavan Gubbala**
GitHub: [@PAVANTECH-06](https://github.com/PAVANTECH-06)
Email: *gubbalapavan9347@gmail.com*

---



---

### ✅ Next Step:
Copy this into your `README.md` file in VS Code and push it:

```bash
git add README.md
git commit -m "Add README with project details"
git push
````
