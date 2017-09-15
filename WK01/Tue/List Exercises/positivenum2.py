# #6 Positive numbers II

numlist = [-10, 2, 5, -6, 11, 3, -4, 7]
length = range(len(numlist))

newlist = []
for i in length:
    if numlist[i] > 0:
        newlist.append(numlist[i])
print("Positive numbers in the list:\n", newlist)
