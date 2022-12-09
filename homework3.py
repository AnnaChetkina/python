import math

# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
print('Задача 1:')

l = [2, 3, 5, 9, 3]


def odd_el_sum(l):
    # summa = 0
    # for ind in range(0, len(l)):
    #     if ind % 2 == 1:
    #         summa += l[ind]
    # print(f'Сумма элементов списка {l}, стоящих на нечётной позиции = {summa}')
    print(sum(l[1::2])) # последняя 2 в срезе означает, что мы идем через 2 элемента

odd_el_sum(l)
print()

# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])
print('Задача 2:')

l1 = [2, 3, 4, 5, 6]
l2 = [2, 3, 5, 6]


def mult_pairs(l):
    res = []
    for ind in range(0, math.ceil(len(l) / 2)):
        res.append(l[ind] * l[len(l) - 1 - ind])
    print(f'Произведение пар чисел списка {l} = {res}')

mult_pairs(l1)
mult_pairs(l2)
print()


# 3'. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

print('Задача 3:')
def get_truncate_list(elem):
    el = str(elem)
    dot_ind = el.find('.')
    if dot_ind == -1:
        str_res = '0.0'
    else:
        str_res = '0' + el[dot_ind:]
    return float(str_res)


def fn_diff(l):
    res = list(map(get_truncate_list, l))
    # diff = max(list.copy(res)) - min(list.copy(res))
    diff = max([*res]) - min([*res])
    print(f'Разница между максимальным и минимальным значением дробной части элементов списка {l} = {diff}')

l3 = [1.1, 1.2, 3.1, 5.9, 10.01]
fn_diff(l3)
print()


# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
print('Задача 4:')

def get_binary(num, res: str):
    # print(num, res)
    if num == 1:
        return '1' + res
    else:
        res = str(num % 2) + res
    return get_binary(int(num / 2), res)

num = 15
print(f"{num} = {get_binary(num, '')}")
print(f'{num} = {bin(15)[2:]} # Проверка через встроенную функцию ')
print()


# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

print('Задача 5:')
def fib(num):
    res = []
    i = 0
    while i < num:
        if i == 0 or i == 1:
            res.append(i)
        if i > 1:
            prev = (res[i - 2] + res[i - 1])
            res.append(prev)
        i += 1
    # print(res, 'fib')
    return res


def negafib(fib):
    neg_fib = [*fib]
    for i in range(1, len(fib)):
        neg_fib[i] = ((-1) ** (i + 1)) * fib[i]
    # print(neg_fib[::-1], 'neg')
    neg_fib.remove(0)
    return neg_fib[::-1]


def join_fib_lists(fib, negafib):
    fib_list = [*negafib, *fib]
    print(fib_list, 'fib_list')


fib1 = fib(11)
negafib1 = negafib(fib1)
print('[−55, 34, −21, 13, −8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]', 'WIKI')

join_fib_lists(fib1, negafib1)
