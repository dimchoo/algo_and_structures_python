"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.

Примечания ко всем задачам урока:
1.	Решите задачу при помощи линейного алгоритма или алгоритма с ветвлением (цикл и рекурсии будут на уроке 2 и тут их не используем для решения).
2.	Аналогично п. 1. массивы пройдём на уроке 3, поэтому постарайтесь решить задачи без них.
3.	Если речь идёт о символах, используйте только строчные буквы английского алфавита.
"""

import random


print('Случайное целое число.')
integer1 = int(input('Введите первое число диапазона: '))
integer2 = int(input('Введите второе число диапазона: '))

if integer1 < integer2:
    random_integer = random.randint(integer1, integer2)
    print(f'Случайное целое число в диапазоне от {integer1} до {integer2} включительно:\n'
          f'{random_integer}')
elif integer1 > integer2:
    random_integer = random.randint(integer2, integer1)
    print(f'Случайное целое число в диапазоне от {integer2} до {integer1} включительно:\n'
          f'{random_integer}')
else:
    print('Некорректный ввод!')


print('Случайное вещественное число.')
float1 = float(input('Введите первое число диапазона: '))
float2 = float(input('Введите второе число диапазона: '))

if float1 < float2:
    random_float = random.random() * (float2 - float1) + float1
    print(f'Случайное вещественное число в диапазоне от {float1} до {float2}:\n'
          f'{round(random_float, 3)}')
elif float1 > float2:
    random_float = random.random() * (float1 - float2) + float2
    print(f'Случайное вещественное число в диапазоне от {float2} до {float1}:\n'
          f'{round(random_float, 3)}')
else:
    print('Некорректный ввод!')


print('Случайный символ.')
symbol1 = ord(input('Введите первый символ: '))
symbol2 = ord(input('Введите второй символ: '))

if symbol1 < symbol2:
    random_symbol = random.randint(symbol1, symbol2)
    print(f'Случайный символ в диапазоне от {chr(symbol1)} до {chr(symbol2)}:\n'
          f'{chr(random_symbol)}')
elif symbol1 > symbol2:
    random_symbol = random.randint(symbol2, symbol1)
    print(f'Случайный символ в диапазоне от {chr(symbol2)} до {chr(symbol1)}:\n'
          f'{chr(random_symbol)}')
else:
    print('Некорректный ввод!')
