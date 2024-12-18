
import os
import time
print('Текущая директория', os.getcwd())

for root,dirs,files in os.walk('.'):
    for file in files:
        filepath = os.path.join(root,file)
        filetime = os.path.getatime(filepath)
        formatted_time = time.strftime("%d.%m.%H:%M", time.localtime(filetime))
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(os.path.abspath(filepath))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
              f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')



