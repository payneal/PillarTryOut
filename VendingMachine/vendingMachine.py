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
		self.coinsInserted=[]
		self.amountInserted = 0.00
		self.items = {} 
		self.returnCoin = []
		self.returnCoinAmount = 0
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

	def getCoinsInserted(self): 
		return self.coinsInserted



	def getAllItems(self):
		return self.items 

	def getReturnCoins(self): 
		return self.returnCoin

	def getReturnCoinAmount(self):
		return self.returnCoinAmount		 

	def clearReturnedCoin(self): 
		self.returnCoin = []
		self.returnCoinAmount = 0 

	def insertCoin(self, thecoin):
		deposit = Coins.getAmount(thecoin)

		if deposit == None: 
			#they entered something other than a real coin
			self.returnCoin.append(thecoin)
		else:

			if thecoin in self.acceptedCoins:
				self.amountInserted = deposit + self.amountInserted
				self.coinsInserted.append(thecoin)

				#so that everything works (display)
				rounded2places = "{0:.2f}".format(self.amountInserted)

				self.amountInserted= float(rounded2places)
				self.display = "${}".format(rounded2places)
			else: 
				#tried to enter a coin that machine doesnt accept
				self.returnCoin.append(thecoin)
				self.returnCoinAmount = deposit + self.returnCoinAmount

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

			#find number of quartes
			quarters = 0
			for x in self.coinsInserted: 
				if x == 'quarter': 
					quarters = quarters + 1
			#print "there were this many quarters {}".format(quarters)

			#find number of dimes
			dimes = 0
			for x in self.coinsInserted: 
				if x == 'dime': 
					dimes = dimes + 1
			#print "there were this many dimes {}".format(dimes)

			#find number of nicks
			nickles = 0
			for x in self.coinsInserted: 
				if x == 'nickle': 
					nickles = nickles + 1
			#print "there were this many nickles {}".format(nickles)

			#for math to have something to subtract 
			takeAway = priceOfItem
			#print "this is the sub number {}".format(takeAway)

			for x in range(quarters + dimes + nickles):
				if takeAway >= .25 and quarters > 0: 
					takeAway = takeAway - .25
					quarters = quarters - 1
					#print "a quarter was subed so q= {} and total= {}".format(quarters, takeAway)
					self.coinsInserted.remove('quarter')
				elif takeAway >= .10 and dimes > 0:
					takeAway = takeAway - .10
					dimes = dimes - 1
					self.coinsInserted.remove('dime')
				elif takeAway >= .05 and nickles > 0:
					takeAway = takeAway - .05
					nickles = nickles - 1
					self.coinsInserted.remove('nickle')


			self.amountInserted = float('{}'.format("{0:.2f}".format(self.amountInserted)))

			self.setVendDisplay('THANK YOU')

			#change the quality
			Products.subQtyofItem(nameOfBuy)

			#put change in the coin return
			for x in self.coinsInserted:
				self.returnCoin.append(x)

			#clear coins Inserted because they are in return bin
			self.coinsInserted = []

			#state how much money in coin return
			self.returnCoinAmount = self.amountInserted

			#clear amount inserted 
			self.amountInserted = 0.00



	def checkQty(self, number): 
		nameOfBuy = Products.getItemNameWithNumber(number)
		return Products.getItemPriceQty('qty', nameOfBuy)

	def hitReturn(self): 
		return 'hi'
