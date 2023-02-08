import telebot

from extensions import Requst, APIException, _spelling
from conf import TOKEN, KEYS
from time import sleep

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    txt = 'Для того что бы получить курс введите данные в формате:\n\
<что переводим>  <во что переводим>  <количество переводимой валюты>\n\
Дробные числа пишем через "."\n\
Что бы увидеть список всех доступных валют наберите: /values или /список'
    bot.send_message(message.chat.id, txt)


@bot.message_handler(commands=['values', 'список'])
def _list(message: telebot.types.Message):
    txt = 'Список доступных валют: '
    for key in KEYS.keys():
        txt = txt + f'\n {key}'
    bot.send_message(message.chat.id, txt)


@bot.message_handler(content_types=['text', ])
def _convertor(message: telebot.types.Message):
    _message = message.text.split(' ')
    try:
        result = round(float(Requst.get_price(_message)), 2)

    except APIException as e:
        bot.reply_to(message, f'Вы ошиблись. \n{e}')
    except Exception as e:
        bot.reply_to(message, f'Ошибка программы. \nНет связи с сервером')
    else:
        base, quote, amount = _message
        txt = f'{amount} {_spelling(base, float(amount))} это {result} {_spelling(quote, result)}'
        bot.reply_to(message, txt)


while True:
    try:
        bot.polling(none_stop=True)
    except Exception as _ex:
        print(_ex)
        sleep(15)
