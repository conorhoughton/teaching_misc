from turtle import *

tom=Turtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="turtle_doing_nothing.eps")

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

