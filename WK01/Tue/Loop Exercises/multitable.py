# #9 Multiplication table

for i in range(1,11):
    print("\n"+"="*12)
    print("Table for {}".format(i))
    print("="*12)
    for j in range(1,11):
        print("{} x {} = {}".format(i,j,i*j))
