person = {'name': 'Max', 'phones': {123, 345}}

# откроем файл
with open('person.dat', 'wb') as f:
    # например запишем объект в файл построчно
    # сначала возьмем имя
    name = person['name']
    # добавим перенос строки, переведем в байты и запишем
    f.write(f'{name}\n'.encode('utf-8'))
    # получим телефоны
    phones = person['phones']
    # запишем 1 телефон в новую строку
    for phone in phones:
        f.write(f'{phone}\n'.encode('utf-8'))

print('объект записан')
