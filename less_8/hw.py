# 1 Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

name = input("Ваше имя: ")
city = input("Ваш город: ")
age = input("Ваш возраст: ")

def print_date(name, city, age):
    print("{}, {} год(а) проживаeт в городе {}.". format(name, age, city))

print_date(name, city, age)

# 2 Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def max_digit(*num):
    maximum=0
    for i in num:
        if i>maximum:
            maximum=i
    return maximum

numbers=[]
for i in range(0,3):
    numbers.append(int(input('Введите число : ')))
print(max_digit(numbers[0],numbers[1],numbers[2]))

# 3 Давайте опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения:
# name - строка полученная от пользователя,
# health = 100,
# damage = 50.

# 4 Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.

def udarit(kto,komu):
    komu['health']=komu['health']-sila_udara(kto['damage'],komu['armor'])

def sila_udara(damage,armor):
    return damage/armor

player={'name':None, 'health':2000, 'damage':100,'armor':1.2}
enemy={'name':None, 'health':1000, 'damage':50,'armor':1.2}
udarit(player,enemy)
print(enemy['health'])