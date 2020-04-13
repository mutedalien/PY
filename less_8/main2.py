# Функция простой разделитель

def get_sep(sep, sep_len): # sep - символ разделителя, sep_len - длинна
    #print (sep * sep_len) # Выводим значение
    return sep * sep_len # Возвращаем значение
print('Разделитель')
print(get_sep('*', 50))
print(get_sep('/', 50))
print(get_sep('-', 50))

sep = get_sep('.', 10)
text = 'Hello {} Func {} !!'.format(sep, sep)

print(text)