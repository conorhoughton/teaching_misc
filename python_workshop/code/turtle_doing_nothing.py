from turtle import *

tom=Turtle()

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="turtle_doing_nothing.eps")


tom.getscreen()._root.mainloop()

