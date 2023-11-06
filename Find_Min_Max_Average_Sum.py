
import random
# юзер вводит кол-во чисел, например 10
# компьютер генерирует случайное число от 1 до 1000
# надо найти максимум среди сгенерированных чисел
# надо найти минимум среди сгенерированных чисел
# надо найти среднее среди сгенерированных чисел
# надо найти колличество четных чисел среди сгенерированных чисел
# надо найти колличество нечетных чисел среди сгенерированных чисел

number = int(input("Enter number:"))
listNumbers =[]
i = 0
while i < number:
    listNumbers.append(random.randint(1,1000))
    i = i+1
print('List of numbers:', listNumbers)
print('Min value:',min(listNumbers))
print("Max value:", max(listNumbers))
print('Summ of elements:', sum(listNumbers))

print('Average:', sum(listNumbers)/number)

oddNumberCount = 0
evenNumberCount = 0
for i in listNumbers:
    if i % 2 == 0:
        evenNumberCount = evenNumberCount + 1
    else:
        oddNumberCount = oddNumberCount + 1

print('Even numbers:', evenNumberCount)
print('Odd numbers:', oddNumberCount)

