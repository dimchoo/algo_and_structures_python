"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""


# Решение с помощью рекурсии


def reverse_number(number, reversed_num=''):
    reversed_number = reversed_num
    one_number = int(number) % 10
    new_number = int(number) // 10

    if new_number == 0:
        reversed_number += str(one_number)
        print(reversed_number)
        return
    else:
        reversed_number += str(one_number)
        return reverse_number(new_number, reversed_number)


user_number = input('Введите число: ')

reverse_number(user_number)


# Решение с помощью цикла

user_number = input('Введите число: ')

reversed_number = ''

for i in user_number:
    reversed_number = f'{i}{reversed_number}'

print(reversed_number)
