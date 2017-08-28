from turtle import *

tom=Turtle()

tom.forward(100)

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="line.eps")

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

