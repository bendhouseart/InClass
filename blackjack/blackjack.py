suit = {0: 'Clubs', 1: 'Diamonds', 2: 'Hearts', 3: 'Spades'}
rank = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
		'9': 9, '10': 10, 'A': 1, 'J': 10, 'Q': 10, 'K': 10}

suit_list = ['clubs', 'spades', 'diamonds', 'hearts']
rank_list = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']

from random import shuffle
import os

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

	def show_hand(self):
		for card in self.hand:
			return str(card.rank) + ' of ' +str(suit[card.suit])


def print_stars():
	rows, columns = os.popen('stty size', 'r').read().split()
	print('*'*int(columns))

def game_menu(players, num_players, deck):
	print_stars()
	print_stars()
	print('''Welcome to Console Poker: The Reckoning
Currently on the Table:''')
	print('Dealer is showing: ', players[0].show_hand())
	for i in range(1, num_players):
		print('Player ' + str(i) + ' is holding {}'.format(players[i].show_hand()))
	print_stars()
	print_stars()

	advance = ''

	while 'c' not in advance:
		advance = input('''If a player wishes to hit enter that player's integer number, else enter C to continue: '''.lower())
		try:
			if 1 <= int(advance) <= num_players:
				players[int(advance)].hit_me(deck)
		except:
			print('Please enter a valid player input.')
			continue	

''' Here we are starting the game by asking the user how many decks
  	they will be using to play black jack. '''

while True:
	try:
		num_decks = int(input('Enter the number of decks to be played in this game: '))
		break
	except ValueError:
		os.system('clear')
		print('Please enter an integer')
		continue


deck = Deck(num_decks)


''' Here we will get the number of players playing the game, not including    the dealer'''

while True:
	try:
		num_players = int(input('Enter the number of players who wish to play: '))
		os.system('clear')
		break
	except ValueError:
		os.system('clear')
		print('Please enter an integer.')
		continue

''' Here we will put our players and dealer into existence and deal them a card each. For the sake of consistency 
	the dealer will always be refered to as player 0 in our code '''

players = []

for i in range(0,(num_players + 1)):
	new_player = Hand()
	players.append(new_player)
	players[i].hit_me(deck)
		

''' And now the game begins!'''

game_state = True
while game_state == True:
	game_menu(players, num_players, deck)
#	os.system('clear')
#	print_stars()
#	print_stars()
#	print('''Welcome to Console Poker: The Reckoning
#Currently on the Table:''')
#	print('Dealer is showing: ', players[0].show_hand())
#	for i in range(1, num_players):
#		print('Player ' + str(i) + ' is holding {}'.format(players[i].show_hand()))
#	print_stars()
#	print_stars()
#
#	advance = ''
#
#	while 'c' not in advance:
#		advance = input('''If a player wishes to hit enter that player's integer number, else enter C to continue: '''.lower())
#		try:
#			if 1 <= int(advance) <= num_players:
#			players[int(advance)].hit_me(deck)
#			except:
#				print('Please enter a valid player input.')
#				continue				
				
	game_state = False	


