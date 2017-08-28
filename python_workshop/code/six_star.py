from turtle import *

tom=Turtle()

for i in range(0,12):
    tom.forward(80)
    if i%2==0:
        tom.right(120)
    else:
        tom.left(60)

#this hides the turtle
tom.hideturtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="six_star.eps")

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

