def my_f(my_var):
    my_var = 999
    print('Внутри функции:', my_var)

a = 1
my_f(a)
print('После выполнения функции: ', a)

global_var = 1

def my_f2():
    # Локальная переменная
    local_var = 100
    # Используем ее внутри функции
    print(local_var)
    # Глобальная переменная, объявлена в модуле (изменить нельзя)
    print(global_var)

my_f2()
print(global_var)
# Локальная переменная тут недоступна
# print(local_var)

# Здесь пробуем изменить глобальную переменную (не рекомендуется)
def my_f3():
    global global_var
    # Локальная переменная
    local_var = 100
    # Используем ее внутри функции
    print(local_var)
    # Глобальная переменная, объявлена в модуле
    global_var = 999
    print(global_var)

my_f3()
print(global_var)
