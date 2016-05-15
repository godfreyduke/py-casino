import random

class Card():
    
    faces = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}

    def __init__(self, card):
        self.suit = card[1]
        self.card = card[0]
        self.flagged = False
        
    def __str__(self):
        return self.card + ' of ' + self.suit
    
    def flag(self):
        self.flagged = True
    
    @property
    def value(self):
        return self.faces.get(self.card, self.card)
    
    @property
    def suit(self):
        return self.suit
    

class Deck():
    def __init__(self, number_of_decks=1):
        suits = ['hearts', 'diamonds', 'clubs', 'spades']
        faces = {'Ace':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':10,'Queen':10,'King':10}
        self.deck = []
        for i in xrange(number_of_decks):
            for face in faces:
                for suit in suits:
                    self.deck.append(Card([face,suit]))
                
    def __str__(self):
        return str([str(x) for x in self.deck])
        
    def shuffle(self, times=1):
        for i in xrange(times):
            random.shuffle(self.deck)
        
    def draw(self):
        return self.deck.pop(0)
        
    def cards_remaining(self):
        return len(self.deck)
        
class Hand():
    def __init__(self):
        self.hand = []
    
    def __str__(self):
        return str([str(x) for x in self.hand])
                
    def draw_from(self, deck, times=1):
        for i in xrange(times):
            self.hand.append(deck.draw())
    
    def new_hand(self):
        self.hand = []
        
    def discard(self,indicies):
        remaining = []
        
        for index in indicies:
            self.hand[index].flag()
            
        for card in self.hand:
            if not card.flagged:
                remaining.append(card)
                
        self.hand = remaining
        
    @property
    def value(self):
        value = 0
        for card in self.hand:
            value+= card.value
        for card in self.hand:
            if card.card == 'Ace':
                if value <= 10:
                    return value+10
        return value
    @property
    def cards(self):
        cards = []
        for card in self.hand:
            cards.append(str(card))
        return cards
        
    
class VideoPoker():
    def __init__(self):
        self.deck = Deck()
        self.hand = Hand()        
        self.deck.shuffle(times=5)
        
    def new_game(self):
        self.__init__()
        return self.start()
        
    def start(self):
        self.hand.draw_from(self.deck, times=5)
        return self.show()
        
    def discard(self, indicies):
        self.hand.discard(indicies)
        self.hand.draw_from(self.deck, times=len(indicies))
        return self.show()
        
    def show(self):
        return self.hand.cards

