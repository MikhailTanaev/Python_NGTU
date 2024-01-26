'''
Задание 5
Выполнить циклический сдвиг в списке целых чисел на указанное число шагов.
Сдвиг также должен быть кольцевым, то есть элемент, вышедший за пределы
списка, должен появляться с другого его конца.
'''


def move_position(base_list, shift):
    # создаем новый список такой же длинны
    new_list = [0] * len(base_list)
    # проходимся по нему
    for i in range(len(base_list)):
        # если сумма текущей позиции и смещения больше или равны длинне списка
        if i + shift >= len(base_list):
            # тогда вычитаем длинну списка из этой суммы
            new_list[i + shift - len(base_list)] = base_list[i]
        # если сумма текущей позиции и смещения меньше длинны списка
        elif i + shift < 0:
            # тогда прибавляем к этой сумме длинну списка
            new_list[i + shift + len(base_list)] = base_list[i]
        else:
            # иначе просто приравниваем
            new_list[i + shift] = base_list[i]

    return new_list


example = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(move_position(example, -3))
