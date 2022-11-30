import math

# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
l = [2, 3, 5, 9, 3, 8]


def odd_el_sum(l):
    summa = 0
    for ind in range(0, len(l)):
        if ind % 2 == 1:
            summa += l[ind]
    print(summa)

print('Задача 1:')
odd_el_sum(l)

# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

# *Пример:*
# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5])

l1 = [2, 3, 4, 5, 6]
l2 = [2, 3, 5, 6, 2]


def mult_pairs(l):
    res = []
    for ind in range(0, math.ceil(len(l) / 2)):
        res.append(l[ind] * l[len(l) - 1 - ind])
    print('res', res)


mult_pairs(l1)
print()
mult_pairs(l2)


# 3'. Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
def get_truncate(elem):
    el = str(elem)
    dot_ind = el.find('.')
    if dot_ind == -1:
        str_res = '0.0'
    else:
        str_res = '0' + el[dot_ind:]
    return float(str_res)


l3 = [1.1, 1.2, 3.1, 5.9, 10.01]


def fn_diff(l):
    res = list(map(get_truncate, l))
    # min_el = min(list.copy(res))
    # max_el = max(list.copy(res))
    diff = max(list.copy(res)) - min(list.copy(res))
    # print(min_el, max_el, diff)
    print(diff)


print()
fn_diff(l3)


# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def get_binary(num, res: str):
    # print(num, res)
    if num == 1:
        return '1' + res
    else:
        res = str(num % 2) + res
    return get_binary(int(num / 2), res)


print()


# print(get_binary(15, ''))
# print(bin(15))

# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fib(num):
    res = []
    i = 0
    while i < num:
        # print(i, 'i')
        if i == 0 or i == 1:
            res.append(i)
        if i > 1:
            prev = (res[i - 2] + res[i - 1])
            res.append(prev)
        i += 1
    print(res, 'fib')
    return res


# fib(11)

def negative_fib(fibb):
    # print('вход в функцию negative_fib', fibb)
    # neg_fibb = list.copy(fibb)
    neg_fibb = fibb[:]
    for i in range(1, len(fibb)):
        # print(((-1)**i), 'множитель')
        # print(fibb[i], 'fibb[i]')
        neg_fibb[i] = ((-1) ** (i + 1)) * fibb[i]
    # print(neg_fibb[::-1], 'neg')
    neg_fibb.remove(0)
    return neg_fibb[::-1]


# negative_fib(fib(11))

# def join_fib_lists(fib(11), negative_fib(fib)):
def join_fib_lists(fib, negative_fib):
    # print(fib, negative_fib, 'join')
    fib_list = [*negative_fib, *fib]
    print(fib_list, 'fib_list')


fibb1 = fib(11)
fibb2 = negative_fib(fibb1)
print('[−55, 34, −21, 13, −8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]', 'WIKI')

join_fib_lists(fibb1, fibb2)
