"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""

# Решение с помощью рекурсии

def count_number_in_sequence(number, count_of_numbers, counter=0, try_count=0):
    try_count += 1
    if count_of_numbers == 0:
        print(f'Число {number} встречается {counter} раз(а)')
        return

    number_in_sequence = int(input(f'Введите {try_count} число последовательности: '))
    if number_in_sequence == number:
        counter += 1
        count_of_numbers -= 1
        return count_number_in_sequence(number, count_of_numbers, counter, try_count)
    else:
        count_of_numbers -= 1
        return count_number_in_sequence(number, count_of_numbers, counter, try_count)


search_number = int(input('Ведите искомое число: '))
sequence_len = int(input('Введите количество чисел в последовательности: '))

count_number_in_sequence(search_number, sequence_len)


# Решение с помощью цикла

search_number = int(input('Ведите искомое число: '))
sequence_len = int(input('Введите количество чисел в последовательности: '))
counter = 0
try_count = 1

for i in range(sequence_len):
    number = int(input(f'Введите {try_count} число последовательности: '))
    try_count += 1
    if number == search_number:
        counter += 1

print(f'Число {search_number} встречается {counter} раз(а)')

