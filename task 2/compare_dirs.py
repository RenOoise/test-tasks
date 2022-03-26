import os

path_a = 'dirs/a'
path_b = 'dirs/b'

# получаем список файлов в директориях 
# a
files_list_a = os.listdir(path_a)
# b
files_list_b = os.listdir(path_b)

# прогоняем циклами по спискам
for a in  files_list_a:
    for b in files_list_b:
        # проверяем что это не директория
        if os.path.isfile(os.path.join(path_b, b)):
            # проверяем на совпадения в именах
            if a == b:
                os.remove(os.path.join(path_b, b))
