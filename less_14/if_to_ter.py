# слово -> СлОвО

word = 'человечков святослав николаевич'
result = [] # pдесь будут храниться переведенные буквы

# так
for i in range(len(word)): # цикл с индексом по длинне слова
    if i%2 != 0: # ghjdthbv yf четность
        letter = word[i].lower() # переводим в нижний регистр
    else:
        letter = word[i].upper() # иначе переводим в верхний
    result.append(letter) # добавляем в результирующий список нашу букву

result = ''.join(result) # из списка делаем строку
print(result)

# или так
for i in range(len(word)):
    letter = word[i]
    letter = letter.lower() if i%2 != 0 else letter.upper()
    result.append(letter)

result = ''.join(result) # из списка делаем строку
print(result)