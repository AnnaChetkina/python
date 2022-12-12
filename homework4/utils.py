import random
import sympy


def generate_values(values_count: int, values_range: int) -> list:
    """ Фунуция вернет список коэффициентов длиной values_count,
    каждый коэффициент генерируется случайным образом в диапазоне от 0 до values_range"""
    return [random.randint(0, values_range) for elem in range(0, values_count)]

def generate_polynom(k: int) -> str:
    """ Фунуция вернет полином с сгенерированными коэффициентами"""
    coefficients = generate_values(k + 1, 100)
    print('Коэффициенты', coefficients)
    eq = ''
    for i in range(0, len(coefficients) - 1):
        eq += f'{coefficients[i]}*x**{k - i}+'
    eq += f'{coefficients[-1]}'
    return eq

def solve_polynom(polynom: str):
    """ Фунуция решит уравнение polynom и напечатает решение"""
    x = sympy.Symbol('x')
    solution = sympy.solve(polynom, x)
    print(f'Решение уравнения {solution}')


def write_to_file(text: str, file_name: str):
    """ Фунуция откроет существующий файл и перезапишет в нем текст"""
    with open(file_name, 'w') as data:
        data.write(text)

def read_from_file(file_name: str):
    """ Фунуция откроет существующий файл и прочитает из него текст"""
    with open(file_name, 'r') as data:
        file_content = data.read()
    return file_content
