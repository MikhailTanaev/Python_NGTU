
import random
''' Задание:
Пользователь вводит кол-во чисел, которое надо сгенерировать в диапазоне от 1 до 1000 (например 10)
1. Сгенерировать заданное колличество чисел
2. Найти максимум среди сгенерированных чисел
3. Найти минимум среди сгенерированных чисел
4. Найти среднее среди сгенерированных чисел
5. Найти количество четных чисел среди сгенерированных чисел
6. Найти количество нечетных чисел среди сгенерированных чисел
'''
# Считываем введенное в консоли число
number = int(input("Enter number:"))
# Создаем пустой список
listNumbers =[]
# В цикле генерируем данные и записываем их в список
i = 0
while i < number:
    listNumbers.append(random.randint(1,1000))
    i = i+1
print('List of numbers:', listNumbers)
# Используем встроеноую функцию для получения минимального значения
print('Min value:',min(listNumbers))
# Используем встроеноую функцию для получения максимального значения
print("Max value:", max(listNumbers))
# Используем встроеноую функцию для получения суммы всех элементов
print('Summ of elements:', sum(listNumbers))
# Считаем среднее значение
print('Average:', sum(listNumbers)/number)

# Считаем количество четных и нечетных чисел в списке.
# Для этого используем функцию % (остаток от деления). Если остаток 0 - значит число было четное.
oddNumberCount = 0
evenNumberCount = 0
for i in listNumbers:
    if i % 2 == 0:
        evenNumberCount = evenNumberCount + 1
    else:
        oddNumberCount = oddNumberCount + 1

print('Even numbers:', evenNumberCount)
print('Odd numbers:', oddNumberCount)

