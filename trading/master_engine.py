from database import cursor, conn
from trading.copy_engine import copy_trade
from bot.alerts import send_alert   # ✅ FIXED IMPORT
from datetime import datetime


def execute_trade(symbol, side, entry, sl, tp):

    trade = {
        "symbol": symbol,
        "side": side,
        "entry": entry,
        "sl": sl,
        "tp": tp,
        "timestamp": str(datetime.now())
    }

    try:
        # Save trade to database
        cursor.execute("""
            INSERT INTO trades (symbol, side, entry, sl, tp, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (symbol, side, entry, sl, tp, trade["timestamp"]))

        conn.commit()

        # Send alert
        send_alert(trade)

        # Copy to users
        copy_trade(trade)

        return {"status": "success", "trade": trade}

    except Exception as e:
        print("Trade execution error:", e)
        return {"status": "error", "message": str(e)}
