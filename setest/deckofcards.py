from random import shuffle

from setest.decks import frenchplayingcards as fp
# Card Classes

class FrenchCard(object):

    def __init__(self, suit=None, rank=None, joker=False):
        '''Classic french playing cards, with suits and ranks.

        Parameters
        ----------
        suit: str
        rank: str
        joker: boolean
        '''
        if suit not in fp.suit_list and not joker:
            raise ValueError('Not a valid suit type!')
        if rank not in fp.rank_list and not joker:
            raise ValueError('Not a valid rank type!')
        if not any([suit, rank, joker]):
            raise ValueError('This card must have a suit/rank or be a joker!')

        if joker:
            self.joker = joker
        else:
            self.suit = suit
            self.rank = rank


class CatanDevCard(object):

    def __init__(self, kind):
        '''Catan Development Card

        Parameters
        ----------
        kind: one of 'knight', 'progress', 'vp'
        '''
        if kind not in ['knight', 'progress', 'vp']:
            raise ValueError('This is not a valid Development card type!')

        self.kind = kind

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

