"""
2. Создать пользовательский класс данных (или использовать) один из классов,
реализованных в курсе Python.Основы. Реализовать класс с применением слотов
и обычным способом. Для объекта обычного класса проверить отображение словаря
атрибутов. Сравнить, сколько выделяется памяти для хранения атрибутов обоих
классов.
"""

from pympler import asizeof


# 1. Создадим простой класс "Машина" обычным способом:

class Car:
    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def get_car_info(self):
        print(f'Машина: {self.color} {self.name}\n'
              f'Скорость: {self.speed} км/ч')

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')


# 2. Создадим такой же класс "Машина", но с применением слотов:

class CarSlots:
    # Переопределим хранение атрибутов класса в виде кортежа:
    __slots__ = ('speed', 'color', 'name', 'direction')

    def __init__(self, speed, color, name):
        self.speed = speed
        self.color = color
        self.name = name

    def get_car_info(self):
        print(f'Машина: {self.color} {self.name}\n'
              f'Скорость: {self.speed} км/ч')

    def go(self):
        print(f'Машина {self.name} поехала!')

    def stop(self):
        print(f'Машина {self.name} остановилась!')


# Заполним одинаковыми значениями атрибуты обоих классов:

car_simple = Car('220', 'Синий', 'Audi')
car_slots = CarSlots('220', 'Синий', 'Audi')

# Вызовем системный метод словарь для car_simple:
# Результат: {'speed': '220', 'color': 'Синий', 'name': 'Audi'}

print(car_simple.__dict__)

# Сравним размеры обычного класса и класса с использованием слотов:

print(f'Размер обычного экземпляра класса Car: {asizeof.asizeof(car_simple)}')
print(f'Размер экземпляра класса со слотами CarSlots: {asizeof.asizeof(car_slots)}')

# Результат:
# Размер обычного экземпляра класса Car: 536
# Размер экземпляра класса со слотами CarSlots: 272

# Вывод: если нет необходимости динамически создавать новые атрибуты класса,
# целесообоазно использование slots, для экономии памяти.
