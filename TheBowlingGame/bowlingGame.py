class Game(object): 
	def __init__(self):
		self.frameMax = 10
		self.spearOrStrike = 10
		self.stats =[]

		self.frameOn = 1
		self.whichRollInFrame= 1
		self.frameStats= None
		self.scoreBoard = {'1': None, '2': None, '3': None , '4':None ,'5':None , '6':None , '7':None , '8':None , '9':None , '10':None }
		
	def roll(self, pins):
		if self.whichRollInFrame == 1: 
			self.handleFirstRollOfFrame(pins)
		else:
			return self.handleAnyRollAfterFirstRollOfFrame(pins) 
	
	def handleFirstRollOfFrame(self, pinsHit): 
		self.setUpFrameStatsStructure()
		self.fillInFrameStatsWithPinsHit(pinsHit) 
		self.decideWhatToDo4FirstRoll()

	def handleAnyRollAfterFirstRollOfFrame(self, pinsHit): 
		if self.whichRollInFrame <= 3: 
			self.fillInFrameStatsWithPinsHit(pinsHit)
			if self.whichRollInFrame == 2: 
				self.decideWhatToDo4SecondRoll() 
			elif self.whichRollInFrame == 3:
				self.fillInScoreBoard(True)
		else: 
			return "no more than three balls can be rolled in tenth frame"

	def setUpFrameStatsStructure(self): 
		if self.frameOn == self.frameMax: 
			self.frameStats= {'1': None, '2': None, '3': None }
		else: 
			self.frameStats= {'1': None, '2': None }

	def fillInFrameStatsWithPinsHit(self, pins): 
		#fill in the frame stats fpr roll #1
		self.frameStats[str(self.whichRollInFrame)]= pins
		#add to stats
		self.stats.append(pins)

	def decideWhatToDo4FirstRoll(self): 
		if self.isStrike(self.frameStats['1']): 
			if self.frameOn != self.frameMax:
				self.fillInScoreBoard()
			else: 
				self.moveToNextRollOrReset()
		else: 
			self.moveToNextRollOrReset()

	def decideWhatToDo4SecondRoll(self): 	
		if self.frameOn == self.frameMax: 
		  	if self.isStrike(self.frameStats['1']) or self.isSpare(self.frameStats['1'],self.frameStats['2']):
				self.moveToNextRollOrReset()
		else: 
			self.fillInScoreBoard()
			self.moveToNextRollOrReset(1)

	def fillInScoreBoard(self, tenthFrame = None): 
		self.scoreBoard[str(self.frameOn)] = self.frameStats
		if tenthFrame: 
			self.moveToNextRollOrReset()
		else: 
			self.moveToNextFrame()

	def moveToNextFrame(self):
		self.frameOn += 1

	def moveToNextRollOrReset(self, number= None):
		if number: 
			self.whichRollInFrame = 1
		else:	
			self.whichRollInFrame += 1

	def score(self): 
		score = 0
		rollIndex = 0
		for x in range(self.frameMax):
			score = self.addScoreBasedOnIfStrikeOrSpare(score, rollIndex)
			rollIndex = self.addToRollIndex(rollIndex)
		return score
	
	def isSpare(self, pinHitOnRollOne, pinHitOnRollTwo): 
		return pinHitOnRollOne + pinHitOnRollTwo == self.spearOrStrike

	def isStrike(self, pinsHit): 
		return pinsHit == self.spearOrStrike

	def addToRollIndex(self, rollIndex): 
		if self.isStrike(self.stats[rollIndex]): 
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
		if self.isStrike(self.stats[rollIndex]) or self.isSpare(self.stats[rollIndex], self.stats[rollIndex+1]):  
			score += self.addToScoreThisManyRolls(3, rollIndex)
		else: 
			score += self.addToScoreThisManyRolls(2, rollIndex)
		return score

