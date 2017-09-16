# #11 De-dup

numlist = [3, 4, 9, 2, 8, 9, 2, 0, 6, 5]
listsize = len(numlist)
newlist = []
for i in range(listsize):
    numlist.sort()
    if i == listsize - 1:
        if i not in newlist:
            newlist.append(i)
    elif numlist[i] != numlist[i + 1]:
        newlist.append(numlist[i])
print("Sorted original list:\t\t",numlist)
print("New list without duplicates:\t",newlist)

# ==A better way==
# newlist = []
# for num in numlist:
#     if num not in newlist:
#         newlist.append(num)
# print("Original list:\t\t",numlist)
# print("Without duplicates:\t",newlist)

# ==An even better way==
# print(list(set(numlist)))
