import os import logging import requests from dotenv import load_dotenv from telegram import Update from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

Load environment variables from .env if present

load_dotenv()

Enable structured logging

logging.basicConfig( format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO ) logger = logging.getLogger(name)

Retrieve bot token from environment

TOKEN = os.getenv("BOT_TOKEN")

/gettoken command handler

async def get_token(update: Update, context: ContextTypes.DEFAULT_TYPE): if len(context.args) != 1: await update.message.reply_text("❌ Usage: /gettoken your@email.com") return

email = context.args[0]
api_url = f"https://jaatcptokenapi.vercel.app/get-token?email={email}"

try:
    response = requests.get(api_url, timeout=10)
    if response.status_code == 200:
        token = response.json().get("token")
        if token:
            await update.message.reply_text(f"✅ Token generated: `{token}`", parse_mode="Markdown")
        else:
            await update.message.reply_text("❌ Token not found in response.")
    else:
        await update.message.reply_text(f"❌ Failed to get token from API. Status code: {response.status_code}")
except Exception as e:
    logger.error(f"Error while fetching token: {e}")
    await update.message.reply_text(f"❌ Error: {str(e)}")

/start command handler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text("👋 Send /gettoken your@email.com to get your token.")

Main bot runner

def main(): if TOKEN is None: logger.error("BOT_TOKEN not set in environment.") return

app = ApplicationBuilder().token(TOKEN).build()

# Command handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("gettoken", get_token))

logger.info("Bot is starting...")
app.run_polling()

Entry point

if name == "main": main()

