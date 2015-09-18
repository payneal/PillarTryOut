class Game(object): 
	def __init__(self):
		self.stats = []

	def roll(self, pins): 
		self.stats.append(pins)

	def score(self): 
		return 0
