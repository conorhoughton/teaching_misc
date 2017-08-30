import timeit

class Neuron:

    def __init__(self,v_t,e_l,v_r,t_m):
        self.v_t=v_t
        self.e_l=e_l
        self.v_r=v_r
        self.t_m=t_m
        self.v=v_r

    def dvdt(self,ie,v):
        return (self.e_l-v+ie)/self.t_m

    def update(self,ie,delta_t):
	 k1=self.dvdt(ie,self.v)
	 k2=self.dvdt(ie,self.v+0.5*k1*delta_t)
	 k3=self.dvdt(ie,self.v+0.5*k2*delta_t)
	 k4=self.dvdt(ie,self.v+k3*delta_t)
	 self.v+=(k1+2*k2+2*k3+k3)*delta_t/6.0
	 if self.v>self.v_t:
             self.v=self.v_r
             return True
         False

def run_neuron(t1):
    mV=0.001
    ms=0.001

    neurons=[Neuron(-55*mV,-87*mV,-87*mV,10*ms) for i in range(1000)]

    t=0.0

    ie=33*mV

    delta_t=ms

    while t<t1:
        spikes=[]
        for i,neuron in enumerate(neurons):
            if neuron.update(ie,delta_t):
                spikes.append(i)
        t+=delta_t

run_neuron(10.)
