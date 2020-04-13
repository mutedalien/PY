# Функция - filter
# Набор чисел
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Получить только четные числа
def is_even(number):
    return number % 2 == 0

result = filter(is_even, numbers)
print(result) # Получаем: <filter object at 0x01202FE8>
result = list(result) # Приводим к риличному виду
print(result) #  Получаем: [2, 4, 6, 8]

# набор строк
names = ['Max', 'Alex', 'Kate']

# Получить строки больше 3-х символов
print(list(filter(lambda x: len(x)>3, names))) # Получаем: ['Alex', 'Kate']
