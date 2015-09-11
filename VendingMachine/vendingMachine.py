# this is the brains of my vending machine

#so that I can accept or reject coins
from Coin import coins



class machine(object): 
	def __init__(self): 
		self.display = "INSERT COIN"
		self.amountInserted = 0
		self.totalInserted = 0 
		self.items = {} 
		self.returnCoin = None

	def getReturnCoin(self): 
		return self.returnCoin

	def clearReturnedCoin(self): 
		self.returnCoin = None

	def setVendDisplay(self, thanks= None):
		if thanks == True:
			self.display = 'THANKS'
		elif self.totalInserted == 0: 
			self.display = "INSERT COIN"
		else: 
			#we nee dto convert this number to a string 
			self.display = "{0:.2f}".format(self.totalInserted)

	def getVendDisplay(self):
		return self.display

	def getTotalInserted(self): 
		return self.totalInserted

	def insertCoin(self, thecoin):
		deposit = coins(thecoin) 

		if deposit.check() == False: 
			self.returnCoin = thecoin
		else:
			self.totalInserted += thecoin

			#so that everything works
			rounded2places = "{0:.2f}".format(self.totalInserted)

			self.totalInserted= float(rounded2places)

	def addAllItems(self, items):
		self.items = items

	def getAllItems(self):
		return self.items 
			





if __name__ == '__main__':
	test = machine() 

	

	test.addAllItems({'chips': {'price': 0.5, 'qty': 10}})

	this = test.getAllItems()

	print this



