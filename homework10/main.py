# Создать бота для вывода текущего курса валют(желательно запрос по конкретной валюте)
import json
import requests
import telebot

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)

msg_ids = [] # для удаления сообщений
valute = dict()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    global msg_ids
    bot.send_message(message.chat.id, "/help\n/del_msg\n/valute\n")
    msg_ids.append(message.message_id)


@bot.message_handler(commands=['del_msg'])
def del_msg(message):
    """delete messages"""
    global msg_ids
    bot.send_message(message.chat.id, msg_ids)
    msg_ids.append(message.message_id)
    for msg in msg_ids:  # ПОПЫТКА УДАЛИТЬ СООБЩЕНИЕ
        try:
            bot.delete_message(message.chat.id, msg)
        except Exception as e:
            print(f'Сообщение не найдено! \n{e}')


@bot.message_handler(commands=['valute'])
def del_msg(message):
    """choose valute"""
    global msg_ids, valute
    bot.send_message(message.chat.id, get_valutes())
    msg_ids.append(message.message_id)


def get_valutes():
    global valute
    response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
    res = json.loads(response.content)
    valute = res['Valute']
    # print('valute', valute)
    valutes_comands = list(map(lambda el: '/' + el['CharCode'] + '-' + el['Name'], valute.values()))
    valutes_comands = "\n".join(valutes_comands)
    # print('valutes_comands', valutes_comands)
    return valutes_comands


@bot.message_handler(
    commands=['AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR',
              'KZT', 'CAD', 'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 'RON', 'XDR', 'SGD', 'TJS', 'TRY', 'TMT',
              'UZS', 'UAH', 'CZK', 'SEK', 'CHF', 'ZAR', 'KRW', 'JPY'])
def get_valute(message):
    """get valute"""
    global msg_ids, valute

    if not valute:
        bot.send_message(message.chat.id,
                         f"Сначала необходимо запустить команду /valute")

    command = message.text.replace('/', '')
    bot.send_message(message.chat.id, f"Текущий курс {valute[command]['CharCode']} = {str(valute[command]['Value'])}")
    msg_ids.append(message.message_id)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """save id of send message"""
    global msg_ids
    # bot.send_message(message.chat.id, message.message_id)
    msg_ids.append(message.message_id)


bot.infinity_polling()
