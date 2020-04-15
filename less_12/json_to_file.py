# модуль json
import json

friends = [
    {'name': 'Max', 'age': 23, 'phones': [123, 345]},
    {'name': 'Leo', 'age': 33}
]
# посмотрим тип объекта
print(type(friends))
# открываем файл
with open('friends.json', 'w') as f:
    # преобразуем список друзей в json и сохраняем в файл
    json_friends = json.dump(friends, f)

# обратно из файла в объект
with open('friends.json', 'r') as f:
    friends = json.load(f)

print(friends)
print(type(friends))