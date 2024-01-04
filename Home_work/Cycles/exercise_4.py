'''
Задание 4:
Написать программу – игра - угадай, в которой с помощью функции random
генерируется случайное число от 1 до 50 Пользователю предлагается угадать данное
число, на основе подсказать – загаданное число больше или меньше числа пользователя.
Вывести число попыток отгадывания числа
'''
import random


random_number = random.randint(1, 50)
# Инициализируем переменные
guess = False
attempts = 0

# Проверяем до тех пор, пока пользователь не угадает число
while guess == False:
    # каждый раз увеличиваем число попыток
    attempts += 1
    # добавляем try на случай если будет введено не число
    try:
        user_number = int(input('Enter your guess: '))

        if random_number == user_number:
            guess = True
            print(f'Bingo! You needed {attempts} attempts')
        else:
            if user_number < random_number:
                print('Your number is less')
            else:
                print('Your number is more')

    except ValueError:
        print('You should enter number only')