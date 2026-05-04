from database import cursor
from trading.risk_manager import check_risk

def copy_trade(trade):

    cursor.execute("SELECT telegram_id, risk FROM users WHERE active=1")
    users = cursor.fetchall()

    for user in users:
        telegram_id, risk = user

        adjusted = check_risk(trade, risk)

        print(f"[COPY] Sending trade to {telegram_id}: {adjusted}")
