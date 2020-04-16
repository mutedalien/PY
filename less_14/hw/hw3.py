# 3. Напишите функцию которая принимает на вход список.
# Функция создает из этого списка новый список из квадратных корней чисел
# (если число положительное) и самих чисел (если число отрицательное)
# и возвращает результат (желательно применить генератор и тернарный оператор
# при необходимости).
# В результате работы функции исходный список не должен измениться.

import math

old_list = [1, -1, 2, -2, 4, 5, 6, 7, 8, 9]

def new_sqrt_list(input_list):
    # так
    input_list = input_list.copy()
    for i in range(len(input_list)):
        number = input_list[i]
        if number > 0:
            input_list[i] = math.sqrt(number)
            # else:
            #       del input_list[i]
    return input_list

    # или так:
    result = [math.sqrt(number) for number in input_list if number > 0]
    return result


result = new_sqrt_list(old_list)
print(result)
print(old_list)