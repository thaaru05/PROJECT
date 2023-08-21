from turtle import *
bgcolor('black')
speed(0)
penup()
goto(-100,0)
pendown()

for i in range(10):
    for colours in ['red','blue','cyan','green','yellow','white']:
        color(colours)
        pensize(3)
        circle(150)
        forward(20)