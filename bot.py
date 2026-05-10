from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters

TOKEN = "8532629951:AAHOwGNpI98JL0TftBuzGZjGTEMkHRGzABw"

async def start(update, context):
    await update.message.reply_text("Bot is running 🚀")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot started...")
app.run_polling()
