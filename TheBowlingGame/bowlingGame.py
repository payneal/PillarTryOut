class Game(object): 
	def __init__(self):
		self.frame = 10
		self.spearOrStrike = 10
		self.stats =[]

		self.frameOn = 1
		self.whichRollInFrame= 1
		self.frameStats= None
		self.scoreBoard = {'1': None, '2': None, '3': None , '4':None ,'5':None , '6':None , '7':None , '8':None , '9':None , '10':None }
		
	def roll(self, pins):
		#add to stats
		self.stats.append(pins)
	
		if self.whichRollInFrame == 1: 
			#set up frame stats structure for fram 10 
			if self.frameOn == 10: 
				self.frameStats= {'1': None, '2': None, '3': None }
			else: 
				self.frameStats= {'1': None, '2': None }

			#fill in the frame stats fpr roll #1
			self.frameStats[str(self.whichRollInFrame)]= pins
			
			#CHECK  to see if strike 
			if self.frameStats['1'] == 10: 
				
				#check see if not frame 10
				if self.frameOn != 10:
					#this is a strike so fill in score board
					self.scoreBoard[str(self.frameOn)] = self.frameStats

					# move to the next frame
					self.frameOn += 1
				else: 
					#in the 10th so just move to the next roll
					self.whichRollInFrame += 1
			else: 
				#they didnt roll a strike
				#to the next roll 
				self.whichRollInFrame += 1
		else:
			#fill in the frame stats for roll(2nd or 3rd if on 10th)
			self.frameStats[str(self.whichRollInFrame)]= pins  

			if self.whichRollInFrame == 2: 
				#SEE IF we are in the 10th
				if self.frameOn == 10: 
					#check to see if they rolled spare or strike in 1oth
				  	if self.frameStats['1'] == 10 or self.frameStats['1'] + self.frameStats['2'] == 10:
						#move to the next roll in frame(they get the 3rd bonus roll)
						self.whichRollInFrame +=1
				else: 
					#tfill in score board no additional roll permitted
					self.scoreBoard[str(self.frameOn)] = self.frameStats
					#move to the next frame
					self.frameOn += 1
					#set roll 
					self.whichRollInFrame = 1

			elif self.whichRollInFrame == 3:
			 		#tfill in score board no additional roll permitted
					self.scoreBoard[str(self.frameOn)] = self.frameStats
					#make sure roll is set to 4 and there is no comming back
					self.whichRollInFrame +=1
			else:
				return "no more than three balls can be rolled in tenth frame"

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

