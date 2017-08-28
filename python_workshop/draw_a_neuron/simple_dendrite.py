from turtle import *
from math import *
import random as rnd

def dendrite(length,width):
    
    if width==0:
        return

    tom.width(width)

    x=tom.xcor()
    y=tom.ycor()

    left_branch=False
    if rnd.random()<left_branch_prob:
        left_branch=True
    left_branch_location=length*rnd.random()
    
    right_branch=False
    if rnd.random()<right_branch_prob:
        right_branch=True
    right_branch_location=length/3.*(1+rnd.random())
    
    if right_branch_location<left_branch_location:
        tom.forward(right_branch_location)
        if right_branch:
            tom.right(angle)
            dendrite(length*factor,width-1)
            tom.left(angle)
        tom.forward(left_branch_location-right_branch_location)
        if left_branch:
            tom.left(angle)
            dendrite(length*factor,width-1)
            tom.right(angle)
        

    if left_branch_location<right_branch_location:
        tom.forward(left_branch_location)
        if left_branch:
            tom.left(angle)
            dendrite(length*factor,width-1)
            tom.right(angle)
        tom.forward(right_branch_location-left_branch_location)
        if right_branch:
            tom.right(angle)
            dendrite(length*factor,width-1)
            tom.left(angle)


    tom.penup()
    tom.setx(x)
    tom.sety(y)
    tom.width(width+1)
    tom.pendown()
    return

left_branch_prob=0.75
right_branch_prob=0.75
factor=0.75
angle=30

tom=Turtle()

tom.penup()
tom.goto(x=0,y=-150)
tom.left(90)
tom.pendown()

dendrite(200,7)



tom.hideturtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="simple_dendrite.eps")

tom.getscreen()._root.mainloop()

