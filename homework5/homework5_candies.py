import random


# 1. Создайте программу для игры с конфетами человек против человека.
# *' Условие задачи: На столе лежит 117 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.

def player1_move(candies):
    candies = move('ИГРОК 1', candies)
    if candies <= 28:
        print(f'Победил ИГРОК 2, он забирает последние конфеты ({candies} шт.) ')
    return candies


def player2_move(candies):
    candies = move('ИГРОК 2', candies)
    if candies <= 28:
        print(f'Победил ИГРОК 1, он забирает последние конфеты ({candies} шт.) ')
    return candies

def bot_move(candies):
    candies = move('БОТ', candies)
    if candies <= 28:
        print(f'Победил ИГРОК, он забирает последние конфеты ({candies} шт.) ')
    return candies

def human_move(candies):
    candies = move('ИГРОК', candies)
    if candies <= 28:
        print(f'Победил БОТ, он забирает последние конфеты ({candies} шт.) ')
    return candies

#
# def move(player: str, candies: int) -> int:
#     max_candies_in_move = 28
#     try:
#         player_move = int(input(f'{player} берет конфеты (не более 28 шт):'))
#         while player_move not in range(0, max_candies_in_move + 1):
#             player_move = int(input('Введите корректное количество конфет (не более 28 шт):'))
#         candies -= player_move
#     except ValueError as e:
#         print('Это не число.', e.args)
#         return
#     return candies

def move(player: str, candies: int) -> int:
    max_candies_in_move = 28
    player_move = int(input(f'{player} берет конфеты (не более 28 шт):'))
    while player_move not in range(0, max_candies_in_move + 1):
        player_move = int(input('Введите корректное количество конфет (не более 28 шт):'))
    candies -= player_move
    return candies


def candies_game():
    candies = 117
    first_move_player = random.randint(1, 2)
    print(f'Первый ход у ИГРОКА {first_move_player}')
    while candies >= 28:
        if first_move_player == 1:
            candies = player1_move(candies)
            candies = player2_move(candies)
        else:
            candies = player2_move(candies)
            candies = player1_move(candies)
        print('Осталось конфет в этом ходу', candies)


# candies_game()


# a) Добавьте игру против бота

def candies_with_bot():
    candies = 117
    players = {1: 'ИГРОК', 2: 'БОТ'}
    first_move_player = random.randint(1, 2)
    print(first_move_player)
    print(f'Первым ходит {players[first_move_player]}')
    while candies >= 28:
        if first_move_player == 1:
            candies = human_move(candies)
            candies = bot_move(candies)
        else:
            candies = bot_move(candies)
            candies = human_move(candies)
        print('Осталось конфет в этом ходу', candies)
candies_with_bot()
# 2. Создайте программу для игры в ""Крестики-нолики"".(в консоли происходит выбор позиции)
