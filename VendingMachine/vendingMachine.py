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
		self.coinsInMachine = []
		self.amountInMachine = 0

	def getVendDisplay(self):
		if self.display == "THANK YOU":
			hold = self.display
			if self.amountInserted > 0.00: 
				self.display = "${0:.2f}".format(self.amountInserted)
			else:
				check = self.checkIfExactChangeOnly()
				if check == True: 
					self.display = "EXACT CHANGE ONLY"
				else: 
					self.display = "INSERT COINS"
			return hold
		elif "PRICE" in self.display: 
			hold = self.display
			check = self.checkIfExactChangeOnly()
			if check == True: 
				self.display = "EXACT CHANGE ONLY"
			else: 
				self.display = "INSERT COINS"
			return hold
		elif self.display == "SOLD OUT":
			hold = self.display
			check = self.checkIfExactChangeOnly()
			if check == True: 
				self.display = "EXACT CHANGE ONLY"
			else: 
				self.display = "INSERT COINS"
			return hold
		else: 
			if self.amountInserted == 0: 
				check = self.checkIfExactChangeOnly()
				if check == True: 
					self.display = "EXACT CHANGE ONLY"
				else: 
					self.display = "INSERT COINS"
			else: 
				self.display = "${0:.2f}".format(self.amountInserted)
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
		elif self.amountInserted== 0: 
			check = self.checkIfExactChangeOnly()
			if check == True: 
				self.display = "EXACT CHANGE ONLY"
			else: 
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

			if self.checkQty(number) == 0: 
				self.setVendDisplay('SOLD OUT')
			else: 
				#they buy item
				self.amountInserted = self.amountInserted - priceOfItem

				#Place this amount of money in the machine
				self.amountInMachine = self.amountInMachine + priceOfItem
				#print "this is the amount in the amchine: {}".format(self.amountInMachine)

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
				takeAway = int(priceOfItem * 100)
				#print "this is the sub number {}".format(takeAway)

				for x in range(quarters):
					if takeAway >= 25 and quarters > 0: 
						takeAway = takeAway - 25
						quarters = quarters - 1
						#print "a quarter was subed so q= {} and total= {}".format(quarters, takeAway)
						self.coinsInserted.remove('quarter')
						self.coinsInMachine.append('quarter') 
				
				for x in range(dimes):
					if takeAway >= 10 and dimes > 0:
						takeAway = takeAway - 10
						dimes = dimes - 1
						self.coinsInserted.remove('dime')
						self.coinsInMachine.append('dime') 
				
				for x in range(nickles):		
					#idk why i cant get takeAway >= .05 to work
					if takeAway >= 5 and nickles > 0: 
						takeAway = takeAway - 5
						nickles = nickles - 1
						self.coinsInserted.remove('nickle')
						self.coinsInMachine.append('nickle') 

				#print "coins in machin = {}".format(self.coinsInMachine)

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

	def returnButton(self): 
		#putt total inserted into return bin 
		self.returnCoin = self.coinsInserted
		self.coinsInserted = []

		#put coins inserted into return bin 
		self.returnCoinAmount = self.amountInserted 
		self.amountInserted = 0

		#reset the display
		self.setVendDisplay()

	def getAmountInMachine(self):
		return self.amountInMachine

	def getCoinsInMachine (self):
		return self.coinsInMachine 

	def checkIfExactChangeOnly(self): 
		#to be able to deliver all change I would need at least $.50 
		#but I would also need to be able to make $.35 cents 
		if self.amountInMachine < .50: 
			#need exact change 
			return True
		else: 
			#copy Coins in Machine to new variible
			n = self.getCoinsInMachine()

			#creat varibible that is .35
			makeChange = 35
			for x in self.coinsInMachine: 
				if 'quarter' in n  and  makeChange >= 25:  
					#n.remove('quarter')
					makeChange = makeChange -25 
				elif 'dime' in n and makeChange >= 10:
					#n.remove('dime')
					makeChange = makeChange - 10
				elif 'nickle' in n and makeChange >= 5: 
					#n.remove('nickle')
					makeChange = makeChange -5

			#see if we were able to creat 35 
			#print "this is make change {}".format(makeChange) 
			if makeChange == 0: 
				return False
			else:
				return True
			
		




		