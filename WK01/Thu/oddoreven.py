# #4 Odd or even

import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 0:
        x = -1
        return x
    else:
        x = 1
        return x

xs = list(range(-5,6))
ys = []

for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.show()
