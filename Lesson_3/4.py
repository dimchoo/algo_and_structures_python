# 4. Определить, какое число в массиве встречается чаще всего.

import random

random_list = []

for i in range(20):
    random_list.append(random.randint(0, 100))

max_count = 0
max_count_number = 0

for i in random_list:
    if max_count < random_list.count(i):
        max_count = random_list.count(i)
        max_count_number = i

if max_count == 1:
    print('Все числа в массиве уникальны!')
else:
    print(f'В массиве случайных целых чисел: {random_list}\n'
          f'Первое число, встречающиеся чаще всего: {max_count_number}, в количестве {max_count} раз(а)')
