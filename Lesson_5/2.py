"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

user_hex_number1 = list(deque(input('Введите 1 шестнадцатеричное число: ').upper()))
user_hex_number2 = list(deque(input('Введите 2 шестнадцатеричное число: ').upper()))

hex_number1 = ''
hex_number2 = ''

for i in user_hex_number1:
    hex_number1 += i

for i in user_hex_number2:
    hex_number2 += i

sum_str = (hex(int(hex_number1, 16) + int(hex_number2, 16)).upper())[2:]
product_str = (hex(int(hex_number1, 16) * int(hex_number2, 16)).upper())[2:]

print(f'Сумма {user_hex_number1} и {user_hex_number2}:\n'
      f'{list(deque(sum_str))}\n'
      f'Произведение {user_hex_number1} и {user_hex_number2}:\n'
      f'{list(deque(product_str))}')


