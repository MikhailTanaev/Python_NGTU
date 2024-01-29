'''
Задание 2:
Файл article.txt содержит тест. Требуется реализовать функцию longest_words(file), которая выводит
слово, имеющее максимальную длину (или список слов, если таковых несколько).
'''


# Открываем файл для чтения
def longest_words(filename):
    with (open(filename, 'r', encoding="utf-8") as file):
        # Считываем слова из файла и преобразуем их в список
        words = []
        for word in file.read().split():
            # если список пустой, добавляем туда слово
            if len(words) == 0:
                words.append(word)
            # если следующее слово равно по длинне с уже записаным, его тоже добавляем
            elif len(word) == len(words[0]):
                words.append(word)
            # если следующее слово длинне тех, что есть списке, то очищаем его и добавляем туда слово
            elif len(word) > len(words[0]):
                words.clear()
                words.append(word)

    return words


print(longest_words('article.txt'))
