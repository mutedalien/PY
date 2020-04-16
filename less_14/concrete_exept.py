# исключения и исключительные ситуации
number = int(input('Введите число: '))
try:
    result = 100 / number # при вводе 0 произойдет ZeroDivisionError
except ZeroDivisionError:
    print('Попытка деление на 0')
except Exception:
    print('Неизвестная ошибка')