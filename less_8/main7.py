# Набор чисел
numbers = [1, 5, 3, 5, 9, 7, 11]
# Сортировка по возрастанию
print(sorted(numbers))
# Сортировка по убыванию
print(sorted(numbers, reverse=True))

# набор строк
names = ['Max', 'Alex', 'Kate']
# Сортировка по алфавиту
print(sorted(names))

# Города и численность населения
cities = [('Moscow', 1000), ('LosVegas', 500), ('Amsterdam', 2000)]
# Такая сортировка сработает по алфавиту
print(sorted(cities))
# Отсортировать по численности населения
def by_count(city):
    return city[1]
print(sorted(cities, key=by_count))
# lambda-функция
print(sorted(cities, key=lambda city: city[1]))