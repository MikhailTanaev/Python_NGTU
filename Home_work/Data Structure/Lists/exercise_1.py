'''
Задача 1.
Написать программу: дан список из 10 чисел,
которые задаются с помощью датчика случайных чисел в диапазоне 1-10.
Программа находит повторяющиеся элементы и удаляет их из списка.
Например, дан список (1,1,1,2,3,4,2,3,4) результат (1,2,3,4)
'''

import random
randomList = []
# в цикле 10 раз генерируем случайное число в диапазоне от 1 до 10
for i in range(10):
    randomList.append(random.randint(1, 10))
print('Случайным список:', randomList)

uniqList = []
# прохоимся по всем элемментам списка
for i in randomList:
# и если элемента нет в "уникальном" списке, то добавляем его туда
    if not i in uniqList:
        uniqList.append(i)

print('Уникальный список', uniqList)


