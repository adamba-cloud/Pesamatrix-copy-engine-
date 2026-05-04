import os
import threading
from flask import Flask, request, jsonify

from trading.master_engine import execute_trade
from telegram.bot import run_bot

app = Flask(__name__)

# =========================
# TELEGRAM BOT START (BACKGROUND THREAD)
# =========================
def start_bot():
    run_bot()

threading.Thread(target=start_bot, daemon=True).start()

# =========================
# FLASK ROUTES
# =========================

@app.route("/")
def home():
    return "Copy Trading System Active 🚀"

@app.route("/trade", methods=["POST"])
def trade():
    data = request.json

    # Basic validation (important for stability)
    required_fields = ["symbol", "side", "entry", "sl", "tp"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    result = execute_trade(
        data["symbol"],
        data["side"],
        data["entry"],
        data["sl"],
        data["tp"]
    )

    return jsonify(result)

# =========================
# START SERVER (RENDER SAFE)
# =========================

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
