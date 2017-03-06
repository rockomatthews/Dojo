import random

def grades(students):
    for x in range(0, students):
        score = random.randint(60, 100)
        if score >= 60 and score < 70:
            print "Score: ", score,"; Your grade is D"
        elif score >= 70 and score < 80:
            print "Score: ", score,"; Your grade is C"
        elif score >= 80 and score < 90:
            print "Score: ", score,"; Your grade is B"
        else:
            print "Score: ", score,"; Your grade is A"

grades(10)