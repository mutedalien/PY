# Пользователь вводит три числа.
# Найти минимальное из них, максимальное из них, их сумму и вывести результат.

numbers = []

for i in range(3):
    number = int(input('Введите число: '))
    numbers.append(number)

print(max(numbers))
print(min(numbers))
print(sum(numbers))
