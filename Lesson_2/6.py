"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""

# Решение с помощью рекурсии

import random

random_number = int(random.random() * (100 + 1))


def guess_number(number, attempts=10):
    if attempts == 0:
        print(f'К сожалению количество попыток закончилось!'
              f'Загаданное число: {number}.')
        return

    user_number = int(input('Угадайте число от 0 до 100: '))

    if number < user_number:
        print(f'Загаданное число меньше числа {user_number}!')
        attempts -= 1
        return guess_number(number, attempts)
    elif number > user_number:
        print(f'Загаданное число больше числа {user_number}!')
        attempts -= 1
        return guess_number(number, attempts)
    else:
        attempts -= 1
        print(f'Поздравляю! Вы угадали число "{number}" с {10 - attempts} попытки!')


guess_number(random_number)

# Решение с помощью цикла

attempts = 0
random_number = int(random.random() * (100 + 1))

while attempts < 10:
    user_number = int(input('Угадайте число от 0 до 100: '))
    attempts += 1
    print(random_number)

    if random_number < user_number:
        print(f'Загаданное число меньше числа {user_number}!')
    elif random_number > user_number:
        print(f'Загаданное число больше числа {user_number}!')
    else:
        print(f'Поздравляю! Вы угадали число "{user_number}" с {attempts} попытки!')
        break

    if attempts == 10:
        print(f'К сожалению количество попыток закончилось!'
              f'Загаданное число: {random_number}.')
