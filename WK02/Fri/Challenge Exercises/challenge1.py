

def collatz(num):
    coll = []

    while num > 1:
        if num % 2 == 0:
            nnum = num / 2
            coll.append(num)
            num = nnum
        else:
            nnum = (num * 3) + 1
            coll.append(num)
            num = nnum
    for i in coll:
        print(i)

collatz(5)
