import random
from select import select
from typing import List, Union, Tuple
import card

class Deck:
    def __init__(self):

        self.cards = []
        self.build()
    
    def build(self):
        for x in ["d", "c", "h", "s"]:
            for v in range(1,14):
                self.cards.append(card.Card(x, v))
    
    def shuffle(self):
        print("shuffle")

    def show(self):
        for c in self.cards:
            c.show


        
        