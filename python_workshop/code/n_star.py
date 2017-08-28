from turtle import *

tom=Turtle()

n=8

for i in range(0,2*n):
    tom.forward(80)
    if i%2==0:
        tom.right(720./n)
    else:
        tom.left(360./n)

#this is needed in some situations to keep the turtle console open
tom.hideturtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="n_star.eps")

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

