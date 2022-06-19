#smile

import random
import turtle
t = turtle.Pen()
t.speed(0)
t.hideturtle()
turtle.bgcolor('black')

def draw_smile(x, y):
    t.penup()
    t.setpos(x, y)
    t.pendown()
    #Head
    t.pencolor('yellow')
    t.fillcolor('yellow')
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    #left eye
    t.setpos(x-15, y+60)
    t.fillcolor('blue')
    t.begin_fill()
    t.circle(10)
    t.end_fill()
    #right eye
    t.setpos(x+15, y+60)
    t.fillcolor('blue')
    t.begin_fill()
    t.circle(10)
    t.end_fill()    
    #roth
    t.setpos(x-25, y+40)
    t.pencolor('black')
    t.width(10)
    t.goto(x-10, y+20)
    t.goto(x+10, y+20)
    t.goto(x+25, y+40)
    t.width(1)
turtle.onscreenclick(draw_smile)
input()

