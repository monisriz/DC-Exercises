# #10 Matrix addition II

m1 = [[1, 3, 1], [2, 4, 1], [2, 2, 1]]
m2 = [[5, 2, 1], [1, 0, 1], [1, 1, 1]]
m3 = [[0, 0, 1], [0, 0, 1], [0, 0, 1]]

listsize = len(m1)

for i in range(listsize):
    for j in range(len(m1[i])):
        m3[i][j] = m1[i][j] + m2[i][j]
print("\nThe result is:\n",m3)
