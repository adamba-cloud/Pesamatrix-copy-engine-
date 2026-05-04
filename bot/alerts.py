import requests
from config import BOT_TOKEN

TELEGRAM_API = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
CHAT_ID = "@your_channel"   # change this to your real channel or user ID


def send_alert(trade):
    message = f"""
🚨 NEW TRADE

📊 {trade.get('symbol')}
📈 {trade.get('side')}
💰 Entry: {trade.get('entry')}
🛑 SL: {trade.get('sl')}
🎯 TP: {trade.get('tp')}
"""

    try:
        response = requests.post(
            TELEGRAM_API,
            json={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=10
        )

        # Check Telegram response
        if response.status_code != 200:
            print("Telegram API error:", response.text)
        else:
            print("Alert sent successfully")

    except Exception as e:
        print("Failed to send alert:", e)
