"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

# Конечно все можно сделать намного проще, но поскольку требуется использование модуля collections,
# пришлось везде напихать его методов :)

from collections import defaultdict, namedtuple

companies_count = int(input('Введите количество предриятий: '))

company_profits = namedtuple('Company', 'quarter_1 quarter_2 quarter_3 quarter_4 year_profit')

companies_dict = defaultdict(company_profits)

for i in range(companies_count):
    company_name = input(f'Название {i + 1} компании: ')
    company_profit1 = int(input('Прибыль за 1 квартал: '))
    company_profit2 = int(input('Прибыль за 2 квартал: '))
    company_profit3 = int(input('Прибыль за 3 квартал: '))
    company_profit4 = int(input('Прибыль за 4 квартал: '))
    profits = company_profits(
        quarter_1=company_profit1,
        quarter_2=company_profit2,
        quarter_3=company_profit3,
        quarter_4=company_profit4,
        year_profit=company_profit1 + company_profit2 + company_profit3 + company_profit4
    )
    companies_dict[company_name] = profits

all_profits = 0

for key, value in companies_dict.items():
    all_profits += value.year_profit

average_profit = all_profits / companies_count

high_profit = defaultdict(int)
low_profit = defaultdict(int)
same_profit = defaultdict(int)

for key, value in companies_dict.items():
    if value.year_profit > average_profit:
        high_profit[key] = value.year_profit
    elif value.year_profit < average_profit:
        low_profit[key] = value.year_profit
    else:
        same_profit[key] = value.year_profit

if companies_count > 1:
    print(f'Среднегодовая прибыль {companies_count} компаний: {round(average_profit, 1)} руб.')
    if high_profit:
        print('Предприятия, чья прибыль выше среднего значения:')
        for key, value in high_profit.items():
            print(f'"{key}" - годовая прибыль: {value} руб.')
    if low_profit:
        print('Предприятия, чья прибыль ниже среднего значения:')
        for key, value in low_profit.items():
            print(f'"{key}" - годовая прибыль: {value} руб.')
    if same_profit:
        print('Предприятия, чья прибыль равна среднему значению:')
        for key, value in same_profit.items():
            print(f'"{key}" - годовая прибыль: {value} руб.')
elif companies_count == 1:
    print(f'Годовая прибыль одной компании: {average_profit} руб.\n'
          f'К сожалению ее не с чем сравнить...')
else:
    print('Неправильный ввод!')
