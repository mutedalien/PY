myList = [2, 7, 4, 7, 3, 1, 4, 5, 8, 4, 7, 8, 5, 9]
list = []
for i in myList:
    if myList.count(i) == 1:
        list.append (i)
print(list)

