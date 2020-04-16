# исключения и исключительные ситуации
number = int(input('Введите число: '))
try:
    result = 100 / number # при вводе 0 произойдет ZeroDivisionError
except ZeroDivisionError as e:
    print('Попытка деление на 0')
    print('Информация об исключении', e)
except Exception as e:
    print('Неизвестная ошибка')
    print('Информация об исключении', e)