from turtle import *
from math import *
import random as rnd
from simple_dendrite_more_branches import *

jacob=Turtle()
jacob.up()
jacob.goto(x=0,y=-100)
jacob.down()
jacob.speed(0)
jacob.width(3)

turns=[]


for i in range(45):
    jacob.forward(0.75)
    turns.append(rnd.normalvariate(2,1.5))
    jacob.right(turns[-1])
for i in range(10):
    jacob.forward(2)
    turns.append(rnd.normalvariate(0,2))
    jacob.right(turns[-1])
for i in range(45):
    jacob.forward(0.75)
    turns.append(rnd.normalvariate(2,1.5))
    jacob.right(turns[-1])

x=jacob.xcor()
y=jacob.ycor()
jacob.width(2)
jacob.setheading(rnd.normalvariate(270,10))
for i in range(50):
    jacob.forward(2)
    jacob.left(rnd.normalvariate(0,2))
jacob.up()
jacob.setx(x)
jacob.sety(y)
jacob.down()
jacob.setheading(180)
jacob.width(3)
turns.reverse()
for i in range(45):
    jacob.forward(0.75)
    jacob.right(turns.pop())
for i in range(10):
    jacob.forward(2)
    jacob.right(turns.pop())
for i in range(45):
    jacob.forward(0.75)
    jacob.right(turns.pop())

jacob.setheading(90)
dendrite(150,7,7,0.7,60,jacob)

jacob.hideturtle()

ts = jacob.getscreen()
ts.getcanvas().postscript(file="neuron.eps")


jacob.getscreen()._root.mainloop()
