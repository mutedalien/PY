from random import randint, choice, sample, shuffle
# 1. Загадать случайное число от 0 до 100
print(randint(0, 100))
# 2. Выбрать победителя лотереи из списка players
players = ['Max', 'Leo', 'Kate', 'Ron', 'Bill']
print(choice(players))
# 3. Выбрать 3-х победителей лотереи из списка players
print(sample(players, 3))
# 4. Перемешать карты в стопке (списке) cards
cards = ['6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
print(cards)
shuffle(cards)
print(cards)