# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

import random

random_list = []

for i in range(10):
    random_list.append(random.randint(-10, 10))

max_from_negative = float('-inf')
max_from_negative_index = 0
min_from_positive = float('inf')
min_from_positive_index = 0

for i in random_list:
    if i < 0:
        if i > max_from_negative:
            max_from_negative = i
            max_from_negative_index = random_list.index(i)
    elif i > 0:
        if i < min_from_positive:
            min_from_positive = i
            min_from_positive_index = random_list.index(i)

if -max_from_negative <= min_from_positive:  # либо abs(max_from_negative), либо (max_from_negative * -1)
    max_negative_element = max_from_negative
    max_negative_element_index = max_from_negative_index
else:
    max_negative_element = min_from_positive
    max_negative_element_index = min_from_positive_index

print(f'В массиве:\n'
      f'{random_list}\n'
      f'Максимальный отрицательный элемент:\n'
      f'{max_negative_element}, его индекс {max_negative_element_index}')
