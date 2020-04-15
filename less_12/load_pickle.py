# модуль pickle для загрузки в файл
import pickle

# открываем файл
with open ('person.dat', 'rb') as f:
    # сразу пишем объект целиком с помощью pickle
    person = pickle.load(f)

print(person)