from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os

TOKEN = os.getenv("BOT_TOKEN")

# Old text + buttons (with emojis, exactly as in your original code)
keyboard = [
    [InlineKeyboardButton("Register", url="https://your-site.com")],
    [InlineKeyboardButton("Channel", url="https://t.me/yourchannel")]
]
reply_markup = InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        " Welcome to BYD!\nChoose below:",
        reply_markup=reply_markup
    )

async def welcome_new_member(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This runs automatically when someone joins the group
    for new_member in update.message.new_chat_members:
        # Skip welcoming the bot itself if it joins
        if new_member.is_bot:
            continue
        # Using the exact old welcome text
        welcome_text = "Welcome to BYD!\nChoose below:"
        await update.message.reply_text(
            welcome_text,
            reply_markup=reply_markup
        )

app = ApplicationBuilder().token(TOKEN).build()

# Keep the original /start command
app.add_handler(CommandHandler("start", start))

# Welcome bot functionality for new group members
app.add_handler(MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, welcome_new_member))

app.run_polling()