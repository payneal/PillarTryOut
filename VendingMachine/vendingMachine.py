# this is the brains of my vending machine

#so that I can accept or reject coins
from Coin import coins

#using coins
Coins = coins()

from Products import products

#using products
Products = products()



class machine(object): 
	def __init__(self): 
		self.display = "INSERT COINS"
		self.amountInserted = 0
		self.items = {} 
		self.returnCoin = None
		self.acceptedCoins = {"nickle":.05, 'dime': .10, 'quarter': .25} 

	def getVendDisplay(self):
		if self.display == "THANK YOU":
			hold = self.display
			if self.amountInserted > 0.00: 
				self.display = "${0:.2f}".format(self.amountInserted)
			else: 
				self.display = "INSERT COINS"
			return hold
		elif "PRICE" in self.display: 
			hold = self.display
			self.display = "INSERT COINS"
			return hold
		#elif self.amountInserted > 0.00:
		#	self.display = "{$0:.2f}".format(self.amountInserted)
		#	return self.display

		else: 
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
				self.display = "${}".format(rounded2places)
			else: 
				#tried to enter a coin that machine doesnt accept
				self.returnCoin = thecoin

	def addAllItems(self):
		self.items = Products.getAllProducts()

	def showItems(self):
		string = ''
		count= 1
		for x in self.items: 
			name = Products.getItemNameWithNumber(count)
			price = Products.getItemPriceQty('price', name)
			string = string + "{}.) {} = ${}".format(count, name , "{0:.2f}".format(price))
			count+= 1
			if count != len(self.items) +1 : 
				string = string + ", "
		return string

	def setVendDisplay(self, what= None):
		if what:
			self.display = what
		elif self.totalInserted == 0: 
			self.display = "INSERT COINS"
		else: 
			#we nee dto convert this number to a string 
			self.display = "{0:.2f}".format(self.amountInserted)


	def buyItem(self, number):
		nameOfBuy = Products.getItemNameWithNumber(number)

		priceOfItem =  Products.getItemPriceQty('price', nameOfBuy)

		if priceOfItem > self.amountInserted: 
			price = Products.getItemPriceQty('price', nameOfBuy)
			string = 'PRICE = ${}'.format("{0:.2f}".format(price))
			self.display = string
		else: 
			#they buy item
			self.amountInserted = self.amountInserted - priceOfItem
			
			self.amountInserted = float('{}'.format("{0:.2f}".format(self.amountInserted)))

			self.setVendDisplay('THANK YOU')

			#change the quality
			Products.subQtyofItem(nameOfBuy)

	def checkQty(self, number): 
		nameOfBuy = Products.getItemNameWithNumber(number)
		return Products.getItemPriceQty('qty', nameOfBuy)








	


		



	
			






