from random import shuffle

# Attribute class
class Attribute(object):

    # Initialize an attribute with it's properties
    def __init__(self, name, value):
        self.name = name
        self.value = value

# Card class
class Card(object):

    # Initialize the card with no attributes
    # attributes property is a key-value dictionary
    def __init__(self):
        self.attributes = {}

    # Iterable over attributes, returns attribute value
    def __iter__(self):
        return self.attributes.itervalues()

    # Adds an attribute to the card
    # key is the 'name' property, value is the 'value' property
    def add_attribute(self, attribute):
        self.attributes[attribute.name] = attribute.value

# Deck class
class Deck(object):
    
    # Initialize with no cards
    def __init__(self):
        self.cards = []
        self.index = 0

    # len returns number of cards in deck
    def __len__(self):
        return len(self.cards)

    # iterable over cards in deck
    def __iter__(self):
        return self

    def next(self):
        if self.index == len(self.cards):
            self.index = 0
            raise StopIteration
        self.index += 1
        return self.cards[self.index-1]

    # Add a card to the deck
    def add_card(self, card):
        self.cards.append(card)

    # Shuffle the deck of cards
    def shuffle_cards(self):
        shuffle(self.cards)

    # Deal a card from the top of the deck
    def deal_card(self):
        return self.cards.pop(0)

    # Deal a card from the bottom of the deck
    def deal_card_cheat(self):
        return self.cards.pop(-1)

    # Cut the deck
    def cut_deck(self, loc):
        self.cards = self.cards[loc:] + self.cards[0:loc]

