"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

ROW_COUNT = 5
COL_COUNT = 4

matrix = []
for i in range(ROW_COUNT):
    row = []
    sum_row = 0
    for j in range(COL_COUNT):
        number = int(input(f'Введите {j + 1} элемент {i + 1} строки: '))
        sum_row += number
        row.append(number)
    row.append(sum_row)
    matrix.append(row)

for r in matrix:
    print(r)

