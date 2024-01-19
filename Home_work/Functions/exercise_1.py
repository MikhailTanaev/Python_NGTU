'''
Задание 1 
Написать программу, которая последовательно вызывает три функции.
Функция 1 – подсчитывает для заданного отрезка чисел все числа, которые делятся нацело на 3,
функция 2 – подсчитывает для заданного отрезка чисел все числа, которые делятся нацело на 4,
Функция 3– подсчитывает для заданного отрезка чисел все числа, которые делятся нацело на 5
'''


def divided_on_3(section):
    divided = []
    for i in section:
        if i % 3 == 0:
            divided.append(i)
    print('Nummber devided to 3: ', divided)


def divided_on_4(section):
    divided = []
    for i in section:
        if i % 4 == 0:
            divided.append(i)
    print('Nummber devided to 4: ', divided)


def divided_on_5(section):
    divided = []
    for i in section:
        if i % 5 == 0:
            divided.append(i)
    print('Nummber devided to 5: ', divided)

# CHECK


segment = range(0, 101)
divided_on_3(segment)
divided_on_4(segment)
divided_on_5(segment)