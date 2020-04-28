import yfinance as yf
import telebot

telebot.apihelper.proxy = {'http': 'http://10.10.1.10:3128'}

bot = telebot.TeleBot('1200593659:AAFMpll7K1qnrQWCF5mKHVEJK8QGJKtQjc8')
keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Акции', 'Валюты', 'Криптовалюты')


@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        bot.send_message(message.from_user.id, text='Выбери интересующие тебя активы', reply_markup=keyboard1)

    else:
        bot.send_message(message.from_user.id, 'Напиши /start')


keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
key_stocks = telebot.types.InlineKeyboardButton(text='Акции', callback_data='stocks')
keyboard.add(key_stocks)
key_currency = telebot.types.InlineKeyboardButton(text='Валюты', callback_data='currency')
keyboard.add(key_currency)
key_crypto = telebot.types.InlineKeyboardButton(text='Криптовалюты', callback_data='crypto')
keyboard.add(key_crypto)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "Акции":  # call.data это callback_data, которую мы указали при объявлении кнопки
        keyboard2 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard2.row('Apple', 'Tesla', 'Facebook')  # наша клавиатура
        key_aapl = telebot.types.InlineKeyboardButton(text='Apple', callback_data='aapl')
        keyboard2.add(key_aapl)
        key_tsla = telebot.types.InlineKeyboardButton(text='Tesla', callback_data='tsla')
        keyboard2.add(key_tsla)
        key_fb = telebot.types.InlineKeyboardButton(text='Facebook', callback_data='fb')
        keyboard2.add(key_fb)

        bot.send_message(call.from_user.id, text='Выбери нужную акцию', reply_markup=keyboard1)

    elif call.data == "currency":  # call.data это callback_data, которую мы указали при объявлении кнопки
        keyboard3 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard3.row('Доллар', 'Евро', 'Йена')
        key_usd = telebot.types.InlineKeyboardButton(text='Доллар', callback_data='usd')
        keyboard3.add(key_usd)
        key_euro = telebot.types.InlineKeyboardButton(text='Евро', callback_data='euro')
        keyboard3.add(key_euro)
        key_yena = telebot.types.InlineKeyboardButton(text='Йена', callback_data='yena')
        keyboard3.add(key_yena)

        bot.send_message(call.from_user.id, text='Выбери нужную валюту', reply_markup=keyboard1)

    elif call.data == "crypto":  # call.data это callback_data, которую мы указали при объявлении кнопки
        keyboard4 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard4.row('Bitcoin', 'ETH', 'NEO')
        key_bitcoin = telebot.types.InlineKeyboardButton(text='Биткоин', callback_data='bitcoin')
        keyboard4.add(key_bitcoin)
        key_eth = telebot.types.InlineKeyboardButton(text='Эфириум', callback_data='eth')
        keyboard4.add(key_eth)
        key_neo = telebot.types.InlineKeyboardButton(text='NEO', callback_data='neo')
        keyboard4.add(key_neo)

        bot.send_message(call.from_user.id, text='Выбери нужную акцию', reply_markup=keyboard1)


bot.polling(none_stop=True, interval=0)



