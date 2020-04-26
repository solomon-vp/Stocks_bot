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

        keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
        key_stocks = telebot.types.InlineKeyboardButton(text='Акции', callback_data='stocks')
        keyboard.add(key_stocks)
        key_currency = telebot.types.InlineKeyboardButton(text='Валюты', callback_data='currency')
        keyboard.add(key_currency)
        key_crypto = telebot.types.InlineKeyboardButton(text='Криптовалюты', callback_data='crypto')
        keyboard.add(key_crypto)

    else:
        bot.send_message(message.from_user.id, 'Нужно выбрать из списка')


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "stocks":  # call.data это callback_data, которую мы указали при объявлении кнопки
        keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
        key_aapl = telebot.types.InlineKeyboardButton(text='Apple', callback_data='aapl')
        keyboard.add(key_aapl)
        key_tsla = telebot.types.InlineKeyboardButton(text='Tesla', callback_data='tsla')
        keyboard.add(key_tsla)
        key_fb = telebot.types.InlineKeyboardButton(text='Facebook', callback_data='fb')
        keyboard.add(key_fb)

        bot.send_message(call.from_user.id, text='Выбери нужную акцию', reply_markup=keyboard)

    elif call.data == "currency":  # call.data это callback_data, которую мы указали при объявлении кнопки
        keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
        key_usd = telebot.types.InlineKeyboardButton(text='Доллар', callback_data='usd')
        keyboard.add(key_usd)
        key_euro = telebot.types.InlineKeyboardButton(text='Евро', callback_data='euro')
        keyboard.add(key_euro)
        key_yena = telebot.types.InlineKeyboardButton(text='Йена', callback_data='yena')
        keyboard.add(key_yena)

        bot.send_message(call.from_user.id, text='Выбери нужную валюту', reply_markup=keyboard)

    elif call.data == "crypto":  # call.data это callback_data, которую мы указали при объявлении кнопки
        keyboard = telebot.types.InlineKeyboardMarkup()  # наша клавиатура
        key_bitcoin = telebot.types.InlineKeyboardButton(text='Биткоин', callback_data='bitcoin')
        keyboard.add(key_bitcoin)
        key_eth = telebot.types.InlineKeyboardButton(text='Эфириум', callback_data='eth')
        keyboard.add(key_eth)
        key_neo = telebot.types.InlineKeyboardButton(text='НЕО', callback_data='neo')
        keyboard.add(key_neo)


bot.polling(none_stop=True, interval=0)



