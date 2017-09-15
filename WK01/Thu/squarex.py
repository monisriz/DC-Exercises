# #3 Square of x

import matplotlib.pyplot as plot

def f(x):
    return x ** 2
xs = list(range(-100, 101))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
