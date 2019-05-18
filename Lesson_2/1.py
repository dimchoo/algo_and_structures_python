"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""

# Решение с помощью рекурсии


def arithmetic():
    operation = input('Введите оператор (выйти: 0): ')

    if operation == '0':
        print('До свидания!')
        return
    elif operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print('Неверный оператор! Допустимые значения: +, -, *, /')
        return arithmetic()

    num1 = int(input('Первый операнд: '))
    num2 = int(input('Второй операнд: '))

    if operation == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
        return arithmetic()
    elif operation == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
        return arithmetic()
    elif operation == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
        return arithmetic()
    elif operation == '/':
        if num2 == 0:
            print('На ноль делить нельзя!')
            return arithmetic()
        else:
            print(f'{num1} / {num2} = {num1 / num2}')
            return arithmetic()


arithmetic()


# Решение с помощью цикла


while True:
    operation = input('Введите оператор (выйти: 0): ')

    if operation == '0':
        print('До свидания!')
        break
    elif operation != '+' and operation != '-' and operation != '*' and operation != '/':
        print('Неверный оператор! Допустимые значения: +, -, *, /')
        continue

    num1 = int(input('Первый операнд: '))
    num2 = int(input('Второй операнд: '))

    if operation == '+':
        print(f'{num1} + {num2} = {num1 + num2}')
    elif operation == '-':
        print(f'{num1} - {num2} = {num1 - num2}')
    elif operation == '*':
        print(f'{num1} * {num2} = {num1 * num2}')
    elif operation == '/':
        if num2 == 0:
            print('На ноль делить нельзя!')
        else:
            print(f'{num1} / {num2} = {num1 / num2}')
