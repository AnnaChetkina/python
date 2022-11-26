import random

# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

print('Задача 1')


def get_digits_sum(num):
    string = str(num)
    string = string.replace('.', '')
    summa = 0
    for n in string:
        summa = summa + int(n)
    print(f'Сумма цифр числа {num} = {summa}')


get_digits_sum(6782)
get_digits_sum(0.56)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
print()
print('Задача 2')


def get_list(n):
    res_list = []
    a = 1
    for i in range(1, n + 1):
        el = a * i
        res_list.append(el)
        a *= i
    print(f'Набор произведений чисел от 1 до {n} = {res_list}')


get_list(4)

# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]
print()
print('Задача 3')


def get_list_sum(n):
    res = []
    summa = 0
    for i in range(1, n + 1):
        res.append((1 + 1 / i) ** i)
    summa = sum(res)
    print(f'Список = {res}')
    print(f'Сумма элементов списка {summa}')


get_list_sum(6)

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
print()
print('Задача 4')


def read_file1(n):
    init_list = fill_list(n)
    pos_list = read_file()
    max_pos = max(pos_list)
    if len(init_list) <= max_pos:
        print('Нельзя посчитать произведение элементов, т.к. максимальная позиция больше длины массива')
        return
    mult = 1
    for pos in pos_list:
        print(f'Элемент на позиции {pos} = {init_list[pos]}')
        mult *= init_list[pos]
    print(f'Произведение элементов на позициях {pos_list} = {mult}')


def fill_list(n):
    init_list = []
    for i in range(-n, n + 1):
        init_list.append(i)
    print(f'Список, заполненный числами из промежутка [-{n}, {n}] = {init_list}')
    return init_list


def read_file():
    file = open('positions.txt', 'r')
    pos_list = file.readlines()
    pos_list = list(map(int, pos_list))
    file.close()
    return pos_list


read_file1(5)

# Реализуйте алгоритм перемешивания списка.
print()
print('Задача 5')
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f'Исходный список = {init_list}')


def mix_list(init_list):
    mixed_list = []
    used_pos_list = []
    for el in init_list:
        rand_pos = random.randint(0, len(init_list) - 1)
        while rand_pos in used_pos_list:
            rand_pos = random.randint(0, len(init_list) - 1)
        mixed_list.append(init_list[rand_pos])
        used_pos_list.append(rand_pos)
        # print(used_pos_list, 'used_pos_list')
    print(f'Перемешанный список = {mixed_list}')


mix_list(init_list)
