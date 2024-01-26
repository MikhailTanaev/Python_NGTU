'''
Задание 4
Дан список целых чисел. Посчитать, сколько раз в нем встречается каждое
число. Например, если дан список [1, 1, 3, 2, 1, 3, 4], то в нем число 1 встречается три раза,
число 3 - два раза, числа 2 и 4 - по одному разу.
'''

import random


def generate_random_int_list(length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(1, 3))
    return random_list


def count_occurrences(numbers):
    # создаем словарь в который будем записывать число : сколько раз встречается
    occurrences = {}
    # проходим по списку чисел
    for number in numbers:
        # если число входит в словарь то увеличиваем его количество в финальном списке
        if number in occurrences:
            occurrences[number] += 1
        # если этого чтсла нет в финальном списке, то добавляем его со значением 1
        else:
            occurrences[number] = 1

    return occurrences


# Замените 10 на желаемую длину списка
random_int_list = generate_random_int_list(10)
# печатаем список
print(random_int_list)

 # создаем словарь
occurrences = count_occurrences(random_int_list)
# печатаем список
for number, count in occurrences.items():
    print(f"Число {number} встречается {count} раз(а)")
