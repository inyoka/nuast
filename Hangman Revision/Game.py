import random
class Game:
    def __init__(self,deck):
        self.deck = deck
        self.deckname = deck["Properties"["DeckName"]]
        self.decklength = len(deck)-1

    def WordChooser(deck,decklength):
        Choice = random.randint(1,len(decklength))
        print(deck.items())
    