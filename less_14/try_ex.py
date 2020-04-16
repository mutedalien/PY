# исключения и исключительные ситуации
number = int(input('Введите число: '))
try:
    result = 100 / number # при вводе 0 произойдет ZeroDivisionError
except:
    print('Деление на 0')
print('Конец')