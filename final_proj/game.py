import random


def game():
    number = random.randint(1, 100)
    # print (number)

    user_number = None
    count = 0
    levels = {1: 10, 2: 5, 3: 3}

    level = int(input('Выберите уровень сложности: '))
    max_count = levels[level]

    # Добавим количество игроков
    user_count = int(input('Введите количество игроков: '))
    users = []
    for i in range(user_count):
        user_name = input(f'Введите имя игрока {i}: ')
        users.append(user_name)

    print(users)

    is_winner = False
    winner_name = None

    while not is_winner:
        count += 1
        if count > max_count:
            print('Все игроки продули :(')
            break
        print(f'Попытка № {count}')
        for user in users:
            print(f'Ход игрока {user}')
            # Шаг 2. Предложить юзеру ввести число
            user_number = int(input('Введите число: '))
            if user_number == number:
                is_winner = True
                winner_name = user
                break
            # Шаг 3. Сравнение чисел. Вывод результата
            elif number > user_number:
                print('Ваше число меньше загаданного')
            else:
                print('Ваше число больше загаданного')
    else:
        print(f'Победа достается {winner_name}!')
