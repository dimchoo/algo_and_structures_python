"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


# Решение с помощью рекурсии


def row_sum(el_count, el_start=1, el_sum=0.0, el_row=''):
    if el_count != 0:
        el_sum = el_start + el_sum
        el_row = el_row + f'{el_start} '
        el_start /= -2
        el_count -= 1
        return row_sum(el_count, el_start, el_sum, el_row)
    else:
        print(f'Сумма элементов ряда: {el_row}= {el_sum}')


n = int(input('Введите количество элементов ряда: '))

row_sum(n)


# Решение с помощью цикла

n = int(input('Введите количество элементов ряда: '))

el_sum = 0
el_start = 1
el_row = ''


for i in range(n):
    el_sum += el_start
    el_row += f'{el_start} '
    el_start /= -2

print(f'Сумма элементов ряда: {el_row}= {el_sum}')
