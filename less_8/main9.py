# Функция - map
# Набор чисел
numbers = [5, 3, 4, 7, 8]

# Получить список квадратов чисел
print(list(map(lambda x: x**2, numbers))) # Получаем [25, 9, 16, 49, 64]
# Привести числа к строке
print(list(map(lambda x: str(x), numbers))) # Получаем ['5', '3', '4', '7', '8']

