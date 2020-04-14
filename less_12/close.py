# Открываем файл на чтение
f = open('firsr.txt', 'r')

for line in f:
    print(line.replace('\n', ''))

f.close()

with open('firsr.txt', 'r') as f:
    for line in f:
        print(line.replace('\n', ''))

print('end')