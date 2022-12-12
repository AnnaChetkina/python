import math
import sympy
from sympy import simplify

from utils import generate_values, \
    generate_polynom, \
    solve_polynom, \
    write_to_file, \
    read_from_file

# 1'. Вычислить число Пи c заданной точностью d
# *Пример:*
# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415
print('Задача № 1')


def get_pi():
    accuracy = input('Введите требуемую точность: ')
    accuracy_len = len(accuracy) - 2
    res_pi = format(math.pi, f'.{accuracy_len}f')
    print(f'Пи = {res_pi}')


# get_pi()
print()

# 2'. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]
print('Задача № 2')


def prime_factors(n):
    init_n = n
    prime_factors = []
    i = 2
    while i ** 2 <= n:
        if n % i == 0:
            prime_factors.append(i)
            n = n / i
        else:
            i += 1
    if (n > 1):
        prime_factors.append(int(n))
    print(f'Уникальные простые множители числа {init_n} = {set(prime_factors)}')


prime_factors(6)
prime_factors(63)
print()

print('Задача № 3')


# 3'. Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов исходной последовательности.

def non_repeating_values(values_count, values_range):
    init_list = generate_values(values_count, values_range)
    return f'Список неповторяющихся элементов исходной последовательности {list(set(init_list))}'


print(non_repeating_values(10, 10))
print()

# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0

print('Задача № 4')


def create_polynom_in_file(k, file_name):
    eq = str(sympy.simplify(generate_polynom(k)))
    print(f'Сгенерированный многочлен {eq}')
    # solve_polynom(eq)
    write_to_file(eq, file_name)
    return eq


create_polynom_in_file(3, 'task4.txt')
print()

# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.
# В file1.txt :
# 2*x**2 + 4*x + 5
# В file2.txt:
# 4*x**2 + 1*x + 4
# Результирующий файл:
# 6*x**2 + 5*x + 9

print('Задача № 5')


def get_polynoms_sum(k1: int, k2: int):
    """Функция принимает степени многочленов, генерирует их записывает в файлы,
    затем читает многочлены из файлов, складывает и записывает в результирующий файл"""
    create_polynom_in_file(k1, 'polynom1.txt')
    create_polynom_in_file(k2, 'polynom2.txt')
    polynom1 = read_from_file('polynom1.txt')
    polynom2 = read_from_file('polynom2.txt')
    sum_polynom = sympy.simplify(polynom1 + "+" + polynom2)
    print("Сумма многочленов: {}".format(sum_polynom))
    write_to_file(str(sum_polynom), 'res_polynom.txt')


get_polynoms_sum(3, 4)
