import random
from utils import player1_move, player2_move, human_move, bot_move, max_candies_in_move
candies_amount = 117

def candies_game():
    candies = candies_amount
    first_move_player = random.randint(1, 2)
    print(f'Первый ход у ИГРОКА {first_move_player}')
    while candies >= max_candies_in_move:
        if first_move_player == 1:
            candies = player1_move(candies)
            candies = player2_move(candies)
        else:
            candies = player2_move(candies)
            candies = player1_move(candies)
        print('Осталось конфет в этом ходу', candies)


# candies_game()
print()


# a) Добавьте игру против бота

def candies_with_bot():
    candies = candies_amount
    players = {1: 'ИГРОК', 2: 'БОТ'}
    first_move_player = random.randint(1, 2)
    print(f'Первым ходит {players[first_move_player]}')
    while candies >= max_candies_in_move:
        if first_move_player == 1:
            candies = human_move(candies)
            candies = bot_move(candies)
        else:
            candies = bot_move(candies)
            candies = human_move(candies)
        print('Осталось конфет в этом ходу', candies)


candies_with_bot()
