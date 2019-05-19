"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""

# Решение с помощью рекурсии


def even_odd(number, even_num=0, odd_num=0, events_str='', odds_str=''):
    even_count = even_num
    odd_count = odd_num
    evens = events_str
    odds = odds_str
    one_number = number % 10
    new_number = number // 10

    if new_number == 0:
        if one_number % 2 == 0:
            even_count += 1
            events = f'{one_number}, {evens}'
            print(f'Четные цифры: {events}количесво {even_count} шт.\n'
                  f'Нечетные цифры {odds}количество {odd_count} шт.')
        else:
            odd_count += 1
            odds = f'{one_number}, {odds}'
            print(f'Четные цифры: {evens}количесво {even_count} шт.\n'
                  f'Нечетные цифры {odds}количество {odd_count} шт.')
        return

    if one_number % 2 == 0:
        even_count += 1
        events = f'{one_number}, {evens}'
        return even_odd(new_number, even_count, odd_count, events, odds)
    else:
        odd_count += 1
        odds = f'{one_number}, {odds}'
        return even_odd(new_number, even_count, odd_count, evens, odds)


user_number = int(input('Введите натуральное число: '))

even_odd(user_number)


# Решение с помощью цикла

user_number = input('Введите натуральное число: ')

even_count = 0
evens = ''
odd_count = 0
odds = ''


for i in user_number:
    if int(i) % 2 == 0:
        even_count += 1
        evens += f'{i}, '
    else:
        odd_count += 1
        odds += f'{i}, '

print(f'Четные цифры: {evens}количесво {even_count} шт.\n'
      f'Нечетные цифры {odds}количество {odd_count} шт.')

