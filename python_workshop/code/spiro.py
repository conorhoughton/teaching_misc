from turtle import *

tom=Turtle()

radius=150
step_size=2*3.141592*100/360


for j in range(0,12):
    for i in range(0,120):
        tom.forward(step_size)
        tom.right(1)
    tom.right(90)

tom.hideturtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="spiro.eps")

tom.getscreen()._root.mainloop()

