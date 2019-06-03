"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

# Сравним 4 разных реализации алгоритма нахождения i-го по счёту простого числа.

# Для анализа затрачеваемой памяти воспользуемся декоратором profile мз модуля memory_profiler:

from memory_profiler import profile


# 1. Первый алгоритм, реализованый мной на 4 занятии - «Решето Эратосфена»:

@profile
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


# 2. Второй алгоритм, реализованый мной на 4 занятии - «Нахождение i-го числа, при помощи цикла»:

@profile
def prime_number(count, element):
    lst = [2]
    for num in range(3, count, 2):
        if all(num % i != 0 for i in range(2, int(num ** .5) + 1)):
            lst.append(num)
    return lst[element]


# 3. Третий алгоритм, реализованы Вами - «Решето Эратосфена»:

@profile
def eratosfen(i, l):
    n = 2
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


# 4. Четвертый алгоритм, реализованы Вами - «Нахождение i-го числа, при помощи цикла»:

@profile
def simple(i, count):
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


# Сравним затрачиваемую память при работе всех функций на маленьких и больших значениях:

# test_el = 1
# test_count = 4

test_el = 10
test_count = 200


if __name__ == '__main__':
    # eratosthenes(test_count, test_el)
    # prime_number(test_count, test_el)
    # eratosfen(test_el, test_count)
    simple(test_el, test_count)

# Результаты:

# Общая выделеная память на выполнение функции
# eratosthenes(test_count=4, test_el=1) = 10.5 MiB
# Общая выделеная память на выполнение функции
# eratosthenes(test_count=200, test_el=10) = 10.6 MiB

# Общая выделеная память на выполнение функции
# prime_number(test_count=4, test_el=1) = 10.6 MiB
# Общая выделеная память на выполнение функции
# prime_number(test_count=200, test_el=10) = 10.6 MiB

# Общая выделеная память на выполнение функции
# eratosfen(test_el=1, test_count=4) = 10.6 MiB
# Общая выделеная память на выполнение функции
# eratosfen(test_count=10, test_el=200) = 10.6 MiB

# Общая выделеная память на выполнение функции
# simple(test_el=1, test_count=4) = 10.6 MiB
# Общая выделеная память на выполнение функции
# simple(test_count=10, test_el=200) = 10.6 MiB

# Вывод: На выполнение всех (4-х) реализаций одного алгоритма
# затрачивается примерно одинаковое количество памяти
