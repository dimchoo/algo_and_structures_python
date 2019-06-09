"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы. Задачу можно решить без сортировки исходного
массива. Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках
"""

import random

# Сделал при помощи шейкерной сортировки, как проосили на занятии.

m = int(input('Для массива размером 2m + 1, где m – натуральное число,\nвведите m: '))
list_length = 2 * m + 1
random_list = [random.randint(0, 100) for _ in range(list_length)]


def shaker_sort(lst):
    left = 0
    right = len(lst) - 1
    while left <= right:
        for i in range(left, right):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        right -= 1
        for i in range(right, left, -1):
            if lst[i - 1] > lst[i]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
        left += 1
    return lst


print(f'Исходный массив: {random_list}')
print(f'Отсортированный массив: {shaker_sort(random_list)}')
print(f'Медиана отсортированного массива: {shaker_sort(random_list)[m]}')


# 2-й вариант Python-way:

print(f'Python wey: {sorted(random_list)[m]} :)')



