from turtle import *
from math import *
import random as rnd

def get_angle():
    return rnd.normalvariate(angle,sigma)

def dendrite(length,width):
    
    if width==0:
        return

    tom.width(width)

    x=tom.xcor()
    y=tom.ycor()

    branches=[]
    number_branches=2+rnd.randrange(branch_n-2)

    for c in range(number_branches):
        branches.append(length*rnd.random())
    
    while len(branches)!=0:
        next_branch=min(branches)
        tom.forward(next_branch)
        if rnd.random()<0.5:
            tom.right(get_angle())
            dendrite(length*factor,width-1)
            tom.left(get_angle())
        else:
            tom.left(get_angle())
            dendrite(length*factor,width-1)
            tom.right(get_angle())
    
        branches=[b-next_branch for b in branches if b!=next_branch]
        


    tom.penup()
    tom.setx(x)
    tom.sety(y)
    tom.width(width+1)
    tom.pendown()
    return


branch_n=5

factor=0.75
angle=30
sigma=5
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

