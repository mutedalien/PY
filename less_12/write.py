# Открываем файл на запись
f = open('firsr.txt', 'w') # создаст файл

f.write('Hello\n') # \n - перенос строки
f.write('World!\n')

f.writelines(['Hello\n', 'Pyton!\n']) 

