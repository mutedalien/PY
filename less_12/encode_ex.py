s = 'Hello world Мир привет'

sb = s.encode('utf-8')

print(sb)
print(type(sb))

s = sb.decode('utf-8') # раскодируем кирилицу

print(s)
print(type(s))