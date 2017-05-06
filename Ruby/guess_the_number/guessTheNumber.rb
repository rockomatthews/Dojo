def guess_number(guess)
    number = 25
    if guess > number
        puts "hi"
    elsif guess < number
        puts "low" 
    else
        puts "nice"
    end  
end


guess_number(10)
guess_number(25)
guess_number(100)

