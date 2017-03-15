class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        

    def display_all(self):
        print "Price: $" + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + self.fuel
        print "Mileage: " + str(self.mileage) + "mpg"
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        print "Tax: " + str(self.tax)


chevy = Car(2000, 35, "full", 15)
chevy.display_all()

print "#######################################"

chevy = Car(2000, 5, "not full", 105)
chevy.display_all()

print "#######################################"

chevy = Car(2000, 15, "kind of full", 95)
chevy.display_all()

print "#######################################"

chevy = Car(2000, 25, "full", 25)
chevy.display_all()

print "#######################################"

chevy = Car(2000, 45, "empty", 25)
chevy.display_all()

print "#######################################"

chevy = Car(20000000, 35, "empty", 15)
chevy.display_all()