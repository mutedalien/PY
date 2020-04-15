# читаем объект из файла
# открываем файл
with open('person.dat', 'rb') as f:
    # теперь нам надо узнать как мы записывали объект
    # прочитаем файл в список
    result = f.readlines()

# теперь воссоздаем исходный объект
person = {}
# первый элемент в нем
person['name'] = result[0].decode('utf-8').replace('\n', '')
# дальше идут телефоны
phones = []
for bphones in result[1:]:
    phones.append(bphones.decode('utf-8').replace('\n', ''))

person['phones'] = phones

# получили исходный объект. А что будет, если он изменится?
print(person)