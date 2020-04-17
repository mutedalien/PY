import random

words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет',
              'библиотека', 'шайба', 'олимпиада', 'зима', 'пальма')

secret_word = random.choice(words_list)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

errors_counter = 0
while True:
    letter = input('введите ОДНУ русскую букву: ')
    if len(letter) != 1 or not letter.isalpha():
        continue

    if letter in secret_word:
        for idx, symbol in enumerate(secret_word):
            # print(idx, symbol)
            if letter == symbol:
                gamer_word[idx] = symbol
        if '*' not in gamer_word:
            print('вы выиграли!!!')
            break
    else:
        errors_counter += 1
        # errors_counter = errors_counter + 1
        print('ошибок допущено', errors_counter)
        if errors_counter == 8:
            print('вы проиграли ;(')
            break

    print(''.join(gamer_word))

print('играйте еще!')
