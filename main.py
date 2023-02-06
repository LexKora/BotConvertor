import telebot

from extensions import Requst
from conf import TOKEN, KEYS, HEADERS

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'помощь'])
def start_help(message: telebot.types.Message):
    txt = 'Для того что бы получить курс введите данные в формате:\n\
<что переводим>  <во что переводим>  <количество переводимой валюты>\n\
 Что бы увидеть список всех доступных валют наберите: /values или /список'
    bot.send_message(message.chat.id, txt)


@bot.message_handler(commands=['values', 'список'])
def _list(message: telebot.types.Message):
    txt = 'Список доступных валют: '
    for key in KEYS.keys():
        txt = txt + f'\n {key}'
    bot.send_message(message.chat.id, txt)


@bot.message_handler(content_types=['text', ])
def _list(message: telebot.types.Message):
    result = Requst.get_price(message.text.split(' '))
    if result:
        base, quote, amount = message.text.split(' ')
        txt = f'{amount} {base} {result} {quote}'
        bot.send_message(message.chat.id, txt)


bot.polling(none_stop=True)
