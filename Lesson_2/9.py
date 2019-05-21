"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""


def one_number_amount(number, numbers_sum=0):
    numbers_sum += number % 10
    if number // 10 == 0:
        return numbers_sum
    else:
        number //= 10
        return one_number_amount(number, numbers_sum)


def check_numbers_amount(num_count, highest_sum=0, highest_num=0):
    if num_count != 0:
        num_count -= 1
        check_number = int(input('Введите натуральное число: '))
        if one_number_amount(check_number) > highest_sum:
            highest_sum = one_number_amount(check_number)
            highest_num = check_number
            return check_numbers_amount(num_count, highest_sum, highest_num)
        else:
            return check_numbers_amount(num_count, highest_sum, highest_num)
    else:
        print(f'У числа {highest_num}, наибольшая сумма цифр, она равна {highest_sum}')


count_of_numbers = int(input('Введите количество натуральных чисел: '))

check_numbers_amount(count_of_numbers)
