import math
import random

import sympy
from sympy import simplify

# 1) 10-9 округление до этого числа
# 2) число делим на что без остатка, из делителей можно получить уникальные, если перевести в сэт (множество),
# метод sympy
# 3) используем сэт, и дополнительно лист чтобы упорядочить массив/ лист компрехеншенс
#
# 4) рэндж с 3 параметрами?
# 5) обратить внимание на склеивание полиномов, чтобы они сложились по числам правильно! ф-ция simplify сложит
#
# 1'. Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415


def get_pi():
    accuracy = input('Введите требуемую точность: ')
    accuracy_len = len(accuracy) - 2
    res_pi = format(math.pi, f'.{accuracy_len}f')
    print(res_pi)
# get_pi()


# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

def prime_factors(n):
    prime_factors = []
    i = 2
    while i**2 <= n:
        if n % i == 0:
            prime_factors.append(i)
            n = n / i
        else:
            i += 1
    if (n > 1):
        prime_factors.append(int(n))
    print(set(prime_factors))
# prime_factors(6)
# prime_factors(63)

# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def non_repeating_values(values_count, values_range):
    init_list = [random.randint(0, values_range) for elem in range(0, values_count)]
    res_list = list(set(init_list))
    return res_list
# print(non_repeating_values(10, 10))

# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
def generate_polynom(k):
    coefficients = [random.randint(0, 100) for elem in range(0, k + 1)]
    print('coefficients', coefficients)
    eq = ''
    for i in range(0, len(coefficients) - 1):
        eq += f'{coefficients[i]}*x**{k - i}+'
    eq += f'{coefficients[-1]}'
    # eq = sympy.simplify(eq)
    print(eq)
    x = sympy.Symbol('x')
    solutions = sympy.solve(eq, x)
    print(solutions, ' = solution')
    return eq
print('Task 4')
generate_polynom(2)

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9
#
# expr1 = "90*x**2+60*x**1+100"
# expr2 = "10*x**2+40*x**1"

expr1 = generate_polynom(2)
expr2 = generate_polynom(3)

smpl = sympy.simplify(expr1 + "+" + expr2)
print("After Simplification : {}".format(smpl))