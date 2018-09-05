import numpy as np
import matplotlib.pyplot as plt


def example_function(x):
    return np.sin(x)

x0=0
x1=2*np.pi
delta_x=0.01

fxn_values=[]
x_values=[]

x=x0

while x<x1:
    new_f=example_function(x)
    x_values.append(x)
    fxn_values.append(new_f)
    x+=delta_x


plt.plot(x_values,fxn_values)
plt.show()
