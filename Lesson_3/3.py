# 3. В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.

import random

random_list = []

for i in range(10):
    random_list.append(random.randint(-100, 100))

print(f'Массив случайных целых чисел:\n{random_list}')

min_el = float('inf')
min_index = 0
max_el = float('-inf')
max_index = 0

for i in random_list:
    if i < min_el:
        min_el = i
        min_index = random_list.index(i)
    if i > max_el:
        max_el = i
        max_index = random_list.index(i)

print(f'Минимальный элемент: {min_el}\n'
      f'Максимальный элемент: {max_el}\n'
      f'Меняем их местами:')

random_list[min_index] = max_el
random_list[max_index] = min_el

print(random_list)
