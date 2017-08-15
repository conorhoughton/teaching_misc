from turtle import *

tom=Turtle()



tom.forward(100)

#these two lines are for saving the image
ts = tom.getscreen()
ts.setup(400,400)
ts.getcanvas().postscript(file="line.eps")

tom.getscreen()._root.mainloop()

