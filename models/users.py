from database import cursor, conn

def add_user(telegram_id):
    cursor.execute("""
        INSERT OR IGNORE INTO users (telegram_id)
        VALUES (?)
    """, (telegram_id,))
    conn.commit()


def get_users():
    cursor.execute("SELECT telegram_id, risk, active FROM users WHERE active=1")
    return cursor.fetchall()


def set_risk(telegram_id, risk):
    cursor.execute("""
        UPDATE users SET risk=? WHERE telegram_id=?
    """, (risk, telegram_id))
    conn.commit()
