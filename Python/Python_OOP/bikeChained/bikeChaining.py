class bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print "price: $" + str(self.price)
        print "max speed: " + str(self.max_speed) + "MPH"
        if self.miles < 0:
            self.miles = 0
            print "miles: "  + str(self.miles)   #not sure if this is what was being asked to do when dealing with a negative number.
            return self
        else:
            print "miles: "  + str(self.miles)
            return self

    def ride(self):
        print "Riding..."
        self.miles += 10
        return self

    def reverse(self):
        print "Reversing... a certain amount of miles"
        self.miles -= 5
        return self

gt = bike(250, 80)
gt.ride().ride().ride().reverse().displayInfo()

print "*********************************"

schwinn = bike(100, 30)
schwinn.ride().ride().reverse().reverse().displayInfo()

print "*********************************"

cannondale = bike(1000, 120)
cannondale.reverse().reverse().reverse().displayInfo()


