

function seven_segment(digit::Array{Bool})
    
    function hor(d)
        if d
            println(" - ")
        else
            println("   ")
        end
    end
    function vert(d1,d2)
        if d1 && d2
            println("| |")
        elseif d1
            println("|  ")
        elseif d2
            println("  |")
        else
            println("   ")
        end
    end

    hor(digit[1])
    vert(digit[2],digit[3])
    hor(digit[4])
    vert(digit[5],digit[6])
    hor(digit[7])

    number=0
    for i in 1:4
        if digit[7+i]
            number+=2^(i-1)
        end
    end

    println(number)
        



end

eight=[true,true,true,true,true,true,true,false,false,false,true]
three=[true,false,true,true,false,true,true,true,true,false,false]

seven_segment(three)
seven_segment(eight)

    
