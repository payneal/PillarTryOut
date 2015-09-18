class Game(object): 
	def __init__(self):
		self.frame = 10
		self.spearOrStrike = 10
		self.stats = []
		

	def roll(self, pins): 
		self.stats.append(pins)

	def score(self): 
		score = 0
		rollIndex = 0
		for x in range(self.frame):

			if self.stats[rollIndex] + self.stats[rollIndex+1] == self.spearOrStrike: 
				score += self.stats[rollIndex] + self.stats[rollIndex+1] + self.stats[rollIndex+2]
			else: 
				score += self.stats[rollIndex] + self.stats[rollIndex+1]
			rollIndex += 2
		return score
