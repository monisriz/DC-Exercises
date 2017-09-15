# Exercise 3    shapes2.py
from turtle import *
# A function to draw a polygon with 'n' number of sides of
# size 'x'. Other parameters: pen color 'p' and fill color 'f'.
def polygon(n, x, p, f):
    color(p, f)
    begin_fill()
    for i in range(n):
        forward(x)
        left(360/n)
    end_fill()


# The above function, polygon(), does not work for
# drawing a star as it is not a polygon.
# Other parameters: pen color 'p' and fill color 'f'.
def star(x, p, f):
    color(p, f)
    begin_fill()
    for i in range(5):
        forward(x)
        left(144)
    end_fill()
