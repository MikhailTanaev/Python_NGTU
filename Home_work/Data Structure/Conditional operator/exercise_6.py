'''
Задача 6.
Напишите программу, которая у пользователя запрашивает три числа определяющие стороны треугольника.
Определить тип треугольника: равнобедренный, равносторонний, прямоугольный, обычный
'''

# Считываем введенное в консоли число
a = int(input('Введите сторону А: '))
b = int(input('Введите сторону B: '))
c = int(input('Введите сторону C: '))
triangle = [a,b,c]
regular = True
#
if a == b and b == c:
    print('Треугольник равносторонний')
    regular = False
if a == b or b == c or a== c:
    print('Треугольник равнобедренный')
    regular = False
# отсортируем, чтоб найти гипотенузу
triangle.sort()
# в прямоугольном треугольнике квадрат гипотенузы равен сумме квадратов двух других сторон
if triangle[2]**2 == triangle[0]**2 + triangle[1]**2:
    print('Треугольник прямоугольный')
    regular = False
if regular:
    print('Треугольник обычный')
