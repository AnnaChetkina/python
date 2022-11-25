# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет
def day_week(day):
    if day in (6, 7):
        return 'Выходной'
    elif day in (1, 5):
        return 'Будний'
    else:
        return 'Ошибка'


print('Задача 1:')
print(day_week(5))
print(day_week(6))
print(day_week(90))
print(day_week('day'))
print(day_week(0))

# Напишите программу для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬ - Отрицание ⋁ - логическое "Или" ⋀ - логическое "И"
print()
print('Задача 2:')
x_l = [True, False]
y_l = [True, False]
z_l = [True, False]
for x in x_l:
    for y in y_l:
        for z in z_l:
            print(x, y, z)
            res1 = not(x or y or z)
            res2 = not x and not y and not z
            print(f'Для значений предикат x={x}, y={y}, z={z} утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z {res1 == res2}')



# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти
# плоскости, в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 2
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3
def get_quarter(x, y):
    if x == 0 or y == 0:
        return 'Не выполняется условие X ≠ 0 и Y ≠ 0'
    if x > 0 and y > 0:
        return '1'
    if x > 0 and y < 0:
        return '2'
    if x < 0 and y < 0:
        return '3'
    if x < 0 and y > 0:
        return '4'

print()
print('Задача 3:')
print(get_quarter(34, -30))
print(get_quarter(2, 4))
print(get_quarter(-34, -30))
print(get_quarter(0, -30))

# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print()
print('Задача 4:')
coordinates = {
    1: 'x > 0 and y > 0',
    2: 'x > 0 and y < 0',
    3: 'x < 0 and y < 0',
    4: 'x < 0 and y > 0'
}


def get_coordinates(quarter):
    return coordinates[quarter]


print(get_coordinates(1))
print(get_coordinates(4))

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
print()
print('Задача 5:')


def distance(a_x, a_y, b_x, b_y):
    d = ((b_x - a_x) ** 2 + (b_y - a_y) ** 2) ** 0.5
    print(round(d, 2))


distance(3, 6, 2, 1)
distance(7, -5, 1, -1)