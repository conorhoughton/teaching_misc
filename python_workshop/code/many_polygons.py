from turtle import *

def polygon(n):

    for i in range(0,n):
        tom.forward(100)
        tom.right(360.0/n)


tom=Turtle()

repeats=8
polygon_sides=5

for i in range(0,repeats):
    polygon(polygon_sides)
    tom.right(360.0/repeats)


#these two lines are for saving the image
ts = tom.getscreen()
ts.getcanvas().postscript(file="many_polygons.eps")

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

