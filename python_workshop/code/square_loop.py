from turtle import *

tom=Turtle()

for i in range(0,4):
    tom.forward(100)
    tom.right(90)

#this is needed in some situations to keep the turtle console open
tom.getscreen()._root.mainloop()

