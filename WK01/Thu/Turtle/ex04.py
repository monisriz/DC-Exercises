# Exercise 4    A night sky full of stars
import random
from turtle import *
setup (width=800, height=800)

starqty = random.randrange(50, 100)         # random number of stars drawn
bgcolor("black")                            # background color
color("white", "white")                     # pen and fill color
speed(0)                                    # set speed for faster animation
hideturtle()                                # hide turtle for a cleaner look

for i in range(starqty):
    randx = random.randrange(-390,390)      # random x-coordinate
    randy = random.randrange(-390,391)      # random y-coordinate
    penup()
    goto(randx, randy)                      # go to a random drawing position
    pendown()
    sz = random.randrange(5, 15)            # random star size
    begin_fill()
    for i in range(5):                      # function to draw a star
        forward(sz)
        left(72)
        forward(sz)
        right(144)
    end_fill()
    penup()

mainloop()
