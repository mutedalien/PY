# Передаем функцию в другую функцию

def my_filter(numbers, function): # Даем на вход переменную и функцию для ее обработки
    result = []
    for number in numbers:
        # Если функция вернет True, то запишем результат
        if function(number):
            result.append(number)
    return result

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

def is_even(number):
    return number % 2 == 0
print(my_filter(numbers, is_even))

def is_not_even(number):
    return number % 2 != 0
print(my_filter(numbers, is_not_even))

def big_4(number):
    return number > 4
print(my_filter(numbers, big_4))

# lambda - функция

print(my_filter(numbers, lambda number: number % 2 == 0))
print(my_filter(numbers, lambda number: number % 2 != 0))
print(my_filter(numbers, lambda number: number > 4))
