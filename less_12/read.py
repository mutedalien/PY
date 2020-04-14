# Открываем файл на чтение
f = open('firsr.txt', 'r')

#print(f.read())

#for line in f:
    #print(line) # вернет с лишними переносами строк
    #print(line.replace('\n', '')) # затрем лишние переносы

print(f.readlines())
