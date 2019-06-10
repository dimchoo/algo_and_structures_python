"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

from collections import Counter, deque

source_string = 'beep boop beer'


def huffman_tree(string_to_compress):
    """
    Функция принимает на вход строку и преобразует ее в дерево Хаффмана,
    возврашает многомерный словарь.
    :param string_to_compress: string
    :return: dict
    """
    frequency_dict = Counter(string_to_compress)
    sorted_frequency = deque(sorted(frequency_dict.items(), key=lambda item: item[1]))
    if len(sorted_frequency) != 1:
        while len(sorted_frequency) > 1:
            weight = sorted_frequency[0][1] + sorted_frequency[1][1]
            comb = {0: sorted_frequency.popleft()[0],
                    1: sorted_frequency.popleft()[0]}
            for i, freq in enumerate(sorted_frequency):
                if weight > freq[1]:
                    continue
                else:
                    sorted_frequency.insert(i, (comb, weight))
                    break
            else:
                sorted_frequency.append((comb, weight))
        else:
            weight = sorted_frequency[0][1]
            comb = {0: sorted_frequency.popleft()[0], 1: None}
            sorted_frequency.append((comb, weight))
        return sorted_frequency[0][0]


code_table = {}


def huffman_compression(tree, path=''):
    """
    Функция принемает на вход дерево Хаффмана
    и заполняет словарь соответствия букв и их битовых значений
    :param tree: dict
    :param path: string (0 or 1)
    """
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        huffman_compression(tree[0], path=f'{path}0')
        huffman_compression(tree[1], path=f'{path}1')


huffman_compression(huffman_tree(source_string))

for i in source_string:
    print(code_table[i], end=' ')
