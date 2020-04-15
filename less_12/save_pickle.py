# модуль pickle для загрузки в файл
import pickle

person = {'name': 'Max', 'phones': [123, 345], 'age': 20} # можно добавлять сколько угодно параметров

# открываем файл
with open ('person.dat', 'wb') as f:
    # сразу пишем объект целиком с помощью pickle
    pickle.dump(person, f)

print('Щбъект записан')