# 3. Разработать генератор случайных чисел. В функцию передавать начальное и конечное число генерации
# (нуль необходимо исключить). Заполнить этими данными список и словарь. Ключи словаря должны создаваться по шаблону:
# “elem_<номер_элемента>”. Вывести содержимое созданных списка и словаря.

import random


def generate(start, finish):
    value_list = []
    value_dict = {}
    for idx, _ in enumerate(range(10), 1):
        rnd = int((finish - start) * random.random() + start)
        value_list.append(rnd)
        value_dict[f'elem_{idx}'] = rnd

    return value_list, value_dict


print(generate(1, 10))
