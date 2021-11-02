# work_with_file.py [a-zA-Z]{17}: Test_Mail\log.log
import os
import re
from sys import argv

script, regular, path = argv
pattern = re.compile(regular)  # Регулярка для поиска подходящих строк
with open('result.log', 'w') as result:
    if os.path.isdir(path):
        for file in os.listdir(path):  # Цикл для перечисление файлов в директории
            with open(os.path.join(path, file), 'r') as f:  # Открытие файла на чтение
                for line in f:  # Цикл для взаимодействия с файлом построчно
                    if pattern.findall(line):  # Проверяем, есть ли совпадение с шаблоном
                        result.write(line)  # Запись подходящих строк в файл
                        print(line)  # Вывод строки
    elif os.path.isfile(path):
        with open(path, "r") as f:
            for line in f:  # Цикл для взаимодействия с файлом построчно
                if pattern.findall(line):  # Проверяем, есть ли совпадение с шаблоном
                    result.write(line)  # Запись подходящих строк в файл
                    print(line)  # Вывод строки
