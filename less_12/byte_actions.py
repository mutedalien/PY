# обычная строка
s = 'Hello world'
# строка байт
sb = b'Hello bytes'

# индекс в простой строке
print(s[1])
# индекс в строке байт
print(sb[1])

# срез в обычной строке
print (s[1:3])
# срез в строке байт
print (sb[1:3])

# перебор строки байт в цикле
for item in sb:
    print(item)