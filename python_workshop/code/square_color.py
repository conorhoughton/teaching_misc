from turtle import *

tom=Turtle()

colors=['red','green','blue','yellow']

for color in colors:
    tom.pencolor(color)
    tom.forward(100)
    tom.right(90)


#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="square_color.eps")

tom.getscreen()._root.mainloop()

