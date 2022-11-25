# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11
def f(num):
    string = str(num)
    string = string.replace('.', '')
    summa = 0
    for n in string:
        summa = summa + int(n)
    print(summa)
# f(6782)
# f(0.56)
# f(999.111)

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)
def get_list(n):
    res_list = []
    a = 1
    for i in range(1, n + 1):
        el = a * i
        res_list.append(el)
        a *= i
    return res_list
print()
# print(get_list(4))

# Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
# Пример:
# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]

def get_list_sum(n):
    res = []
    summa = 0
    for i in range(1, n + 1):
        res.append((1+1/i)**i)
    summa = sum(res)
    print(f'Список = {res}, сумма {summa}')
get_list_sum(6)


# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.(для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2
#positions.txt
def read_file(n):
    res = []
    for i in range(-n, n + 1):
        res.append(i)
    print(res)
    f = open('positions.txt','r')
    l = f.readlines()
    # s = ''.join(l)
    print(l)
    print(res[int(l[0])])
    print(res[int(l[1])])
    print(res[int(l[2])])
    f.close()
read_file(5)

# Реализуйте алгоритм перемешивания списка.