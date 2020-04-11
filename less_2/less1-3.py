name = input('Введите имя: ')
surname = input('Введите фамилию: ')
age = int(input('Введите возраст: '))
weight = int(input('Введите вес: '))
if age <= 30 and 50 <= weight <= 120:
    print(name, surname, "возраст:", age, "вес:", weight, '- У вас хорошее состояние')
elif 30 < age < 40 and (weight < 50 or weight > 120):
    print(name, surname, "возраст:", age, "вес:", weight, '- Вам следует заняться собой')
elif 30 < age < 40 and 50 <= weight <= 120:
    print(name, surname, "возраст:", age, "вес:", weight, '- Вы хорошо следите за собой!')
elif age >= 40 and (weight < 50 or weight > 120):
    print(name, surname, "возраст:", age, "вес:", weight, '- Вам следует обратится к врачу!')
elif age >= 40 and 50 <= weight <= 120:
    print(name, surname, "возраст:", age, "вес:", weight, '- Хорошее состояние!')
else:
    print(name, surname, "возраст: ", age, "вес", weight, '- Нет данных')