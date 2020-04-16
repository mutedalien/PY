# 1: Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

fruits1 = ['apple', 'banana', 'orange', 'kiwi', 'pear']
fruits2 = ['banana', 'kiwi', 'tangerine']

result = []

for fruit in fruits1: # перебираем первый список
    if fruit in fruits2: # если фрукт есть во втором списке
        result.append(fruit) # то добавляем его в результат
print(result)

# теперь делаем тоже самое генератором
result = [fruit for fruit in fruits1 if fruit in fruits2]
print(result)