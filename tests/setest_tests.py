import nose.tools as nt
from setest.deckofcards import FrenchCard, CatanDevCard, Deck
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

# def test_deck():

	# Create an empty deck
	# thisdeck = Deck()

	# # Cycle through suit and rank lists to generate cards for the deck
	# for suit in suit_list:
	# 	for rank in rank_list:

	# 		# Assign the attributes
	# 		thissuit = Attribute('suit', suit)
	# 		thisrank = Attribute('rank', rank)

	# 		# Create a new card
	# 		thiscard = Card()
	# 		thiscard.add_attribute(thissuit)
	# 		thiscard.add_attribute(thisrank)

	# 		# Add the card to the deck
	# 		thisdeck.add_card(thiscard)

	# # Test the new cards
	# assert_equal(len(thisdeck), 52)
	# assert_equal(thisdeck.cards[0].attributes['suit'], 'hearts')
	# assert_equal(thisdeck.cards[0].attributes['rank'], 'A')
	# assert_equal(thisdeck.cards[51].attributes['suit'], 'diamonds')
	# assert_equal(thisdeck.cards[51].attributes['rank'], 'K')

	# # Test deal methods
	# mycard1 = thisdeck.deal_card()
	# assert_equal(mycard1.attributes['suit'], 'hearts')
	# assert_equal(mycard1.attributes['rank'], 'A')
	# mycard2 = thisdeck.deal_card()
	# assert_equal(mycard2.attributes['suit'], 'hearts')
	# assert_equal(mycard2.attributes['rank'], '2')
	# assert_equal(len(thisdeck), 50)

	# # Add cards back to deck
	# thisdeck.add_card(mycard1)
	# thisdeck.add_card(mycard2)
	# assert_equal(len(thisdeck), 52)

	# # Test dealers cheating method
	# mycheatcard = thisdeck.deal_card_cheat()
	# assert_equal(mycheatcard, mycard2)
	# thisdeck.add_card(mycheatcard)

	# # Test cut method
	# thisdeck.cut_deck(32)
	# assert_equal(len(thisdeck), 52)
	# assert_equal(thisdeck.cards[0].attributes['suit'], 'clubs')
	# assert_equal(thisdeck.cards[0].attributes['rank'], '9')
	# assert_equal(thisdeck.cards[31].attributes['suit'], 'spades')
	# assert_equal(thisdeck.cards[31].attributes['rank'], 'A')
	# assert_equal(thisdeck.cards[51].attributes['suit'], 'clubs')
	# assert_equal(thisdeck.cards[51].attributes['rank'], '8')

	# # Test shuffle method
	# thisdeck.shuffle_cards()
	# assert_equal(len(thisdeck), 52)

