from turtle import *

tom=Turtle()

for i in range(0,8):
    tom.forward(100+10*i)
    tom.right(90)

#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="spiral1.eps")

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

