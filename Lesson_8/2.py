"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""

import hashlib

my_string = 'hello'


def substring_counter_by_hash(string):
    """
    Функция принимает на вход строку,
    вычисояет все подстроки и их количество,
    возвращает словарь с вычисленными данными.
    :param string: str
    :return: dict
    """
    hash_set = set()
    substrings_set = set()
    n = len(string)

    for i in range(n):
        if i == 0:
            n = len(string) - 1
        else:
            n = len(string)
        for j in range(n, i, -1):
            substrings_set.add(string[i:j])
            hash_set.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())

    result = {
        'substring_count': len(hash_set),
        'substrings': tuple(substrings_set),
    }
    return result


substrings_info = substring_counter_by_hash(my_string)

print(f'Все подстроки из строки "{my_string}":\n'
      f'{substrings_info["substrings"]}\n'
      f'Количество подстрок: {substrings_info["substring_count"]}')
