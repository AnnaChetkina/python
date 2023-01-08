# Добавить игру, реализованную ранее, с конфетами к боту.
# *' Условие игры: На столе лежит 117 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.


import telebot
import random


bot = telebot.TeleBot("5732636743:AAH2Aw00pm_z2BwUsGyl1ZkT8JnkY3FzFRA")

candies = 117
max_candies_in_move = 28


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "/help\n/del\n/game")


@bot.message_handler(commands=['del'])
def add_letters(message):
    """/del any txt"""
    res_msg = message.text.replace('/del', '')
    res_msg = res_msg.replace('абв', '')
    bot.reply_to(message, res_msg)


@bot.message_handler(commands=['game'])
def game_init(message):
    bot.delete_message(message.chat.id, message.message_id - 1)
    msg = bot.send_message(message.chat.id, 'Введите кол-во конфет')
    bot.register_next_step_handler(msg, move)


def move(message):
    global candies, max_candies_in_move

    candies = candies - int(message.text)
    bot.reply_to(message, f'Осталось конфет {candies}')
    if candies <= max_candies_in_move:
        bot.send_message(message.chat.id, f'Победил {message.from_user.first_name}, он забирает последние конфеты ({candies} шт.) ')
        return

    bot_move = random.randint(1, max_candies_in_move)
    bot_msg = bot.send_message(message.chat.id, f'Я взял {bot_move} конфет')
    candies -= bot_move
    bot.reply_to(bot_msg, f'Осталось конфет {candies}')
    if candies <= max_candies_in_move:
        bot.send_message(message.chat.id, f'Победил БОТ, он забирает последние конфеты ({candies} шт.) ')
        return

    if candies >= max_candies_in_move:
        msg = bot.send_message(message.chat.id, 'Введите кол-во конфет')
        bot.register_next_step_handler(msg, move)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    """any txt"""
    bot.reply_to(message, message.text)


bot.infinity_polling()
