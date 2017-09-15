# Exercise 4    A night sky full of stars
import random
from turtle import *
# randx = random.randrange(0,401)
# randy = random.randrange(0,301)
# sz = random.randrange(5, 30)
starqty = random.randrange(50, 200)
bgcolor("black")
color("white", "white")
speed(100)

for i in range(starqty):
    randx = random.randrange(-400,401)
    randy = random.randrange(-300,301)
    penup()
    goto(randx, randy)
    pendown()
    sz = random.randrange(5, 30)
    begin_fill()
    for i in range(5):
        forward(sz)
        left(144)
    end_fill()
    penup()

mainloop()
