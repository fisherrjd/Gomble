import random
from select import select
from typing import List, Union, Tuple



class Die:
    def __init__(self, sides):
        self.sides = sides

        
    def roll(self):
        return random.randint(1,self.sides)

    





        

