# #1 Sum the numbers

numsum = 0
numlist = [10, 2, 5, 6, 11, 3, 4, 7]
length = range(len(numlist))

for i in length:
    numsum = numsum + numlist[i]
    i += 1
print("The sum of the numbers in the list is",numsum)
