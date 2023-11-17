'''
Задача 1.
Напишите программу, которая запрашивает у пользователя три числа в диапазоне 1-1000.
Компьютер генерирует два случайных числа в диапазоне 1-100, которые определяют отрезок.
Определить какие  числа указанные пользователям попали в отрезок.
'''

import random

userList = []
for i in range(3):
     userList.append(int(input('Введите целое число от 0 до 1000: ')))

print('Список пользователя',userList)

compList = []
for i in range(2):
    compList.append(random.randint(1, 100))
print('Список компьютера',compList)

compList.sort()

for elem in userList:
    if elem >= compList[0] and elem <= compList[1]:
        print('Число', elem, 'входит в диапазон')






