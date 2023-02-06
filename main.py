import telebot

from extensions import Requst, APIException
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
    _message = message.text.split(' ')
    try:
        result = Requst.get_price(_message)

    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка сервера. \n{e}')
    else:
        base, quote, amount = _message
        txt = f'{amount} {base} {result} {quote}'
        bot.reply_to(message.chat.id, txt)

bot.polling(none_stop=True)
