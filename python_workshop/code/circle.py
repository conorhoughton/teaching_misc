from turtle import *

tom=Turtle()

radius=100
step_size=2*3.141592*radius/360


for i in range(0,360):
    tom.forward(step_size)
    tom.right(1)


#this hides the turtle
tom.hideturtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="circle.eps")

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

