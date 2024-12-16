
import os
import time
print('Текущая директория', os.getcwd())

for root,dirs,files in os.walk('.'):
    for file in files:
        filepath = os.path.join('.',file)
        filetime = os.path.getatime(file)
        formatted_time = time.strftime("%d.%m.%H:%M", time.localtime(filetime))
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(os.path.abspath(__file__))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
              f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')



