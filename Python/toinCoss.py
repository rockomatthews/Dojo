import random

def toss(Amount):
    heads = 0
    tails = 0

    for x in range(1, Amount):
        new_toss = random.randint(0,1)
        if round(new_toss) == 1:
            heads += 1
        else:
            tails += 1
    
    print "There were " + str(heads) + " heads and " + str(tails) + " tails flips. (tails always fails)"
            

toss(5000)
        
