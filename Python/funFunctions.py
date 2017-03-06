def odd_even():
    for num in range(1, 2000):
        if num % 2 == 0:
            print "The number is " + str(num) + ". This is an even number."
        else:
            print "The number is " + str(num) + ". This is an odd number."

odd_even()



a = [2,3,4,5,6,76]
def multiply(list, multy):
    for x in range(0, len(list)):
        list[x] = list[x]*multy
        return list
        
print multiply(a, 5)