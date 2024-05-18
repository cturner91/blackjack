# import random

# SUITS = ('C', 'D', 'H', 'S')
# VALUES = ('A','2','3','4','5','6','7','8','9','10','J','Q','K')


# def random_of(iterable):
# 	return iterable[int(random.random() * len(iterable))]


# class Card:
	
# 	def __init__(self, suit=None, value=None):
# 		if suit is None:
# 			suit = random_of(SUITS)
# 		if value is None:
# 			value = random_of(VALUES)
		
# 		assert suit in SUITS
# 		assert value in VALUES
			
# 		self.suit = suit
# 		self.value = value
	
# 	def __str__(self):
# 		return f'{self.value}{self.suit}'
		
# 	def __repr__(self):
# 		return str(self)
	
# 	@classmethod
# 	def from_str(cls, string):
# 		suit = string[-1:]
# 		value = string[:-1]
# 		return cls(suit, value)


# class Deck:
	
# 	def __init__(self):
# 		self.cards = [Card(suit, value) for suit in SUITS for value in VALUES]
	
# 	def shuffle(self):
# 		rands = sorted([(i, random.random()) for i in range(len(self.cards))], key=lambda x: x[1])
# 		self.cards = [self.cards[x[0]] for x in rands]
	
# 	def draw(self, i=None):
# 		if len(self.cards) < 1:
# 			raise ValueError('No cards left!')
		
# 		if i is None:
# 			i = int(random.random() * len(self.cards))
		
# 		card = self.cards[i]
# 		self.cards.pop(i)
# 		return card


# class Player:
	
# 	def __init__(self):
# 		self.cards = []
	
# 	def draw(self, deck, i=None):
# 		card =  deck.draw(i)
# 		self.cards.append(card)
	
# 	def score(self):
# 		total = 0
# 		for card in self.cards:
# 			value = {
# 				'J': 10,
# 				'Q': 10,
# 				'K': 10,
# 				'A': 11,
# 			}.get(card.value, None)
# 			if value is None:
# 				 value = int(card.value)
# 			total += value
		
# 		if total > 21:
# 			# take off 10 for every ace present (11 -> 1 = drop of 10)
# 			n_aces = sum([card.value == 'A' for card in self.cards])
# 			for n in range(1, n_aces + 1):
# 				score = total - n * 10
# 				if score <= 21:
# 					return score
# 			else:
# 				return None  # bust
				
# 		return total
	
# 	def get_action_1(self, cap=17):
# 		score = self.score()
# 		if score is None:
# 			return 'h'
# 		if score < cap:
# 			return 'd'
# 		return 'h'


# def calculate_winner(player1, player2):
# 	score1 = player1.score()
# 	score2 = player2.score()
	
# 	if score1 is None and score2 is None:
# 		return None
# 	elif score1 is None:
# 		return 2
# 	elif score2 is None:
# 		return 1
# 	elif score1 == score2:
# 		if len(player1.cards) > len(player2.cards):
# 			return 1
# 		elif len(player2.cards) > len(player1.cards):
# 			return 2
# 		else:
# 			return None
# 	else:
# 		return 1 if score1 > score2 else 2
	
	
# def run_game(cap=17):
# 	deck = Deck()
# 	deck.shuffle()

# 	dealer = Player()
# 	me = Player()
	
# 	dealer.draw(deck)
# 	me.draw(deck)
# 	dealer.draw(deck)
# 	me.draw(deck)
	
# 	action = me.get_action_1(cap)
# 	while action != 'h':
# 		me.draw(deck)
# 		action = me.get_action_1(cap)
	
# 	if me.score() is None:
# 		return 2
	
# 	while dealer.score() is not None and dealer.score() < me.score():
# 		dealer.draw(deck)
	
# 	winner = calculate_winner(me, dealer)
# 	if winner is None:
# 		print('---')
# 		print(dealer.cards)
# 		print(me.cards)
# 		print('---')
# 	return winner
	
	

# if __name__ == '__main__':
# 	results_master = []
# 	for cap in range(10, 21):
# 		N = 100
# 		results = {}
# 		for i in range(N):
# 			winner = run_game(cap)
# 			results[winner] = results.get(winner, 0) + 1
		
# 		for key in results:
# 			results[key] = results[key] / N * 100
		
# 		results_master.append((cap, results[1]))

# 	for x in results_master:
# 		print(x)
		
