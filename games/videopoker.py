from framework import Deck, Hand
from framework.terminal import Terminal
from types import IntType


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
        if type(indicies) is IntType:
            indicies = [indicies]

        self.hand.discard(index=indicies)
        self.hand.draw(times=len(indicies))

    def show(self):
        card_index = 0
        for card in self.hand:
            card_index += 1
            print "%i) %s " % (card_index, card)

        return self.hand.cards


if __name__ == "__main__":
    poker = VideoPoker()

    poker.start()
    discard_1_input = raw_input("Pick cards to discard... (ex. 1 4):\n")

    if len(discard_1_input) > 1:
        discard_1_input = discard_1_input.split(" ")
    else:
        discard_1_input = [discard_1_input]

    discards = []

    for discard in discard_1_input:
        discards.append(int(discard) - 1)

    poker.discard(discards)
    Terminal.clear_screen()
    print "Here are your new cards: \n"
    poker.show()
