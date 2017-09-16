# #4 Even numbers

numlist = [10, 2, 5, 6, 11, 3, 4, 7]
length = len(numlist)

print("The even numbers in the list are:")
for i in range(length):
    if numlist[i] % 2 == 0:
        print(numlist[i])
