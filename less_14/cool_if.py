# проверка на пустоту
# строка
s = 'abc'
# классический способ
if len(s) != 0:
    print('Строка не пустая')
else:
    print('Строка пустая')

# python-способ
if s:
    print('Строка не пустая')
else:
    print('Строка пустая')

# аналогично со списками, словарями и другими типами
l = [1, 2, 3]
d = {1: 'a'}
# классический способ
if len(l) != 0 and len(d) != 0:
    print('Список и словарь не пустые')
else:
    print('Список и словарь пустые')

# python-способ
if l and d:
    print('Список и словарь не пустые')
else:
    print('Список и словарь пустые')