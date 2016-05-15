import random
from types import ListType


class Card(object):
    def __init__(self, suit, name, value):
        self.suit = suit
        self.name = name
        self.value = value
        self._flagged = False
        self._discarded = False
        self.extra = {}

    def __str__(self):
        return self.name + ' of ' + self.suit

    def is_flagged(self):
        return self._flagged

    def flag(self):
        self._flagged = True

    def unflag(self):
        self._flagged = False

    def discard(self):
        self._discarded = True

    def is_discarded(self):
        return self._discarded


class Deck(object):
    def __init__(self, number_of_decks=1):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        faces = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
                 'Queen': 10, 'King': 10}
        self.deck = []
        for i in xrange(number_of_decks):
            for face in faces:
                for suit in suits:
                    self.deck.append(Card(name=face, suit=suit, value=faces[face]))

        self.shuffle(7)

    def __str__(self):
        return str([str(x) for x in self.deck])

    def shuffle(self, times=1):
        for i in xrange(times):
            random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop(0)

    def cards_remaining(self):
        return len(self.deck)


class Hand(object):
    def __init__(self, deck=None):
        self.hand = []
        self.deck = deck

    def __str__(self):
        return str([str(x) for x in self.hand])

    def new_deck(self, deck=None):
        if deck is None:
            self.deck = Deck()
        else:
            self.deck = deck

    def draw(self, deck=None, times=1):
        if deck is None and self.deck is None:
            return False

        for i in xrange(times):
            self.hand.append(self.deck.draw())

    def new_hand(self):
        self.hand = []

    def discard(self, index=None, number_of_cards=1):
        if index is not None:
            if type(index) is ListType:
                for pos in index:
                    self.hand[pos].discard()
                    self.hand.pop(pos)
            else:
                self.hand[index].discard()
                self.hand.pop(index)
        elif number_of_cards is not None:
            for i in range(0, number_of_cards):
                self.hand[0].discard()
                self.hand.pop(0)
        else:
            self.new_hand()

    @property
    def value(self):
        value = 0
        for card in self.hand:
            value += card.value
        for card in self.hand:
            if card.card == 'Ace':
                if value <= 10:
                    return value + 10
        return value

    @property
    def cards(self):
        cards = []
        for card in self.hand:
            cards.append(str(card))
        return cards
