string = "If monkeys like bananas, then I must be a monkey!"


print string.find("monkeys")

new_string = string.replace("monkey", "alligator")

print new_string



x = [2,54,-2,7,12,98];
x.sort()
print min(x)
print max(x)



x = ["hello",2,54,-2,7,12,98,"world"];
print x[0] + " " + x[-1]



x = [19,2,54,-2,7,12,98,32,10,-3,6];
x.sort()
sideOne = x[0:len(x)/2]
sideTwo = x[len(x)/2:len(x) - 1]
sideTwo.insert(0, sideOne)
print sideTwo