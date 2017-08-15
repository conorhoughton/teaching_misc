from turtle import *

tom=Turtle()

tom.forward(100)
tom.right(90)
tom.forward(100)
tom.right(90)
tom.forward(100)
tom.right(90)
tom.forward(100)
tom.right(90)


#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="right_angle.eps")

tom.getscreen()._root.mainloop()

