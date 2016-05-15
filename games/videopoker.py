from framework import Deck, Hand


class VideoPoker:
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand(deck=self.deck)
        self.deck.shuffle(times=5)

    def new_game(self):
        self.__init__()
        return self.start()

    def start(self):
        self.hand.draw(times=5)
        return self.show()

    def discard(self, indicies):
        self.hand.discard(indicies)
        self.hand.draw(times=len(indicies))
        return self.show()

    def show(self):
        return self.hand.cards

