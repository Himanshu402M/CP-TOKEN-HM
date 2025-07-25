# Classplus Token Generator Telegram Bot

This bot fetches a Classplus token using the API from https://jaatcptokenapi.vercel.app.

## 🚀 How to Use

1. Send a message to the bot in this format:
   ```
   /gettoken your@email.com
   ```

2. The bot will reply with the generated token.

## 🛠 Setup

### 1. Clone and Install
```bash
git clone https://github.com/yourusername/classplus-bot.git
cd classplus-bot
pip install -r requirements.txt
```

### 2. Add your Telegram Bot token
Create a `.env` file:
```
BOT_TOKEN=your_token_here
```

### 3. Run the bot
```bash
python bot.py
```

## 📦 Deploy on Render

1. Create new Web Service on [Render](https://render.com)
2. Connect your GitHub repo
3. Set build and start command:
   - **Start command**: `python bot.py`
4. Add environment variable: `BOT_TOKEN`
5. Deploy!
