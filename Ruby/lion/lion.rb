require_relative 'mammal'

class Lion < Mammal

    # def initialize
    #     @health = 170
    # end
    
    def unhealthy_flight
        @health -= 10
        self
    end
    
    def unsuccessfully_attack_town
        @health -= 50
        self
    end
    
    def eat_humans
        @health += 20
        self
    end
    
    def display_health
        puts "I am a lion"
        super
    end
    

end

larry_the = Lion.new
larry_the.unsuccessfully_attack_town.unsuccessfully_attack_town.unsuccessfully_attack_town.eat_humans.eat_humans.unhealthy_flight.unhealthy_flight.display_health
