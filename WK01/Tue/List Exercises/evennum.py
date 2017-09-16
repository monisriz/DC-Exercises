# #4 Even numbers

numlist = [10, 2, 5, 6, 11, 3, 4, 7]
length = len(numlist)


for i in range(length):
    if numlist[i] % 2 == 0:
        print(numlist[i])
