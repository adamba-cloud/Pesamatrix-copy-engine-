from datetime import datetime

def now():
    return str(datetime.now())


def format_trade(trade):
    return f"""
PAIR: {trade['symbol']}
SIDE: {trade['side']}
ENTRY: {trade['entry']}
SL: {trade['sl']}
TP: {trade['tp']}
TIME: {trade.get('timestamp', now())}
"""
