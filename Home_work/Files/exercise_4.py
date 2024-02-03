'''
Задание 4:
В многострочном текстовом файле prices.txt каждая строка с
помощью символа табуляции разделена на три колонки:
1 название товара,2. количество товара и 3. цена за 1 шт.Выведите общую
стоимость заказа с точностью до копеек.
'''


# Открываем файл для чтения
def get_total_price(order):
    with open(order, 'r', encoding="utf-8") as input_file:
        # Читаем строки из входного файла
        lines = input_file.readlines()
    total_price = 0
    # Проходим по всем строкам в файлы
    for item in lines:
        # разбиваем их по пробелу, берем второй элемент (цену), умножаем на первый (количество) и суммируем с итоговой ценой
        total_price += float(item.split('\t')[2]) * int(item.split('\t')[1])

    return total_price


print(get_total_price('prices.txt'))
