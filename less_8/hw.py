# 1 Создайте функцию, принимающую на вход имя, возраст и город проживания человека.
# Функция должна возвращать строку вида «Василий, 21 год(а), проживает в городе Москва»

def person_info (name, age, city):
    result = f'{name}, {age}, год(а) проживает в городе {city}'
    return result
print(person_info('Василий', 21, 'Москва'))
print(person_info('Максим', 21, 'Пермь'))

# Чуть сложнее

name = input("Ваше имя: ")
city = input("Ваш город: ")
age = input("Ваш возраст: ")

def print_date(name, city, age):
    print("{}, {} год(а) проживаeт в городе {}.". format(name, age, city))

print_date(name, city, age)

# 2 Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

def get_max(a, b, c):
    result = max([a, b, c])
    return result
result = get_max(1, 3 , 5)
print(result)
print(get_max(7, 1, 3))

# Чуть сложнее

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

player_name = input('Введите имя игрока')
# Словарь игрока
player = {
    'name': player_name,
    'health': 100,
    'damage': 50
}
# Словарь врага
enemy_name = input('Введите имя врага')
enemy = {
    'name': enemy_name,
    'health': 100,
    'damage': 50
}

def attack(unit, target):
    target['health'] -= unit['damage']

    attack(player, enemy)
    print(enemy)

    attack(enemy, player)
    print(player)

# 4 Давайте усложним предыдущее задание. Измените сущности, добавив новый параметр - armor = 1.2 (величина брони персонажа)
# Теперь надо добавить новую функцию, которая будет вычислять и возвращать полученный урон по формуле damage / armor
# Следовательно, у вас должно быть 2 функции:
# Наносит урон. Это улучшенная версия функции из задачи 3.
# Вычисляет урон по отношению к броне.

player_name = input('Введите имя игрока')
# Словарь игрока
player = {
    'name': player_name,
    'health': 100,
    'damage': 50,
    'armor': 1.2
}
# Словарь врага
enemy_name = input('Введите имя врага')
enemy = {
    'name': enemy_name,
    'health': 100,
    'damage': 50,
    'armor': 1
}

def get_damage(damage, armor):
    return damage / armor

def attack(unit, target):
    damage = get_damage(unit['damage'], target['armor'])
    target['health'] -= damage

attack(player, enemy)
print(enemy)

attack(enemy, player)
print(player)

# Еще вариант

def udarit(kto,komu):
    komu['health']=komu['health']-sila_udara(kto['damage'],komu['armor'])

def sila_udara(damage,armor):
    return damage/armor

player={'name':None, 'health':2000, 'damage':100,'armor':1.2}
enemy={'name':None, 'health':1000, 'damage':50,'armor':1.2}
udarit(player,enemy)
print(enemy['health'])