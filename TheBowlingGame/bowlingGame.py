class Game(object): 
	def __init__(self):
		self.stats = []

	def roll(self, pins): 
		self.stats.append(pins)

	def score(self): 
		score = 0
		for x in self.stats: 
			score = score + x

		return score
