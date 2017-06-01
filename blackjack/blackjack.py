suit = {0: 'Clubs', 1: 'Diamonds', 2: 'Hearts', 3: 'Spades'}
rank = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
		'9': 9, '10': 10, 'A': 1, 'J': 10, 'Q': 10, 'K': 10}

suit_list = ['clubs', 'spades', 'diamonds', 'hearts']
rank_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

from random import shuffle

class Card:
	def __init__(self, suit, rank):
		self.suit = suit
		self.rank = rank

class Deck:
	def __init__(self, no_decks=6):
		self.deck = self.create_deck(no_decks)
		self.shuffle_deck()

	def create_deck(self, no_decks):	
		self = []
		for k in range(0, (no_decks)):
			for i in range(0,4):
				for j in range(len(rank_list)):
					self.append(Card(i, rank_list[j]))
		return self

	def shuffle_deck(self):
		return shuffle(self.deck)

	def cut(self):
		half_length = int(len(self.deck)/2)
		first = self.deck[0:half_length]
		second = self.deck[half_length: -1]
		self.deck[0:half_length] = second
		self.deck[half_length:-1] = first

	def draw(self):
		a_card = self.deck.pop(0)
		return a_card


class Hand:
	def __init__(self, card = None):
		self.hand = []

	def hit_me(self, deck):
		self.hand.append(deck.draw())

	def handsome(self):
		to_sum = []
		contains_ace = False
		for card in self.hand:
			to_sum.append(rank[card.rank])
			if 'a' in card.rank:
				contains_ace = True
			elif 'A' in card.rank:
				contains_ace = True	
		value = sum(to_sum)
		if contains_ace == True:
			if value < 21 and (value + 10) <= 21:
				value += 10		
		else:
			value = sum(to_sum)

		return value	

	def discard(self):
		self = []

six_decks = Deck()

for card in six_decks.deck:
	print(card.suit, card.rank)

print(len(six_decks.deck))

for card in six_decks.deck:
	a_card = six_decks.draw()
	print(a_card.suit, a_card.rank)

print(six_decks)

decks = Deck()

decks.cut()

my_first_hand = Hand()

print('This is an initalized hand with nothing in it: {}'.format(str(my_first_hand)))

my_first_hand.hit_me(decks)	

print(my_first_hand.hand[0])

print(my_first_hand.handsome())
