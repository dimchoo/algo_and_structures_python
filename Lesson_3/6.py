"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

random_list = []

for i in range(10):
    random_list.append(random.randint(-30, 30))

print(random_list)

min_element = 0
min_el_index = 0
max_element = 0
max_el_index = 0

for i in random_list:
    if i < min_element:
        min_element = i
        min_el_index = random_list.index(i)
    elif i > max_element:
        max_element = i
        max_el_index = random_list.index(i)

if min_el_index < max_el_index:
    if min_el_index + 1 != max_el_index:
        result = sum(random_list[min_el_index + 1:max_el_index])
        print(f'Минимальный элемент = {min_element}. Максимальный элемент = {max_element}\n'
              f'Сумма элементов между ними = {result}')
    else:
        print(f'Минимальный элемент = {min_element}. Максимальный элемент = {max_element}\n'
              f'Между минимальным и максимальным элементами не стоит других элементов.')

if min_el_index > max_el_index:
    if max_el_index + 1 != min_el_index:
        result = sum(random_list[min_el_index - 1:max_el_index:-1])
        print(f'Минимальный элемент = {min_element}. Максимальный элемент = {max_element}\n'
              f'Сумма элементов между ними = {result}')
    else:
        print(f'Минимальный элемент = {min_element}. Максимальный элемент = {max_element}\n'
              f'Между минимальным и максимальным элементами не стоит других элементов.')
