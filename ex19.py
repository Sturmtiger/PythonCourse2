import os
# os.chdir('dataset/')
# print(os.getcwd())
with open('dataset\\out(ex19).txt', 'w') as w:
    w.write('\n'.join([path for path, subfolders, files in os.walk('main') if any([file[-3:] == '.py' for file in files])]))

with open('dataset\\out(ex19).txt', 'r') as r:
    print(len(r.readlines()))

#Должно получиться 104 строки. Могут возникнуть проблемы, если папка находится не в одной директории с рабочим файлом.