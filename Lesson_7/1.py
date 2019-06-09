"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""

import random

random_list = [random.randint(-100, 100) for _ in range(30)]


def bubble_sort(lst, reverse=True):
    """
    Функция принимает на вход список с произвольными целыми числами
    и булево значение направления сортировки.
    Сортирует его при помощи пузырькового алгоритма (по направлению)
    и возвращает отсортированный список
    :param lst: list (unsorted)
    :param reverse: boolean (default true)
    :return: list (sorted in reverse order)
    """
    n = 1
    if reverse:
        while n < len(lst):
            for i in range(len(lst) - n):
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            n += 1
        return lst
    else:
        while n < len(lst):
            for i in range(len(lst) - n):
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
            n += 1
        return lst


print(f'Исходный список: {random_list}')
print(f'Отсортированный исходный список: {bubble_sort(random_list)}')
print(f'Отсортированный исходный список: {bubble_sort(random_list, False)}')
