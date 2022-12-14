import random

max_candies_in_move = 28

def player1_move(candies):
    candies = move('ИГРОК 1', candies)
    if candies <= max_candies_in_move:
        print(f'Победил ИГРОК 2, он забирает последние конфеты ({candies} шт.) ')
    return candies


def player2_move(candies):
    candies = move('ИГРОК 2', candies)
    if candies <= max_candies_in_move:
        print(f'Победил ИГРОК 1, он забирает последние конфеты ({candies} шт.) ')
    return candies


def bot_move(candies):
    candies = move('БОТ', candies)
    if candies <= max_candies_in_move:
        print(f'Победил ИГРОК, он забирает последние конфеты ({candies} шт.) ')
    return candies


def human_move(candies):
    candies = move('ИГРОК', candies)
    if candies <= max_candies_in_move:
        print(f'Победил БОТ, он забирает последние конфеты ({candies} шт.) ')
    return candies


def move(player: str, candies: int) -> int:
    if player == 'БОТ':
        player_move = random.randint(1, 28)
        print(f'{player} взял {player_move} шт.')
    else:
        player_move = int(
            input(f'{player} берет конфеты (не более {max_candies_in_move} шт):')
        )
        while player_move not in range(0, max_candies_in_move + 1):
            player_move = int(
                input(f'Введите корректное количество конфет (не более {max_candies_in_move} шт):')
            )
    candies -= player_move
    return candies
