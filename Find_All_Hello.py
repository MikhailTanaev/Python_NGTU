# Задание: посчитать все Hello
a = (5,'Hello', 2.3, True,[21,17,'Hello',35],'Hello', ('By', 'Hello'))
# Считаем сколько Hello у нас в кортеже без учета вложенных списков и кортежей
helloCount = a.count('Hello')
# Проходим в цикле по всем элементам и проверяем не является ли элемент списком/кортежем
for iter in a:
    # Если элемент является списком/кортежем, то считаем сколько в нем Hello и суммируем с найденым ранее
    if type(iter) == list or type(iter) == tuple:
        helloCount = helloCount + iter.count('Hello')

print('Hello найдено', helloCount, 'штуки')


