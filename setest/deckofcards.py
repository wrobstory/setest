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
            self.joker = False

    def __repr__(self):
        if self.joker:
            repr_str = 'Joker'
        else:
            repr_str = '{} of {}'.format(self.rank, self.suit)
        return '<FrenchCard: {}>'.format(repr_str)


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

    def __init__(self, cards=None):
        '''Base deck class. Can be empty

        Parameters
        ----------
        cards: iterable
        '''
        self.cards = cards or []

    def __len__(self):
        '''Get current length of deck'''
        return len(self.cards)

    # iterable over cards in deck
    def __iter__(self):
        '''Iterate over deck of cards'''
        for card in self.cards:
            yield card

    def shuffle(self):
        '''Shuffle deck of cards'''
        shuffle(self.cards)

    def deal(self):
        '''Deal a card from the top of the deck'''
        if not self.cards:
            return 'No more cards to deal!'
        return self.cards.pop()

    def deal_from_bottom(self):
        '''Deal a card from the bottom of the deck'''
        if not self.cards:
            return 'No more cards to deal!'
        return self.cards.pop(0)

    def cut(self, loc):
        '''Cut the deck'''
        self.cards = self.cards[loc:] + self.cards[0:loc]

class FrenchDeck(Deck):

    suits = fp.suit_list
    ranks = fp.rank_list

    def __init__(self, jokers=False):
        '''Deck of French playing cards. There are no jokers by default.

        Parameters
        ----------
        jokers: boolean
        '''
        cards = [FrenchCard(suit, rank) for rank in self.ranks for suit in
                 self.suits]
        super(FrenchDeck, self).__init__(cards)

        self.jokers = jokers

    def __repr__(self):
        return "<French Deck: {} cards, Jokers: {}>".format(len(self),
                                                            self.jokers)

    def add_card(self, card):
        '''Add a card to the deck'''
        if not isinstance(card, FrenchCard):
            raise TypeError('Card must be a FrenchCard!')
        if card.joker == True:
            self.jokers = True
        self.cards.append(card)
