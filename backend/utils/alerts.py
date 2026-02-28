import requests
from datetime import datetime

# -----------------------------
# Telegram Alert (FREE)
# -----------------------------
def send_telegram_alert(message):
    token = "YOUR_TELEGRAM_BOT_TOKEN"
    chat_id = "YOUR_CHAT_ID"

    url = f"https://api.telegram.org/bot{token}/sendMessage"
    data = {"chat_id": chat_id, "text": message}

    try:
        requests.post(url, data=data)
    except Exception as e:
        print("Telegram Error:", e)


# -----------------------------
# Trigger Alert
# -----------------------------
def trigger_alert(kpi_name, value):
    message = f"""
🚨 SMART CITY ALERT
KPI: {kpi_name}
Abnormal Value: {value}
Time: {datetime.now()}
"""
    send_telegram_alert(message)