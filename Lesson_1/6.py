# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

letter_number = int(input('Введите номер буквы: '))

MIN_LETTER = 1
MAX_LETTER = 26
ASCII_COUNT = 96

if MIN_LETTER <= letter_number <= MAX_LETTER:
    print(f'Под номером "{letter_number}" находится буква "{chr(letter_number + ASCII_COUNT)}"')
else:
    print('Некорректный ввод!')
