#  Bale Crypto Bot

##  Description
This bot provides real-time **Bitcoin price updates**, **price analysis using OpenAI GPT**, and **historical price charts** using **Yahoo Finance**. Users can interact with the bot through inline buttons to get insights about Bitcoin.

##  Features
- Get the latest **Bitcoin price** from Coinbase API  
- **Technical analysis** using OpenAI GPT-3.5  
- **Historical price charts** (last 3 months) with Matplotlib  
- Inline keyboard buttons for easy interaction  
- Supports **Bale Messenger** and **Telegram**  

##  Requirements
Ensure you have the following dependencies installed:
```bash
pip install requests yfinance matplotlib python-telegram-bot openai
```

##  Installation & Usage
1. **Clone the repository:**
```bash
git clone https://github.com/your-username/crypto-telegram-bot.git
cd crypto-telegram-bot
```

2. **Set up your API keys:**
- Replace `YOUR_TELEGRAM_BOT_TOKEN` in `main()` with your **Bale Bot Token**.
- Replace `YOUR_API_KEY` in `analyze_with_chatgpt()` with your **OpenAI API Key**.

3. **Run the bot:**
```bash
python bot.py
```

4. **Start the bot on Telegram:**
   - Send `/start` to interact with the bot.
   - Click buttons to **view price, analysis, or chart**.

##  Usage Commands
| Command | Description |
|---------|-------------|
| `/start` | Start the bot and display buttons |
| ` Price` | Fetch the latest Bitcoin price |
| ` Analysis` | Get AI-generated Bitcoin analysis |
| ` Chart` | View a price chart of Bitcoin (last 3 months) |

##  Troubleshooting
If you get an error like `quota exceeded`, make sure you have a **valid OpenAI API key** with available credits. You can check your usage at:
  [OpenAI Usage Dashboard](https://platform.openai.com/account/usage)

For connection issues with **Yahoo Finance**, try changing:
```python
df = yf.download('BTC-USD', period='1mo')  # Change period if data is missing
```

##  Future Improvements
-  Add support for **Ethereum price tracking**
-  Implement **notifications when price crosses a threshold**
-  Deploy the bot using **Docker** for easier deployment

##  License
This project is licensed under the **MIT License**. Feel free to use and modify it!

---
###  Developed by **[Peyman Daei Rezaei]**
- GitHub: [Peyman20122](https://github.com/Peyman20122)  
- Email: peimandaii2012@gmail.com

