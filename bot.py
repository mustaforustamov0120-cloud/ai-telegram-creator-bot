import os
from datetime import datetime

try:
    from telegram import Update
    from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
except ImportError:
    print("Please install python-telegram-bot:")
    print("pip install python-telegram-bot")
    exit()


BOT_TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    text = (
        f"Hello, {user.first_name}!\n\n"
        "I am AI Telegram Creator Bot.\n"
        "I help creators generate ideas, prompts, scripts, translations, and content plans.\n\n"
        "Commands:\n"
        "/idea - Generate a video idea\n"
        "/prompt - Generate an AI prompt\n"
        "/script - Generate a short video script\n"
        "/help - Show help"
    )

    await update.message.reply_text(text)


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "AI Telegram Creator Bot Help\n\n"
        "Use this bot to create content faster.\n\n"
        "Available commands:\n"
        "/idea - Get a YouTube Shorts idea\n"
        "/prompt - Get an AI image or video prompt\n"
        "/script - Get a short script idea\n\n"
        "You can also send any message and the bot will respond with a content suggestion."
    )

    await update.message.reply_text(text)


async def idea(update: Update, context: ContextTypes.DEFAULT_TYPE):
    ideas = [
        "A cinematic AI video showing a lost ancient city before disaster.",
        "A YouTube Short comparing two popular game characters in Tiles Hop style.",
        "A faceless video explaining how AI tools can help creators in 2026.",
        "A horror story short about a strange message received at 3 AM.",
        "A Telegram post about the best AI tools for content creators."
    ]

    text = "Video idea:\n\n" + ideas[datetime.now().second % len(ideas)]
    await update.message.reply_text(text)


async def prompt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "AI Prompt:\n\n"
        "Create a cinematic vertical 9:16 video scene for YouTube Shorts. "
        "Use dramatic lighting, smooth camera movement, realistic details, "
        "high contrast, professional composition, and a strong visual hook in the first second."
    )

    await update.message.reply_text(text)


async def script(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "Short Video Script:\n\n"
        "Hook: Most people use AI the wrong way.\n"
        "Main point: AI works best when you give it clear tasks, examples, and a goal.\n"
        "Ending: Start with one simple workflow and improve it every day."
    )

    await update.message.reply_text(text)


async def message_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    response = (
        "Content suggestion based on your message:\n\n"
        f"Topic: {user_text}\n\n"
        "Try turning this into a short video with:\n"
        "1. A strong hook\n"
        "2. One clear idea\n"
        "3. Fast pacing\n"
        "4. A simple ending"
    )

    await update.message.reply_text(response)


def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN environment variable is missing.")
        print("Set it before running the bot.")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("idea", idea))
    app.add_handler(CommandHandler("prompt", prompt))
    app.add_handler(CommandHandler("script", script))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_handler))

    print("Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
