from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8665546957:AAGjzxEuc5ZH8gxq9Wy33WXHA0akcglHmMM"
PWA_LINK = "https://instanthlx.pics"

WELCOME_TEXT = """🎰 Добро пожаловать!

Регистрируйся и получай бонусы:

🎁 *10 000 ₸* — за регистрацию
💰 *30 000 ₸* — за регистрацию + первый депозит
🚀 *До 60 000 ₸* — за пополнение счёта

👇 Нажми чтобы скачать приложение:"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("🎯 Получить бонус", url=PWA_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        WELCOME_TEXT,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
