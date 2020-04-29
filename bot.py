import yfinance as yf
import telebot
import cur_rate
import crypto

bot = telebot.TeleBot('1200593659:AAFMpll7K1qnrQWCF5mKHVEJK8QGJKtQjc8')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Акции', 'Валюты', 'Криптовалюты')

keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard2.row('Apple', 'Amazon', 'Tesla', 'Назад')

keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard3.row('USD', 'EURO', 'JPY', 'Назад')

keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard4.row('Bitcoin', 'ETH', 'LTC', 'Назад')


# @bot.message_handler(content_types=['text'])
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Выберите интересующие Вас активы", reply_markup=keyboard1)
    # bot.register_next_step_handler(message, get_inf)


@bot.message_handler(content_types=['text'])
def get_inf(message):
    if message.text == "Акции":
        bot.register_next_step_handler(message, get_stocks)
        bot.send_message(message.from_user.id, "Выберите интересующие Вас акции", reply_markup=keyboard2)
    elif message.text == 'Валюты':
        bot.register_next_step_handler(message, get_currency)
        bot.send_message(message.from_user.id, "Выберите интересующую Вас валюту", reply_markup=keyboard3)
    elif message.text == 'Криптовалюты':
        bot.register_next_step_handler(message, get_crypto)
        bot.send_message(message.from_user.id, "Выберите интересующую Вас криптовалюту", reply_markup=keyboard4)
    else:
        bot.send_message(message.from_user.id, "Выберите актив из списка", reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def get_stocks(message):
    if message.text == "Apple":
        stocks = yf.Ticker('AAPL')
        bot.send_message(message.from_user.id, 'Стоимость акций Apple '+str(stocks.info['ask'])+str(' USD'))
        start(message)
    elif message.text == "Amazon":
        stocks = yf.Ticker('AMZN')
        bot.send_message(message.from_user.id, str('Стоимость акций Amazon '+stocks.info['ask'])+str(' USD'))
        start(message)
    if message.text == "Tesla":
        stocks = yf.Ticker('TSLA')
        bot.send_message(message.from_user.id, 'Стоимость акций Tesla '+str(stocks.info['ask'])+str(' USD'))
        start(message)
    if message.text == "Назад":
        get_inf(message)


def get_currency(message):
    if message.text == "USD":
        bot.send_message(message.from_user.id, cur_rate.usd())
        start(message)
    if message.text == "EURO":
        bot.send_message(message.from_user.id, cur_rate.euro())
        start(message)
    if message.text == "JPY":
        bot.send_message(message.from_user.id, cur_rate.jpy())
        start(message)
    if message.text == "Назад":
        get_inf(message)


def get_crypto(message):
    if message.text == "Bitcoin":
        bot.send_message(message.from_user.id, crypto.btc())
        start(message)
    if message.text == "ETH":
        bot.send_message(message.from_user.id, crypto.eth())
        start(message)
    if message.text == "LTC":
        bot.send_message(message.from_user.id, crypto.ltc())
        start(message)
    if message.text == "Назад":
        get_inf(message)


bot.polling(none_stop=True, interval=0)
