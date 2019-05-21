"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
 где n - любое натуральное число.
"""

# Решение с помощью рекурсии

user_n = int(input('Введите натуральное число: '))


def induction(n, start_el=1, el_sum=0):
    el_sum += start_el
    if start_el == n:
        if el_sum == n * (n + 1) / 2:
            print('Гипотеза доказана!')
        else:
            print('Гипотеза опровергнута!')
    else:
        start_el += 1
        return induction(n, start_el, el_sum)


induction(user_n)


# Решение с помощью цикла

user_n = int(input('Введите натуральное число: '))
el_sum = 0

for i in range(user_n):
    i += 1
    el_sum += i
    if i == user_n:
        if el_sum == user_n * (user_n + 1) / 2:
            print('Гипотеза доказана!')
        else:
            print('Гипотеза опровергнута!')
