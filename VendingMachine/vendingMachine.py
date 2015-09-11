# this is the brains of my vending machine

#so that I can accept or reject coins
from Coin import coins

#using coins
Coins = coins()


class machine(object): 
	def __init__(self): 
		self.display = "INSERT COIN"
		self.amountInserted = 0
		self.items = {} 
		self.returnCoin = None
		self.acceptedCoins = {"nickle":.05, 'dime': .10, 'quarter': .25} 

	def getVendDisplay(self):
		return self.display

	def getTotalInserted(self): 
		return self.amountInserted

	def getAllItems(self):
		return self.items 

	def getReturnCoin(self): 
		return self.returnCoin

	def clearReturnedCoin(self): 
		self.returnCoin = None


	def insertCoin(self, thecoin):
		deposit = Coins.getAmount(thecoin)

		if deposit == None: 
			#they entered something other than a real coin
			self.returnCoin = thecoin
		else:


			if thecoin in self.acceptedCoins:
				self.amountInserted = deposit + self.amountInserted

				#so that everything works (display)
				rounded2places = "{0:.2f}".format(self.amountInserted)

				self.amountInserted= float(rounded2places)
				self.display = rounded2places
			else: 
				#tried to enter a coin that machine doesnt accept
				self.returnCoin = thecoin


	def setVendDisplay(self, thanks= None):
		if thanks == True:
			self.display = 'THANKS'
		elif self.totalInserted == 0: 
			self.display = "INSERT COIN"
		else: 
			#we nee dto convert this number to a string 
			self.display = "{0:.2f}".format(self.totalInserted)

	def addAllItems(self, items):
		self.items = items

	
			






