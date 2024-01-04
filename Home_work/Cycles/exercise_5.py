'''
Задание 5:
Написать программу. Пользователь вводит два числа. Данные числа
определяют числовой диапазон, для которого надо найти все числа, которые делятся
нацело на 3, 5, 9 Например диапазон 1 - 20, количество чисел, которые делятся на 3 – 6, 5
– 4, 9 - 2 Важно учесть, что пользователь может ввести числа в обратном порядке,
например 37 и 16
'''

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
range_of_numbers = range(0)

if num1 < num2:
    range_of_numbers = range(num1, num2 + 1)
else:
    range_of_numbers = range(num2, num1 + 1)


def get_count_of_divisible_numbers(divident_range, divider):
    count = 0
    for i in divident_range:
        if i % divider == 0:
            count += 1
    return count


print('Чисел делищяхся на 3:', get_count_of_divisible_numbers(range_of_numbers, 3))
print('Чисел делищяхся на 5:', get_count_of_divisible_numbers(range_of_numbers, 5))
print('Чисел делищяхся на 9:', get_count_of_divisible_numbers(range_of_numbers, 9))
