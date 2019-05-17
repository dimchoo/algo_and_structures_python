# 5. Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

letter1 = ord(input('Введите первую букву: '))
letter2 = ord(input('Введите вторую букву: '))

ASCII_COUNT = 96

position_letter1 = letter1 - ASCII_COUNT
position_letter2 = letter2 - ASCII_COUNT

if letter1 < letter2:
    print(f'Буква "{chr(letter1)}" стоит на {position_letter1} месте алфавита\n'
          f'Буква "{chr(letter2)}" стоит на {position_letter2} месте алфавита\n'
          f'Количество букв между ними: {letter2 - letter1 - 1}')
elif letter1 > letter2:
    print(f'Буква "{chr(letter1)}" стоит на {position_letter1} месте алфавита\n'
          f'Буква "{chr(letter2)}" стоит на {position_letter2} месте алфавита\n'
          f'Количество букв между ними: {letter1 - letter2 - 1}')
else:
    print('Некорректный ввод!')
