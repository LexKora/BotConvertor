import telebot
import requests
import json

from conf import TOKEN, KEYS, HEADERS

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'помощь'])
def start_help(message: telebot.types.Message):
    txt = 'Для того что бы получить курс введите данные в формате:\n\
<первая валюта>  <вторая валюта>  <количество первой валюты>\n\
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
    val1, val2, amount = message.text.split(' ')
    url = f'https://api.apilayer.com/currency_data/convert?to={KEYS[val1]}&from={KEYS[val2]}&amount={amount}'
    r = requests.get(url, headers=HEADERS)
    txt = json.loads(r.content)['result']
    bot.send_message(message.chat.id, txt)

bot.polling(none_stop=True)
