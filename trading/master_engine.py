from database import cursor, conn
from trading.copy_engine import copy_trade
from telegram.alerts import send_alert
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

    cursor.execute("""
        INSERT INTO trades (symbol, side, entry, sl, tp, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (symbol, side, entry, sl, tp, trade["timestamp"]))

    conn.commit()

    send_alert(trade)
    copy_trade(trade)

    return {"status": "success", "trade": trade}
