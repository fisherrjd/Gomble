from os import readlink
import random
from typing import List, Union, Tuple



class Card:
    def __init__(self, suit, rank):
        self.ranks = [None, "Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]
        self.rank = self.ranks[rank]
        self.suits = {"d": "Diamonds", "c": "Clubs", "h": "Hearts", "s": "Spades"}
        self.suit = self.suits[suit]
        self.value = -1

    def getRank(self):
        return self.rank

    def getSuit(self):
        return self.suits

    def bjValue(self):
        if self.rank == "Ace":
            self.value = 1
        elif self.rank == "Jack" or "Queen" or "King":
            self.value = 10
        else:
            self.value = self.rank

    def show(self):
        print (self.value + "of" + self.rank)

card = Card("d", 2)

