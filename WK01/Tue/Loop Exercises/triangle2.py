# #8 Print a triangle II

n = int(input("Height of triangle?: "))
for i in range(0, n):
        print(" "*(n-1-i),"*"*(i*2+1))
