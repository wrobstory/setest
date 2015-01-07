from nose.tools import *
from setest.deckofcards import Attribute, Card, Deck
from setest.decks.frenchplayingcards import suit_list, rank_list

def test_attribute():

	# Initialize a new attribute
	newatt = Attribute('name', 'joker')
	
	# Test
	assert_equal(newatt.name, 'name')
	assert_equal(newatt.value, 'joker')

def test_card():

	# Create two attributes to assign to the card
	strength_att = Attribute('strength', 6)
	health_att = Attribute('health', 4)

	# Create a new card and add the two attributes
	newcard = Card()
	newcard.add_attribute(strength_att)
	newcard.add_attribute(health_att)

	# Test Attributes
	assert_equal(newcard.attributes['strength'], 6)
	assert_equal(newcard.attributes['health'], 4)

	# Iterate over the card attributes
	allatt = []
	for att in newcard:
		allatt.append(att)

	# Test Iteration
	assert_equal(allatt[0], 6)
	assert_equal(allatt[1], 4)

def test_deck():

	# Create an empty deck
	thisdeck = Deck()

	# Cycle through suit and rank lists to generate cards for the deck
	for suit in suit_list:
		for rank in rank_list:
			
			# Assign the attributes
			thissuit = Attribute('suit', suit)
			thisrank = Attribute('rank', rank)

			# Create a new card
			thiscard = Card()
			thiscard.add_attribute(thissuit)
			thiscard.add_attribute(thisrank)

			# Add the card to the deck
			thisdeck.add_card(thiscard)

	# Test the new cards
	assert_equal(len(thisdeck), 52)
	assert_equal(thisdeck.cards[0].attributes['suit'], 'hearts')
	assert_equal(thisdeck.cards[0].attributes['rank'], 'A')
	assert_equal(thisdeck.cards[51].attributes['suit'], 'diamonds')
	assert_equal(thisdeck.cards[51].attributes['rank'], 'K')

	# Test deal methods
	mycard1 = thisdeck.deal_card()
	assert_equal(mycard1.attributes['suit'], 'hearts')
	assert_equal(mycard1.attributes['rank'], 'A')
	mycard2 = thisdeck.deal_card()
	assert_equal(mycard2.attributes['suit'], 'hearts')
	assert_equal(mycard2.attributes['rank'], '2')
	assert_equal(len(thisdeck), 50)

	# Add cards back to deck
	thisdeck.add_card(mycard1)
	thisdeck.add_card(mycard2)
	assert_equal(len(thisdeck), 52)

	# Test dealers cheating method
	mycheatcard = thisdeck.deal_card_cheat()
	assert_equal(mycheatcard, mycard2)
	thisdeck.add_card(mycheatcard)

	# Test cut method
	thisdeck.cut_deck(32)
	assert_equal(len(thisdeck), 52)
	assert_equal(thisdeck.cards[0].attributes['suit'], 'clubs')
	assert_equal(thisdeck.cards[0].attributes['rank'], '9')
	assert_equal(thisdeck.cards[31].attributes['suit'], 'spades')
	assert_equal(thisdeck.cards[31].attributes['rank'], 'A')
	assert_equal(thisdeck.cards[51].attributes['suit'], 'clubs')
	assert_equal(thisdeck.cards[51].attributes['rank'], '8')

	# Test shuffle method
	thisdeck.shuffle_cards()
	assert_equal(len(thisdeck), 52)

