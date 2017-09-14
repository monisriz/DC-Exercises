# #7 Multiply a list

numlist = [10, 2, 5, 6, 11, 3, 4, 7]
length = range(len(numlist))
factor = 2
newlist = []

for i in length:
    newnum = numlist[i] * factor
    newlist.append(newnum)
print("\nNew list after multiplying by a factor of {}:\n{}".format(factor,newlist))
