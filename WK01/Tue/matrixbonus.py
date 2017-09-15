# Bonus: Matrix multiplication

m1 = [[2, 3],
     [4, 5]]

m2 = [[5, 4],
     [3, 2]]

m3 = [[0, 0],
     [0, 0]]

for i in range(2):
    for j in range(2):
        if i == 0 and j == 0:
            m3[i + 1][j + 1] = m1[i][j] * m2[i][j] + m1[i + 1][j] * m2[i][j + 1]

        elif i == 0 and j == 1:
            m3[i][j] = m1[i][j - 1] * m2[i][j] + m1[i][j] * m2[i + 1][j]

        elif i == 1 and j == 0:
            m3[i][j] = m1[i][j] * m2[i - 1][j] + m1[i][j + 1] * m2[i][j]

        elif i == 1 and j == 1:
            m3[i -1][j-1] = m1[i - 1][j] * m2[i][j - 1] + m1[i][j] * m2[i][j]

for m in m3:
    print(m)
