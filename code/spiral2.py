from turtle import *

tom=Turtle()

for i in range(0,30):
    tom.forward(10+10*i)
    tom.right(120)

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="spiral2.eps")

tom.getscreen()._root.mainloop()

