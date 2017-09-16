# #6 Print a box

n = int(input("Width?: "))
m = int(input("Length?: "))
print("*"*n)
for j in range(m):
    print("*"+" "*(n-2)+"*")
print("*"*n)
