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
			score = self.addScoreBasedOnIfStrikeOrSpare(score, rollIndex)
			rollIndex = self.addToRollIndex(rollIndex)

		return score
	
	def isSpare(self, rollIndex): 
		return self.stats[rollIndex] + self.stats[rollIndex+1] == self.spearOrStrike

	def isStrike(self, rollIndex): 
		return self.stats[rollIndex] == self.spearOrStrike

	def addToRollIndex(self, rollIndex): 
		if self.isStrike(rollIndex): 
			rollIndex += 1
		else: 
			rollIndex += 2
		return rollIndex

	def addToScoreThisManyRolls(self, amount, rollIndex): 
		addToScore = 0
		for x in range(amount): 
			addToScore += self.stats[rollIndex + x]
		return addToScore

	def addScoreBasedOnIfStrikeOrSpare(self, score, rollIndex): 
		if self.isStrike(rollIndex) or self.isSpare(rollIndex):  
			score += self.addToScoreThisManyRolls(3, rollIndex)
		else: 
			score += self.addToScoreThisManyRolls(2, rollIndex)
		return score



