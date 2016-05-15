from framework import Hand


class Player(object):
    def __init__(self, name, credits=100, hand=Hand()):
        self.name = name
        self.credits = credits
        self.hand = hand
        
    def bet(self, amount):
        if amount > self.credits:
            raise ValueError('Not enough credits')
        else:
            self.credits -= amount


class Dealer(Player):
    def __init__(self):
        super(Dealer, self).__init__(name='The Dealer', credits=1000000000)
