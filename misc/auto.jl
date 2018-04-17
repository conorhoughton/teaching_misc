
function update(weights::Array{Float64},pattern)
    function activation(a::Float64)
        if a>0
            return 1
        end
        -1
    end

    new_pattern=weights*pattern

    map(activation,new_pattern)

end

#------------------

function seven_segment(pattern::Array{Int64})

    function to_bool(a::Int64)
        if a==1
            return true
        end
        false
    end

    function hor(d)
        if d
            println(" _ ")
        else
            println("   ")
        end
    end
    function vert(d1,d2,d3)
        word=""::String
        if d1
            word="|"
        else
            word=" "
        end
        if d3
            word=string(word,"_")
        else
            word=string(word," ")
        end
        if d2
            word=string(word,"|")
        else
            word=string(word," ")
        end 
        println(word)

    end

    pattern_b=map(to_bool,pattern)

    hor(pattern_b[1])
    vert(pattern_b[2],pattern_b[3],pattern_b[4])
    vert(pattern_b[5],pattern_b[6],pattern_b[7])

    number=0
    for i in 1:4
        if pattern_b[7+i]
            number+=2^(i-1)
        end
    end

    println(number)
        



end

six=Int64[1,1,-1,1,1,1,1,-1,1,1,-1]
three=Int64[1,-1,1,1,-1,1,1,1,1,-1,-1]
one=Int64[-1,-1,1,-1,-1,1,-1,1,-1,-1,-1]

seven_segment(three)
seven_segment(six)
seven_segment(one)

#------------------

patterns=[six,three,one]

pattern_length=11

weights=zeros(Float64,pattern_length,pattern_length)

patterns_n=length(patterns)


for pattern in patterns
    weights+=1.0/patterns_n*pattern*transpose(pattern)
end

for i in 1:pattern_length
    weights[i,i]=0.0
end

println("test1")

test=Int64[1,-1,1,1,-1,1,1,-1,-1,-1,-1]

seven_segment(test)

test=update(weights,test)

seven_segment(test)

println("test2")

test=Int64[1,1,1,1,1,1,1,-1,-1,-1,-1]

old_test=0*test

while test!=old_test
    seven_segment(test)
    old_test=test
    test=update(weights,test)
end
