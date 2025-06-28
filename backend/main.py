import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from routes import summarization, feedback, forecast, anomaly, tips, chat

app = FastAPI()

app.include_router(summarization.router)
app.include_router(feedback.router)
app.include_router(forecast.router)
app.include_router(anomaly.router)
app.include_router(tips.router)
app.include_router(chat.router)
@app.get("/")
def root():
    return {"message": "Welcome to the Smart City Assistant API"}
