
mutable struct Neuron
       v_t::Float64
       e_l::Float64
       v_r::Float64
       t_m::Float64
       v::Float64
end

function dvdt(neuron::Neuron,ie::Float64,v::Float64)
	 (neuron.e_l-v+ie)/neuron.t_m
end

function update(neuron::Neuron,ie::Float64,delta_t::Float64)
	 spiked=false
	 k1=dvdt(neuron,ie,neuron.v)
	 k2=dvdt(neuron,ie,neuron.v+0.5k1*delta_t)
	 k3=dvdt(neuron,ie,neuron.v+0.5k2*delta_t)
	 k4=dvdt(neuron,ie,neuron.v+k3*delta_t)
	 neuron.v+=(k1+2k2+2k3+k3)*delta_t/6.0
	 if neuron.v>neuron.v_t
	    neuron.v=neuron.v_r
	    spiked=true
	 end
	 spiked
end

function run_neuron(t1::Float64)

	 mV=0.001::Float64
	 ms=0.001::Float64

	 neurons=[Neuron(-55*mV,-87*mV,-87*mV,10*ms,-87*mV) for i in 1:1000]

	 t=0.0::Float64


	 ie=33*mV

	 delta_t=ms
	
	 while t<t1
	        spikes=Int64[]
		for (i,neuron) in enumerate(neurons)
      	       	   if update(neuron,ie,delta_t)
		      push!(spikes,i)
		   end
		end
	       t+=delta_t	       
	 end
end

run_neuron(10.0)