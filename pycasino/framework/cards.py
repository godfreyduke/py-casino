import random
from types import ListType


class Card(object):
    def __init__(self, suit, name, value):
        """Card Object

        This Object holds the properties of a card, which is a child of a Deck.

        Args:
            suit (string): The suit of the card. (Spade, Club, Diamond, Heart)
            name (string): The label for the card. (Ace, 2, Queen, King)
            value (integer): The numerical value of the card.

        """
        self.suit = suit
        self.name = name
        self.value = value
        self._flagged = False
        self._discarded = False

    def __str__(self):
        return self.name + ' of ' + self.suit

    def is_flagged(self):
        """Check if the card is currently flagged.

        Returns:
            True if flagged.
            False if not flagged.
        """
        return self._flagged

    def flag(self):
        """Mark the card.

        Sets the flag on the card to True.
        """
        self._flagged = True

    def unflag(self):
        """Unmark the card.

        Sets the flag on the card to False."""
        self._flagged = False

    def discard(self):
        """Mark the card as discared."""
        self._discarded = True

    def is_discarded(self):
        """Check if the card has been discarded."""
        return self._discarded


class Deck(object):
    def __init__(self, number_of_decks=1, auto_shuffle=True):
        """Deck object

        This object holds all methods related to Deck operations. This object is the parent to many Cards.

        Args:
            number_of_decks: (Integer) The number of decks that will be included.
            auto_shuffle: (Boolean[True]) If the deck should be shuffled after it is created.
        """
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        faces = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10,
                 'Queen': 10, 'King': 10}
        self.deck = []
        for i in xrange(number_of_decks):
            for face in faces:
                for suit in suits:
                    self.deck.append(Card(name=face, suit=suit, value=faces[face]))

        if auto_shuffle:
            self.shuffle(7)

    def __str__(self):
        return str([str(x) for x in self.deck])

    def shuffle(self, times=1):
        """Shuffle the deck"""
        for i in xrange(times):
            random.shuffle(self.deck)

    def draw(self):
        """Draw a card off the top of the deck."""
        return self.deck.pop(0)

    def cards_remaining(self):
        """Check the number of cards left in the deck.

        Returns:
            The number of cards left in the deck.
        """
        return len(self.deck)


class Hand(object):
    def __init__(self, deck=None):
        self.hand = []
        self.deck = deck

    def __list__(self):
        return self.hand

    def __iter__(self):
        for card in self.hand:
            yield card

    def __len__(self):
        return len(self.hand)

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
