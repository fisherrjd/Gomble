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
        print (self.rank, " of ", self.suit)


class Deck:
    def __init__(self):

        self.cards = []
        self.build()
    
    def build(self):
        for x in ["d", "c", "h", "s"]:
            for v in range(1,10):
                self.cards.append(Card(x, v))    
    def shuffle(self):
        print("shuffle")

    def showTop(self):
        topCard = Card(self.cards[1].getSuit, self.cards[1].getRank)
        print(topCard.show)