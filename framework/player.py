from framework import Hand, Deck


class Player(object):
    def __init__(self, name, credits=100, hand=None, deck=None):
        self.name = name
        self.credits = credits

        if deck is None:
            self.deck = Deck()
        else:
            self.deck = deck

        if hand is None:
            self.hand = Hand(deck=self.deck)
        else:
            self.hand = hand
        
    def bet(self, amount):
        if amount > self.credits:
            raise ValueError('Not enough credits')
        else:
            self.credits -= amount


class Dealer(Player):
    def __init__(self):
        super(Dealer, self).__init__(name='The Dealer', credits=1000000000)
