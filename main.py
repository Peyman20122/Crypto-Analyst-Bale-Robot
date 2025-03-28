import logging
import requests
import yfinance as yf
from time import sleep
from telegram.ext import Updater,CommandHandler,CallbackQueryHandler,Filters, ConversationHandler,MessageHandler
from telegram import InlineKeyboardButton,InlineKeyboardMarkup,Bot
import matplotlib.pyplot as plt
import openai

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def get_bitcoin_price():
    response = requests.get('https://api.coinbase.com/v2/prices/buy?currency=USD')
    price = float(response.json().get('data', {}).get('amount'))
    return price

def button_start():
    keyboard = [
        [InlineKeyboardButton('قیمت', callback_data='start1')],
        [InlineKeyboardButton('تحلیل', callback_data='start2')],
        [InlineKeyboardButton('نمودار', callback_data='start3')]
    ]
    return InlineKeyboardMarkup(keyboard)


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='سلام به ربات اطلاع دهنده و تحلیلگر ارز های دیجیتال خوش آمدید')
    sleep(5)
    bot.send_message(chat_id=update.message.chat_id,
                     text='توسعه دهنده : پیمان دایی رضایی ')
    sleep(5)
    reply_markup = button_start()
    bot.send_message(chat_id=update.message.chat_id,  text=f'برای مشاهده قیمت  یا تحلیل یا نمودار'
                                                           f' Bitcoin کلیک کنید:',
                     reply_markup=reply_markup)


def plot_bitcoin_price():
    df = yf.download('BTC-USD', period='3mo')
    if df.empty:
        print("دریافت داده‌ها ناموفق بود. لطفاً اتصال خود را بررسی کنید.")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(df.index, df['Close'], label='Bitcoin Closing Price', color='blue')
    plt.title("Bitcoin Price Chart Last 3 Months")
    plt.xlabel("Date")
    plt.ylabel("Price (USD)")
    plt.legend()
    plt.grid(True)
    image_path = "bitcoin_chart.png"
    plt.savefig(image_path)
    plt.close()


    return image_path


def analyze_with_chatgpt():
    openai.api_key = "YOUR_API_KEY"
    df = yf.download('BTC-USD', period='3mo')

    recent_price = df['Close'].iloc[-1]
    start_price = df['Close'].iloc[0]
    max_price = df['Close'].max()
    min_price = df['Close'].min()
    change_percent = ((recent_price - start_price) / start_price) * 100

    prompt = f"""
    سلام! لطفاً یک تحلیل جامع و خلاصه درباره روند قیمت بیت‌کوین در ۳ ماه گذشته ارائه دهید.

    قیمت فعلی بیت‌کوین: {recent_price:.2f} دلار  
    قیمت بیت‌کوین ۳ ماه پیش: {start_price:.2f} دلار  
    بالاترین قیمت در این بازه: {max_price:.2f} دلار  
    پایین‌ترین قیمت در این بازه: {min_price:.2f} دلار  
    تغییر کلی قیمت در ۳ ماه اخیر: {change_percent:.2f}%

    لطفاً توضیح دهید که این تغییرات چه معنایی دارند، آیا روند صعودی یا نزولی است، و چه عواملی ممکن است در این تغییرات مؤثر بوده باشند.
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
        )
    analysis = response['choices'][0]['message']['content']
    return analysis



def Price():
    price = get_bitcoin_price()
    return price


def error(bot, update):
    logger.warning('Update "%s" caused error "%s"', bot, update.error)

def button(bot, update):
    query = update.callback_query
    if query.data == 'start1':
        bot.send_message(chat_id=query.message.chat_id, message_id=query.message.message_id, text=f"قیمت Bitcoin:",reply_markup=Price())
    elif query.data == 'start2':
        bot.send_message(chat_id=query.message.chat_id, message_id=query.message.message_id,reply_markup=analyze_with_chatgpt())
    elif query.data == 'start3':
        image_path = plot_bitcoin_price()
        bot.send_photo(chat_id=query.message.chat_id,message_id=query.message.message_id, photo=open(image_path, 'rb'),caption='نمودار قیمت بیت‌کوین در ۳ ماه گذشته')
def main():
    Token = '423932490:9cdUx3MAUVBGWmkv4TIqrx2O8KTtNCV5f4g5o5kY'
    updater = Updater(token=Token, base_url="https://tapi.bale.ai/bot")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    dp.add_error_handler(error)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
