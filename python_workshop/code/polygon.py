from turtle import *

tom=Turtle()

n=8

for i in range(0,n):
    tom.forward(100)
    tom.right(360.0/n)


#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="polygon.eps")

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

