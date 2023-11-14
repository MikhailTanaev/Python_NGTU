'''
Задача 4.
Поменять местами самый большой и самый маленький элементы списка
'''

import random

randomList = []
# в цикле 10 раз генерируем случайное число в диапазоне от 1 до 100
for i in range(10):
    randomList.append(random.randint(1, 100))
print('Случайный список:', randomList)

# находим максимальное и минимальное значение
maxValue = max(randomList)
print('Максимальное значение:',maxValue)
minValue = min(randomList)
print('Минимальное значение:',minValue)
# охраняем индексы максимального и минимального значения
maxValueIndex = randomList.index(maxValue)
minValueIndex = randomList.index(minValue)
# минимальное значение записываем по индексу максимального
randomList[maxValueIndex] = minValue
# максимальное значение записываем по индексу минимального
randomList[minValueIndex] = maxValue
# выводим обновленный список
print('Обновленный список:', randomList)

