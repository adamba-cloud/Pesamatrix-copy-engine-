from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from database import cursor, conn
from config import BOT_TOKEN


# =========================
# COMMANDS
# =========================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    try:
        cursor.execute("""
            INSERT OR IGNORE INTO users (telegram_id)
            VALUES (?)
        """, (user.id,))
        conn.commit()

        await update.message.reply_text("Welcome to Copy Trading Bot 🚀")

    except Exception as e:
        print("DB Error:", e)
        await update.message.reply_text("Error saving user ❌")


async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("System Running ✅")


# =========================
# BOT RUNNER
# =========================

def run_bot():
    try:
        app = Application.builder().token(BOT_TOKEN).build()

        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("status", status))

        print("🤖 Telegram bot started...")
        app.run_polling()

    except Exception as e:
        import traceback
        print("BOT CRASHED:")
        traceback.print_exc()
