import random

words_list = ('автострада', 'бензин', 'инопланетянин', 'самолет',
              'библиотека', 'шайба', 'олимпиада', 'зима', 'пальма')


secret_word = random.choice(words_list)
print(secret_word)

gamer_word = ['*'] * len(secret_word)
print(''.join(gamer_word))

# gamer_word[2] = 'г'
# print(''.join(gamer_word))

while True:
    letter = input('введите ОДНУ русскую букву: ')
    if len(letter) != 1 or not letter.isalpha():
        # print('....')
        continue

    print('вы ввели:', letter)


print('играйте еще!')
