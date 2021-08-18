# 2. Дополнить следующую функцию недостающим кодом:
#
# def print_directory_contents(sPath):
# """
# Функция принимает имя каталога и распечатывает его содержимое
# в виде «путь и имя файла», а также любые другие
# файлы во вложенных каталогах.
#
# Эта функция подобна os.walk. Использовать функцию os.walk
# нельзя. Данная задача показывает ваше умение работать с
# вложенными структурами.
# """
import os


def print_directory_contents(path):
    struct = []
    for file_or_directory in os.listdir(path):
        full_name = os.path.join(os.path.abspath(path), file_or_directory)
        if os.path.isfile(full_name):
            file_name = os.path.join(os.path.abspath(path), file_or_directory)
            struct.append(file_name)
        else:
            struct.extend(print_directory_contents(full_name))
    return struct


print(print_directory_contents(r'C:\tmp'))
