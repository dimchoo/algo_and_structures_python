# 9. Вводятся три разных числа. Найти, какое из них
# является средним (больше одного, но меньше другого).

num1 = float(input('Введите первое число: '))
num2 = float(input('Введите второе число: '))
num3 = float(input('Введите третье число: '))

if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 < num2 < num3:
        print(f'Средним числом из {num1, num2, num3} является {num2}')
    elif num1 < num3 < num2:
        print(f'Средним числом из {num1, num2, num3} является {num3}')
    else:
        print(f'Средним числом из {num1, num2, num3} является {num1}')
else:
    print('Некорректный ввод!')
