from random import randint, shuffle

game_on = True

class Player(object):
	def __init__(self, name):
		self.name = name
		self.cards = []
		self.score = 0

	def compute_score(self):
		score = 0
		for card in self.cards:
			if card[0]==11 or card[0]==12 or card[0]==13:
				score+=10
			else:
				score+=card[0]
		return score

	def __str__(self):
		return "{0}, {1}, {2}".format(self.name, self.cards, self.score)


	
class Deck(object):
	
	def __init__(self):
		self.deck = []
		for num in range(1, 14):
			hearts = (num, 'hearts')
			spades = (num, 'spades')
			diamonds = (num, 'diamonds')
			clubs = (num, 'clubs')
			self.deck += [hearts, spades, diamonds, clubs]
		shuffle(self.deck)

	def random_card(self):
		card = self.deck[randint(1, len(self.deck))]
		self.deck.remove(card)
#		print len(self.deck)
		return card
		
	# breaks down tuple to get card name as string
	# makes displaying tuple to user "easier"
	def card_name(self, card):
		number = card[0]
		type = card[1]
		return str(number) + " of " + type
	
	def print_deck(self):
		for card in self.deck:
			print(self.card_name(card))



# ------------------------------------------------------------ #



# ---> syntax error: with the word new
deck = Deck()

p1 = Player('p1')
p1.cards += [deck.random_card()]
p1.cards += [deck.random_card()]
p1.score = p1.compute_score()
# print p1.cards
# print p1.score

p2 = Player('p2')
p2.cards += [deck.random_card()]
p2.cards += [deck.random_card()]
p2.score = p2.compute_score()
# print p2.cards
# print p2.score
	
player = p1	
while game_on:

	def is_playing(player):
		if player == p1:
			player = p2
		else:
			player = p1
		return player
	
	print player.name
 	print player.cards
 	print player.score
	
	while player == p1:
		print player.name
		choice = raw_input('Hit, stay: ')
		if choice == 'hit':		
			player.cards += [deck.random_card()]	
			player.score = player.compute_score()
			print player.cards
			print player.score
		
			if player.score > 21:
				print player.score , ' means that you lose'
				player = is_playing(player)
				print 'it is your turn' , player.name
			
			elif player.score == 21:
				print player.name, 'got blackjack, so you win!'
				game_on = False
				break
			
		else:
			player = is_playing(player)
			break

	while player.name == 'p2':
		choice = raw_input('Hit, stay: ')
		print player.name
		if choice == 'hit':
			player.cards += [deck.random_card()]	
			player.score = player.compute_score()
			print player.cards
			print player.score
		
			if player.score > 21:
				print player.score , ' means that you lose'
				player = is_playing(player)
				print 'it is your turn' , player.name
			
			elif player.score == 21:
				print player.name, 'got blackjack, so you win!'
				game_on = False
				break
			
		else:
			player = is_playing(player)

#def play():
#play()