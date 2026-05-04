import requests
from config import BOT_TOKEN

def send_alert(trade):

    message = f"""
🚨 NEW TRADE

📊 {trade['symbol']}
📈 {trade['side']}
💰 Entry: {trade['entry']}
🛑 SL: {trade['sl']}
🎯 TP: {trade['tp']}
"""

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    requests.post(url, json={
        "chat_id": "@your_channel",
        "text": message
    })
