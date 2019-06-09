"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

import random

random_list = [round(random.uniform(0, 50), 2) for _ in range(10)]


def merge_sort(lst):
    if len(lst) > 1:
        center = len(lst) // 2
        left = lst[:center]
        right = lst[center:]

        merge_sort(left)
        merge_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            lst[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            lst[k] = right[j]
            j += 1
            k += 1
        return lst


print(f'Исходный список:\n{random_list}')
print(f'Список, отсортированный слиянием:\n{merge_sort(random_list)}')


