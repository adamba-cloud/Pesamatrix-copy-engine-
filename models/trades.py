from database import cursor, conn

def save_trade(symbol, side, entry, sl, tp, timestamp):
    cursor.execute("""
        INSERT INTO trades (symbol, side, entry, sl, tp, timestamp)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (symbol, side, entry, sl, tp, timestamp))
    conn.commit()


def get_trades():
    cursor.execute("SELECT * FROM trades ORDER BY id DESC")
    return cursor.fetchall()
