"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""

import timeit


# Алгоритм с использованием «Решета Эратосфена»:

def eratosthenes(count, element):
    a = [0] * count
    for i in range(count):
        a[i] = i

    a[1] = 0

    m = 2
    while m < count:
        if a[m] != 0:
            j = m * 2
            while j < count:
                a[j] = 0
                j = j + m
        m += 1

    lst = []
    for i in a:
        if a[i] != 0:
            lst.append(a[i])

    del a
    return lst[element]


# Алгоритм без использования «Решета Эратосфена»:

def prime_number(count, element):
    lst = [2]
    for num in range(3, count, 2):
        if all(num % i != 0 for i in range(2, int(num ** .5) + 1)):
            lst.append(num)
    return lst[element]


my_count = 30
my_element = 3

print(eratosthenes(my_count, my_element))
print(prime_number(my_count, my_element))

print('Решето Эратосфена:', timeit.timeit('eratosthenes(my_count, my_element)',
                                          setup='from __main__ import eratosthenes, my_count, my_element'))
print('Алгоритм без решета:', timeit.timeit('prime_number(my_count, my_element)',
                                            setup='from __main__ import prime_number, my_count, my_element'))

# Решето Эратосфена: 9.436788654999999
# Алгоритм без решета: 16.006209949

# В данном случае решето Эратосфена эффективнее
