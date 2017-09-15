# Exercise 2    shapes.py
from turtle import *
# A function to draw a polygon with 'n' number of sides of size 'x'.
def polygon(n, x):
    for i in range(n):
        forward(x)
        left(360/n)


# The above function, polygon(), does not work for
# drawing a star as it is not a polygon.
def star(x):
    for i in range(5):
        forward(x)
        left(144)
