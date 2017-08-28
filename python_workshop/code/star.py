from turtle import *

tom=Turtle()

for i in range(0,10):
    tom.forward(100)
    if i%2==0:
        tom.right(144)
    else:
        tom.left(72)

tom.hideturtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="star.eps")

tom.getscreen()._root.mainloop()

