"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""

import random

random_list = [random.randint(-10, 10) for i in range(10)]

min_number1 = float('inf')
min_number2 = float('inf')
min_num_index1 = 0
min_num_index2 = 0

for counter, value in enumerate(random_list):
    if value < min_number1:
        min_number1 = value
        min_num_index1 = counter

for counter, value in enumerate(random_list):
    if counter != min_num_index1:
        if value < min_number2:
            min_number2 = value
            min_num_index2 = counter

print(f'В массиве: {random_list}\n'
      f'Первый наименьший элемент: {min_number1}, его индекс = {min_num_index1}\n'
      f'Второй наименьший элемент: {min_number2}, его индекс = {min_num_index2}')
