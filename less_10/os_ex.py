import os
# Имя операционной оси
print(os.name)
# Текущая рабочая директория
print(os.getcwd())
# Создаем новый путь
new_path = os.path.join(os.getcwd(), 'new_f')
# Создаем папку по новому пути
os.mkdir(new_path)