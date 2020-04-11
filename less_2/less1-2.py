while True:
    a = int(input('введите число от 0 до 10'))
    if a <=0 or a> 10:
        print("введен неверный диапазон значений! ")
    else:
        break
print(a**2)