# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

import random

ROWS = 5
COLS = 5

matrix = [[random.randint(10, 99) for i in range(COLS)] for j in range(ROWS)]

new_matrix = []

for i in range(COLS):
    new_matrix_rows = []
    for row in matrix:
        new_matrix_rows.append(row[i])
    new_matrix.append(new_matrix_rows)

min_num_list = []

for i in new_matrix:
    min_num = float('inf')
    for j in i:
        if j < min_num:
            min_num = j
    min_num_list.append(min_num)

max_min_element = float('-inf')

for i in min_num_list:
    if i > max_min_element:
        max_min_element = i

print('В матрице:')
for i in range(ROWS):
    for j in range(COLS):
        print(matrix[i][j], end=' ')
    print()

print('Минимальные элементы столбцов:')

for i in range(COLS):
    print(min_num_list[i], end=' ')

print(f'\nСреди которых максимальный элемент: {max_min_element}')
