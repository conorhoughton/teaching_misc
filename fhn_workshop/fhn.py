
from math import *

class V_dot:

    def __init__(self,input):
        self.input=input

    def __call__(self,v,w):
        return v-pow(v,3)/3-w+self.input


class W_dot:

    def __init__(self,a,b,tau):
        self.a=a
        self.b=b
        self.tau=tau

    def __call__(self,v,w):
        return (v+self.a-self.b*w)/self.tau


class Integrate:

    def __init__(self,v_dot,w_dot,delta_t):
        self.v_dot=v_dot
        self.w_dot=w_dot
        self.delta_t=delta_t

    def update(self,v,w):

        k1v=self.v_dot(v,w)*self.delta_t
        k1w=self.w_dot(v,w)*self.delta_t

        k2v=self.v_dot(v+0.5*k1v,w+0.5*k1w)*self.delta_t
        k2w=self.w_dot(v+0.5*k1v,w+0.5*k1w)*self.delta_t

        k3v=self.v_dot(v+0.5*k2v,w+0.5*k2w)*self.delta_t
        k3w=self.w_dot(v+0.5*k2v,w+0.5*k2w)*self.delta_t
        
        k4v=self.v_dot(v+k3v,w+k3w)*self.delta_t
        k4w=self.w_dot(v+k3v,w+k3w)*self.delta_t

        v_new=v+(k1v+2*k2v+2*k3v+k4v)/6
        w_new=w+(k1w+2*k2w+2*k3w+k4w)/6
 
        return (v_new,w_new)

input = 0.75
a = 0.7
b = 0.8
tau=12.5

v_dot=V_dot(input)
w_dot=W_dot(a,b,tau)

delta_t=0.01

integrate=Integrate(v_dot,w_dot,delta_t)

vs=[0.0]
ws=[0.0]

t=0.0
t_final=1000.0

while t<=t_final:
    print t,vs[-1],ws[-1]
    new_v,new_w=integrate.update(vs[-1],ws[-1])
    vs.append(new_v)
    ws.append(new_w)
    t+=delta_t
