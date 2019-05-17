"""
7.	По длинам трех отрезков, введенных пользователем, определить возможность
существования треугольника, составленного из этих отрезков. Если такой
треугольник существует, то определить, является ли он
разносторонним, равнобедренным или равносторонним.
"""

segment1 = float(input('Первый отрезок: '))
segment2 = float(input('Второй отрезок: '))
segment3 = float(input('Третий отрезок: '))

if segment1 + segment2 > segment3 \
        and segment1 + segment3 > segment2 \
        and segment2 + segment3 > segment1:
    print('Треугольник существует!')
    if segment1 == segment2 == segment3:
        print('Треугольник равносторонний!')
    elif segment1 == segment2 or segment1 == segment3 or segment2 == segment3:
        print('Треугольник равнобедренный!')
    else:
        print('Треугольник разносторонний!')
else:
    print('Такого треугольника не существует!')
