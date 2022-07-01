import random



class Die:
    def __init__(self, sides):
        self.sides = sides

class Throw:
    def __init__(self, totDice):
        totDice = totDice
        total = 0;

    def throw(self):
        for x in totDice:
             total += random.randint(1,6)


crapDie = Die(6)

tot =  crapDie.throw()
print (tot)