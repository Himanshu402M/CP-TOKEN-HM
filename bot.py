import os
import requests
from dotenv import load_dotenv
from telegram.ext import Updater, CommandHandler

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

def get_token(update, context):
    if len(context.args) != 1:
        update.message.reply_text("❌ Usage: /gettoken your@email.com")
        return

    email = context.args[0]
    api_url = f"https://jaatcptokenapi.vercel.app/get-token?email={email}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            token = response.json().get("token")
            if token:
                update.message.reply_text(f"✅ Token generated: {token}")
            else:
                update.message.reply_text("❌ Token not found in response.")
        else:
            update.message.reply_text("❌ Failed to get token from API.")
    except Exception as e:
        update.message.reply_text(f"❌ Error: {str(e)}")

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("gettoken", get_token))
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
