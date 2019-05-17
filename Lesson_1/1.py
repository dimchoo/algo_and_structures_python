# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

user_number = int(input('Введите трехзначное число: '))
MIN_NUMBER = 100
MAX_NUMBER = 999

if MIN_NUMBER <= user_number <= MAX_NUMBER:
    first_number = user_number // 100
    second_number = (user_number // 10) % 10
    third_number = user_number % 10

    print(f'Сумма цифр числа: {first_number + second_number + third_number}\n'
          f'Произведение цифр числа: {first_number * second_number * third_number}')

elif -MIN_NUMBER >= user_number >= -MAX_NUMBER:
    user_number = abs(user_number)
    first_number = -(user_number // 100)
    second_number = (user_number // 10) % 10
    third_number = user_number % 10

    print(f'Сумма цифр числа: {first_number + second_number + third_number}\n'
          f'Произведение цифр числа: {first_number * second_number * third_number}')

else:
    print('Вы ввели некорректные данные!')
