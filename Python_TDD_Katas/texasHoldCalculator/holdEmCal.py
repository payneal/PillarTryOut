
class tableHand(object): 
	def __init__(self):
		self.cardOne = None
		self.cardTwo = None

	def myCards(self, cards):
		self.cardOne = cards['cardOne']
		self.cardTwo = cards['cardTwo'] 

	def chancesOfPair(self): 
		if self.cardOne["rank"] == self.cardTwo["rank"]: 
			return 100
		else:
			return 49


