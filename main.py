import telebot
from conf import TOKEN, KEYS

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


bot.polling()
