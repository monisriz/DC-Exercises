# Artistic Project 3    DigitalCrafts logo

from turtle import *

setup (width=800, height=800)

t1 = Turtle()       # turtle for the left side of the logo
t2 = Turtle()       # turtle for the left side of the logo

t1.up()             # pick up pen to avoid leaving a trail upon drawing
t2.up()             # pick up pen to avoid leaving a trail upon drawing

t1.hideturtle()     # hide turtle for a cleaner look
t2.hideturtle()     # hide turtle for a cleaner look

t1.speed(0)         # max speed for faster animation
t2.speed(0)         # max speed for faster animation

t1.goto(-370,90)    # set starting position for left turtle
t2.goto(370, -50)   # set starting position for right turtle

t2.left(180)        # flip right turtle to face the correct way

def tz1(t,c):       # draw trapezoid. args: t=turtlename, c=pen/fill color
    t.color(c)
    t.begin_fill()
    t.forward(180)
    t.left(120)
    t.forward(100)
    t.left(60)
    t.forward(80)
    t.left(60)
    t.forward(100)
    t.end_fill()

def rbus1(t,c):     # draw rhombus. args: t=turtlename, c=pen/fill color
    t.color(c)
    t.begin_fill()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.end_fill()

def tang1(t,c):     # draw triangle1. args: t=turtlename, c=pen/fill color
    t.color(c)
    t.begin_fill()
    t.forward(80)
    t.left(120)
    t.forward(80)
    t.left(120)
    t.forward(80)
    t.end_fill()

def tang2(t,c):     # draw triangle1. args: t=turtlename, c=pen/fill color
    t.color(c)
    t.begin_fill()
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.left(120)
    t.forward(100)
    t.end_fill()

# Left half of the logo
def left():
    tz1(t1,("#7EC04B"))
    t1.left(120)
    t1.forward(180)
    rbus1(t1,("#5D8842"))
    t1.left(120)
    t1.forward(100)
    tz1(t1,("#7EC04B"))
    t1.left(120)
    t1.forward(80)
    t1.left(60)
    tang2(t1,("#467866"))
    tang1(t1,("#2A94CE"))
    t1.left(120)
    t1.forward(80)
    t1.right(60)
    tz1(t1,("#288ECA"))
    t1.left(180)
    rbus1(t1,("#1771B5"))
    t1.forward(-20)
    tang2(t1,("#1B67A1"))
    t1.left(120)
    t1.forward(100)
    tang2(t1,("#1F84B1"))
    t1.left(120)
    t1.forward(20)
    t1.right(60)
    tang1(t1,("#288ECA"))

# Right half of the logo
def right():
    tz1(t2,("#F79E34"))
    t2.left(120)
    t2.forward(180)
    rbus1(t2,("#F27830"))
    t2.left(120)
    t2.forward(100)
    tz1(t2,("#FBB231"))
    t2.left(120)
    t2.forward(80)
    t2.left(60)
    tang2(t2,("#C08258"))
    tang1(t2,("#BBBDBF"))
    t2.left(120)
    t2.forward(80)
    t2.right(60)
    tz1(t2,("#BBBDBF"))
    t2.left(180)
    rbus1(t2,("#A6AAAB"))
    t2.forward(-20)
    tang2(t2,("#939597"))
    t2.left(120)
    t2.forward(100)
    tang2(t2,("#6E6E71"))
    t2.left(120)
    t2.forward(20)
    t2.right(60)
    tang1(t2,("#A6AAAB"))

left()
right()

mainloop()
