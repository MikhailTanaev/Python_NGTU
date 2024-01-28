'''
Задание 6
Даны два списка целых чисел одинаковый длины. Например [5,4,3] и [2,1,3].
Сформировать третий список полученный путем нахождения разницы между списками,
например [5-2, 4-1,3-3] итоговый список [3,3,0]. Формирование третьего списка
осуществляется с использованием функции
'''

import random


def generate_random_int_list(length):
    random_list = []
    for i in range(length):
        random_list.append(random.randint(1, 3))
    return random_list


def subtract_lists(list_1, list_2):
    new_list = []
    for i in range(len(list_1)):
        new_list.append(list_1[i] - list_2[i])
    return new_list


list_1 = [5, 4, 3, 2, 1]
list_2 = [1, 2, 3, 4, 5]

print(subtract_lists(list_1, list_2))
