from turtle import *

class Colors:
    
    def __init__(self,color_v):
        self.color_v=color_v
        self.current=0

    def change_colour(self,jacob):
        self.current+=1
        if self.current==len(self.color_v):
            self.current=0
        jacob.color(self.color_v[self.current])

def curve(arc_length, curvature,steps,jacob):
    small_arc=arc_length/steps
    small_curve=curvature/steps
    for i in range(steps):
        jacob.forward(small_arc)
        jacob.right(small_curve)


jacob=Turtle()
colors=Colors(['green','red','blue','yellow','orange','black'])

for i in range(0,12):
    curve(200,40,30,jacob)
    curve(40,120,10,jacob)
    colors.change_colour(jacob)

#this hides the turtle

jacob.hideturtle()

#these two lines are for saving the image
ts = jacob.getscreen()
ts.getcanvas().postscript(file="spirograph.eps")

#this is needed in some situations to keep the turtle console open
jacob.getscreen()._root.mainloop()

