from __future__ import print_function

import nose.tools as nt
from setest.deckofcards import FrenchCard, CatanDevCard, Deck, FrenchDeck
from setest.decks.frenchplayingcards import suit_list, rank_list


class TestCards(object):

    def test_french_card(self):
        with nt.assert_raises(ValueError):
            bad_suit = FrenchCard('foosuit', 'A')

        with nt.assert_raises(ValueError):
            bad_rank = FrenchCard('hearts', 'FooRank')

        with nt.assert_raises(ValueError):
            bad_card = FrenchCard('foo', 'bar')

        new_card = FrenchCard('hearts', 'A')
        nt.assert_equal(new_card.suit, 'hearts')
        nt.assert_equal(new_card.rank, 'A')

        joker = FrenchCard(joker=True)
        nt.assert_true(joker)

    def test_catan_card(self):
        with nt.assert_raises(ValueError):
            bad_dev = CatanDevCard('foocard')

        dev_card = CatanDevCard('knight')
        nt.assert_equal(dev_card.kind, 'knight')

class TestDeck(object):

    def setup(self):
        self.deck = FrenchDeck()

    def test_empty_deck(self):
        deck = Deck()
        nt.assert_equal(len(deck), 0)
        nt.assert_list_equal([x for x in deck], [])

    def test_deck_len(self):
        nt.assert_equal(len(self.deck), 52)

    def test_deck_iter(self):
        all_cards = [c for c in self.deck]
        nt.assert_equal(type(all_cards[0]), FrenchCard)
        ranks = [c.rank for c in self.deck]
        suits = [c.suit for c in self.deck]

        nt.assert_items_equal(set(ranks), set(rank_list))
        nt.assert_items_equal(set(suits), set(suit_list))

    def test_deck_shuffle(self):
        shuffled_deck = FrenchDeck()
        shuffled_deck.shuffle()

        nt.assert_not_equal(shuffled_deck.cards, self.deck.cards)

    def test_deck_deal(self):
        top_card = self.deck.deal()
        nt.assert_is_instance(top_card, FrenchCard)
        nt.assert_equal(top_card.rank, 'K')
        nt.assert_equal(top_card.suit, 'diamonds')

        for x in range(0, 52, 1):
            self.deck.deal()
        no_card = self.deck.deal()
        nt.assert_equal(no_card, 'No more cards to deal!')

    def test_deck_deal_from_bottom(self):
        bottom_card = self.deck.deal_from_bottom()
        nt.assert_equal(bottom_card.rank, 'A')
        nt.assert_equal(bottom_card.suit, 'hearts')

    def test_cut(self):
        self.deck.cut(4)
        bottom_card = self.deck.deal_from_bottom()
        top_card = self.deck.deal()

        nt.assert_equal(bottom_card.rank, '2')
        nt.assert_equal(bottom_card.suit, 'hearts')

        nt.assert_equal(top_card.rank, 'A')
        nt.assert_equal(top_card.suit, 'diamonds')

class TestFrenchDeck(object):

    def test_add_card(self):
        deck = FrenchDeck()
        with nt.assert_raises(TypeError):
            deck.add_card(CatanDevCard('knight'))

        new_card = FrenchCard('spades', 'A')
        deck.add_card(new_card)

        nt.assert_equal(deck.cards[-1], new_card)

        joker = FrenchCard(joker=True)
        deck.add_card(joker)

        nt.assert_equal(deck.__repr__(),
                        '<French Deck: 54 cards, Jokers: True>')
