require_relative 'mammal'

class Dog < Mammal
    def pet
        @health += 5
    end

    def walk
        @health -= 1
    end
    
    def run
        @health -= 10
    end
    

end

da_dog = Dog.new
3.times do 
    da_dog.walk
end
2.times do
    da_dog.run
end
da_dog.pet

puts da_dog.display_health

