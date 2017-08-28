from turtle import *

tom=Turtle()

radius=150
step_size=2*3.141592*100/360


for j in range(0,12):
    for i in range(0,120):
        tom.forward(step_size)
        tom.right(1)
    tom.right(90)

#this hides the turtle
tom.hideturtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="spiro.eps")

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

