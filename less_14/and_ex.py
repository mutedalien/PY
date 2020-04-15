import math

if 2 > 1 and math.sqrt(-1): # заведомо False (квадратн корень из -1 нельзя извлечь)
    print('Ошибки не будет, т.к. первое условие False')
print('Двигаемся дальше')

# первая ложь
print([1] and [2] and '' and 1)

# последняя ложь
print([1] and [1] and 20 and 1.1)