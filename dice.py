import random



class Die:
    def __init__(self, sides):
        self.sides = sides

        
    def throw(self):
        return random.randint(1,6)


crapDie = Die(6)

tot = crapDie.throw
print(tot)
    





        

