# Задача: предложить улучшения кода для уже решённых задач:
#
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension
# (выбрать 3 любые)

# (ДЗ2)
# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
import math


def get_list(n):
    res_list = []
    a = 1
    for i in range(1, n + 1):
        el = a * i
        res_list.append(el)
        a *= i
    print(f'Набор произведений чисел от 1 до {n} = {res_list}')


def get_list_refactored(n):
    print(f'Набор произведений чисел от 1 до {n} = {[math.factorial(el) for el in range(1, n + 1)]}')


get_list(6)
get_list_refactored(6)
print()

# (ДЗ2)
def fill_list(n):
    init_list = []
    for i in range(-n, n + 1):
        init_list.append(i)
    print(f'Список, заполненный числами из промежутка [-{n}, {n}] = {init_list}')
    return init_list

def fill_list_refactored(n):
    print(f'Список, заполненный числами из промежутка [-{n}, {n}] = {[el for el in range(-n, n + 1)]}')

fill_list(5)
fill_list_refactored(5)
print()

# (СЕМИНАР 5)
# Напишите программу, удаляющую из текста все слова, содержащие "абв".
# *' 'абвгд гдежз жзе абв ыопыпт' -> ' гдежз жзе ыопыпт'
def del_word(string, find_str):
    list_string = string.split()
    new_list = []
    for s in list_string:
        if s.find(find_str) == -1:
            new_list.append(s)
    print(" ".join(new_list))

def del_word_refactored(string, find_str):
    print(" ".join(list(filter(lambda el: el if el.find(find_str) == -1 else '', string.split()))))

del_word('абвгд гдеабвжз жзе абв ыопыпт шофабва', "абв")
del_word_refactored('абвгд гдеабвжз жзе абв ыопыпт шофабва', "абв")
print()

# (ДЗ3)
# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])


def mult_pairs(l):
    res = []
    for ind in range(0, math.ceil(len(l) / 2)):
        res.append(l[ind] * l[len(l) - 1 - ind])
    print(f'Произведение пар чисел списка {l} = {res}')

def mult_pairs_refactored(l):
    res = [(l[ind] * l[len(l) - 1 - ind]) for ind in range(0, math.ceil(len(l) / 2))]
    print(f'Произведение пар чисел списка {l} = {res}')

l1 = [2, 3, 4, 5, 6]
l2 = [2, 3, 5, 6]
mult_pairs(l1)
mult_pairs(l2)
mult_pairs_refactored(l1)
mult_pairs_refactored(l2)
