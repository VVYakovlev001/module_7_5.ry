import time
import os

# вывести текущую директорию
print("Текущая деректория:", os.getcwd())
# создать пустой каталог (папку)
if not os.path.isdir("folder"):
    os.mkdir("folder")
    # изменение текущего каталога на 'folder'
os.chdir("folder")
# вывод текущей папки
print("Текущая директория изменилась на folder:", os.getcwd())
path = 'C:\\Users\\yakov\\PycharmProjects\\module_7_5.ry\\folder'

for root, dirs, files in os.walk("."):
    for file in files:
        if not os.path.isdir("."):
            os.mkdir(".")

filepath = os.path.join(path)
filetime = os.path.getmtime
formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
filesize = os.path.getsize(path)
parent_dir = os.path.dirname(path)
print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт,'
      f' Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

#Так как в разных операционных системах разная схема расположения папок,
# тестировать проще всего в папке проекта (directory = “.”)
#Пример возможного вывода:
#Обнаружен файл: main.py, Путь: ./main.py, Размер: 111 байт,
# Время изменения: 11.11.1111 11:11, Родительская директория.


#Используйте os.walk для обхода каталога, путь к которому указывает переменная directory
#Примените os.path.join для формирования полного пути к файлам.
#Используйте os.path.getmtime и модуль time для получения и отображения времени
# последнего изменения файла.
#Используйте os.path.getsize для получения размера файла.
#Используйте os.path.dirname для получения родительской директории файла.
#
