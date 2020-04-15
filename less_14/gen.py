# записать в список только положительные числа
numbers = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]

# классический случай
result = [] # переменная для результата
for number in numbers: # в цикле перебираем наши числа
    if number > 0: # если число > 0
        result.append(number) # то добавляем в результат это число
print(result)

# через функцию filter
# на входе number, на выходе number > 0
result = filter(lambda number: number > 0, numbers) # функция из двух частей
print(list(result))

# через генератор
result = [number for number in numbers if number > 0] # перебираем список и записываем по условию (>0)
print(result)


# генератор словаря
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]

# классический способ
result = {}
for pair in pairs: # перебираем пары
    key = pair[0]
    val = pair[1]
    result[key] = val # по ключу сохраняем значение
print(result)

# через генератор словаря
result = {pair[0]: pair[1] for pair in pairs} # слева ключ [0], справа значение [1]
print(result)