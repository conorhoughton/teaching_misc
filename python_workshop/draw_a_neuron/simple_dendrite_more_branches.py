from turtle import *
from math import *
import random as rnd

def get_angle(sigma):
#    return rnd.normalvariate(angle,sigma)
    return 2*sigma*rnd.random()-sigma

def bendy_line(length,jacob):
    mini_length=length/5.
    for i in range(5):
        jacob.forward(mini_length)
        jacob.left(rnd.normalvariate(0,5))


def dendrite(length,width,branch_n,factor,sigma,jacob):
    
    if width<1:
        return

    jacob.width(width)

    x=jacob.xcor()
    y=jacob.ycor()
    heading=jacob.heading()

    branches=[]
    number_branches=2+rnd.randrange(branch_n-2)

    for c in range(number_branches):
        branches.append(length*rnd.random())
    
    while len(branches)!=0:
        next_branch=min(branches)
        bendy_line(next_branch,jacob)
        angle=get_angle(sigma)
        jacob.right(angle)
        dendrite(length*factor,width-2,branch_n,factor,sigma,jacob)
        jacob.left(angle)
    
        branches=[b-next_branch for b in branches if b!=next_branch]
        


    jacob.penup()
    jacob.setx(x)
    jacob.sety(y)
    jacob.setheading(heading)
    jacob.width(width+2)
    jacob.pendown()
    return


if __name__ == "__main__":



    jacob=Turtle()

    jacob.penup()
    jacob.goto(x=0,y=-150)
    jacob.left(90)
    jacob.pendown()
    
    jacob.speed(0)
    dendrite(150,7,5,.75,90,jacob)



    jacob.hideturtle()

#these two lines are for saving the image
    ts = jacob.getscreen()
    ts.getcanvas().postscript(file="simple_dendrite.eps")

    jacob.getscreen()._root.mainloop()

 
