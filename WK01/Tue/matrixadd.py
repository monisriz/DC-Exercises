# #9 Matrix addition

m1 = [[1, 3],[2, 4]]
m2 = [[5, 2],[1, 0]]
m3 = [[0,0],[0,0]]
size = len(m1)

for i in range(size):
    for j in range(size):
        m3[i][j] = m1[i][j] + m2[i][j]
print("\nThe result is: \n",m3)
