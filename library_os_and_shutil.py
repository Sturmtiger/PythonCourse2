import os
import os.path

# print(os.getcwd()) # узнать в какой директории мы находимся(путь)
# print(os.listdir()) # файлы в директории(без аргумента - в текущей директории)
# print(os.path.exists('dataset')) # узнать существует ли файл или папка в директории(out:Boolean)
# print(os.path.isfile('ex1.py')) # является ли объект файлом(out:Boolean)
# print(os.path.isdir('folder')) # является ли объект папкой(out:Boolean)
# print(os.path.abspath('ex3.py')) #узнать абсолютный путь(передаем объект в качестве аргумента и создается относительный путь из директории, в которой мы находимся
# print(os.chdir()) # ИЗМЕНИТЬ текущую директорию
print(os.walk('.')) # позволяет рекурсивно пройтись по всем папкам, подпапкам и т.д., данная функция возвращает - генератор
for current_dir, dirs, files in os.walk('.'): # '.' - текущая директория
    print(current_dir, dirs, files)
# каждое значение, которое возвращает нам генератор есть - кортеж из 3 элементов: 1 - строковое представление текущей директории, которую он осматривает,
# 2 - список подпапок, которые находятся в данной директории, 3 - список всех файлов находящихся в данной директории


import shutil # для копирования файлов

shutil.copy('folder/file1.txt', 'folder/file2.txt') # принимает 2 аргумента, откуда и куда копировать(для файлов)
shutil.copy('folder', 'folder/folder') # принимает 2 аргумента, откуда и куда копировать(для папок). Копирует папку с её содержимым