import os
import re

script_dir = os.path.dirname(__file__)  # Получение пути до директории скрипта
path = input()  # Ввод пути до файла или папки (в моем примере это Test_Mail/log.log или Test_Mail)
pattern = re.compile(' [a-zA-Z]{7}: [a-zA-Z]{7}:')  # Регулярка для поиска подходящих строк
abs_file_path = os.path.join(script_dir, path)  # Прикрепление к пути директории тот путь, что мы ввели
result = open('result.log', 'w')  # Открытие файла на запись для результатов поиска
# print(abs_file_path)  # Вывод пути
if abs_file_path.find('.log') != -1:  # Проверка на то, что у нас путь к файлу
    f = open(abs_file_path, "r")  # Открытие файла на чтение
    for line in f:  # Цикл для взаимодействия с файлом построчно
        print(line)  # Вывод строки
        if pattern.findall(line):  # Проверяем, есть ли совпадение с шаблоном
            result.write(line + '\n')  # Запись подходящих строк в файл
else:  # Иначе)
    for file in os.listdir(abs_file_path):  # Цикл для перечисление файлов в директории
        with open(os.path.join(abs_file_path, file), 'r') as f:  # Открытие файла на чтение
            for line in f:  # Цикл для взаимодействия с файлом построчно
                print(line)  # Вывод строки
                if pattern.findall(line):   # Проверяем, есть ли совпадение с шаблоном
                    result.write(line + '\n')   # Запись подходящих строк в файл
