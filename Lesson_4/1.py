"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import timeit


# Алгоритм нахождения суммы n элементов, ряда чисел: 1 -0.5 0.25 -0.125 ...
# 1. Рекурсия

def row_sum_recursion(el_count, el_start=1, el_sum=0.0, el_row=''):
    if el_count != 0:
        el_sum = el_start + el_sum
        el_row = el_row + f'{el_start} '
        el_start /= -2
        el_count -= 1
        return row_sum_recursion(el_count, el_start, el_sum, el_row)
    else:
        return f'Сумма элементов ряда: {el_row}= {el_sum}'


# Алгоритм нахождения суммы n элементов, ряда чисел: 1 -0.5 0.25 -0.125 ...
# 1. Цикл

def row_sum_cycle(num):
    el_sum = 0
    el_start = 1
    el_row = ''

    for i in range(num):
        el_sum += el_start
        el_row += f'{el_start} '
        el_start /= -2

    return 'Сумма элементов ряда: {el_row}= {el_sum}'


# Зададим количество элементов ряда

n = 20

# Сравним время выполнения алгоритма с рекурсией и алгоритма с циклом,
# при помощи модуля timeit

# Количество выполнений оставим по умолчанию (number = 1000000)

print('RECURSION:', timeit.timeit('row_sum_recursion(n)', setup='from __main__ import row_sum_recursion, n'))
print('CYCLE:', timeit.timeit('row_sum_cycle(n)', setup='from __main__ import row_sum_cycle, n'))

# Результаты (при n = 20):

# RECURSION: 23.808849091
# CYCLE: 19.093803622000003

# Реализация алгоритма с циклом (без рекурсии) быстрее примерно на 2.5 секунды
# Вывод: целесообразнее использовать алгоритм с циклом.
