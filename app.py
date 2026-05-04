from flask import Flask, request, jsonify
from trading.master_engine import execute_trade

app = Flask(__name__)

@app.route("/")
def home():
    return "Copy Trading System Active 🚀"

@app.route("/trade", methods=["POST"])
def trade():
    data = request.json

    result = execute_trade(
        data["symbol"],
        data["side"],
        data["entry"],
        data["sl"],
        data["tp"]
    )

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
