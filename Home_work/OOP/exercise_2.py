'''
Задание 2
Написать класс – списки целых чисел. Учитывая следующие
рекомендации:
- создайте метод __init__(), внутри которого будут определен один параметр: размер
списка. Начальные значения свойства берутся из входных параметров метода.
создайте метод InputData позволяющий задать данные списка пользователем
создайте метод InputDataRandom заполняющий список с помощью датчика
случайных чисел.
создайте метод print() – вывод на экран содержимого списка.
создайте метод FindValue - который возвращает список индексов для
искомого элемента.
создайте метод DelValue - который удаляет из списка искомый элемент.
создайте метод FindMax- который возвращает максимальное значение из
списка.
'''

import random
class ListOfInt:
    def __init__(self, lenght):
        self.length = lenght
        self.items = []

    def input_data_manual(self):
        print('Enter numbers:')
        for i in range(self.length):
            self.items.append(int(input()))

    def input_data_random(self, min_value=0, max_value=100):
        for i in range(self.length):
            self.items.append(random.randint(min_value, max_value))


    def print_data(self):
        print('List of items: ', self.items)

    def find_index_by_value(self):
        item = int(input('Enter number to find: '))
        list = []
        for i in range(self.length):
            if self.items[i] == item:
                list.append(i)
        return list

    def delete_item_by_value(self):
        value = int(input('Enter number to delete: '))
        while value in self.items:
            self.items.remove(value)

    def find_max_value(self):
        return max(self.items)


# Проверяем работу
# Создаем экземпляр класса с указанной блинной
user_list = ListOfInt(5)
# Вводим вручную элементы списка
user_list.input_data_manual()
# Печатаем элементы списка
user_list.print_data()
# Находим все индексы по значению
print('All indexes: ', user_list.find_index_by_value())
# Удаляем все элементы равные нужному значению
user_list.delete_item_by_value()
# Печатаем элементы списка
user_list.print_data()
# Находим максимальное значение
print('Max value: ', user_list.find_max_value())
# Создаем экземпляр класса с указанной блинной
random_list = ListOfInt(20)
# Генерируем случайный список
random_list.input_data_random(-100, 100)
# Печатаем элементы списка
random_list.print_data()


