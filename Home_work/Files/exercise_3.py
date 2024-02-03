'''
Задание 3:
Напишите функцию reverse(in_file, out_file), которая читает
строки из файла in_file и создает файл out_file, куда сохраняет прочитанные
строки в обратном порядке.
'''


# Открываем файл для чтения
def reverse(in_file, out_file):
    with open(in_file, 'r', encoding="utf-8") as input_file:
        # Читаем строки из входного файла
        lines = input_file.readlines()
    # Записываем строки в обратном порядке
    lines.reverse()
    # Открываем выходной файл для записи
    with open(out_file, 'w', encoding="utf-8") as output_file:
        for line in lines:
            output_file.write(line)


reverse('example.txt', 'example_reversed.txt')
