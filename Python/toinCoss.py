import random

def toss(tossAmount):
    for x in range(1, tossAmount):
        new_toss = random.randint(0,1)
        if new_toss == 1:
            print "fuck"
        else:
            print "shit"

toss(5000)
        