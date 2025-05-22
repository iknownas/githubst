from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Github Seller! Click below to view products:\n\nhttps://githubstudents.netlify.app/")

app = ApplicationBuilder().token("7664448568:AAFXPc3fbBKvoH8tNbKGU-DpqPJykAHks9k").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
