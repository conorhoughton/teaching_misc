from math import *

class W_nullkline:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __call__(self,v):
        return (v+self.a)/self.b


class V_nullkline:

    def __init__(self,input):
        self.input=input

    def __call__(self,v):
        return v-pow(v,3)+self.input

input=0.75
a=0.7
b=0.8


v_nullkline=V_nullkline(input)
w_nullkline=W_nullkline(a,b)

v=-3.0
v_final=3.0

delta_v=0.01


while v<v_final:
    print v,v_nullkline(v),w_nullkline(v)
    v+=delta_v
