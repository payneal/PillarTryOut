from items import item

class Shop(object): 
	def __init__(self): 
		self.inStoreItem = [] 

	def addItem(self, name, price, date=None): 
		newItem = item(name,price, date)
		self.inStoreItem.append(newItem)

	def goThroughAllItemsInStoreGetAllOrJustOne(self, name=None): 
		allItems = []
		for theItem in self.inStoreItem:
			if name == None:
				hold = {theItem.name:{'price': theItem.price}}
				allItems.append(hold)
			else:  
				if theItem.name == name:
					return theItem				
		return allItems

	def getAllItems(self): 
		return self.goThroughAllItemsInStoreGetAllOrJustOne()  
	
	def changePrice(self, name, newPrice, date= None):
		theItem = self.goThroughAllItemsInStoreGetAllOrJustOne(name)
		self.executePriceChange(theItem,newPrice, date)

	def executePriceChange(self,theItem,newPrice, date= None):
		previousPrice = theItem.price
		theItem.price = newPrice
		if newPrice <= (previousPrice - (previousPrice * .05)) and  newPrice >= (previousPrice - (previousPrice * .30)):
			if theItem.hadStablePriceFor30Days():
				theItem.changeRedPencilStatus()
		if date == None:
			theItem.updateDateToToday()
		else: 
			theItem.dateOfLastPriceChange = date


	def isOnRedPencileSale(self,name): 
		theItem = self.goThroughAllItemsInStoreGetAllOrJustOne(name) 
		return theItem.redPencilStatus

	def checkDaysPriceItemStable(self,name):
		theItem =  self.goThroughAllItemsInStoreGetAllOrJustOne(name) 
		return theItem.getStablePriceDays()

	def lastPriceChangeDate(self,name):
		theItem = self.goThroughAllItemsInStoreGetAllOrJustOne(name) 
		return theItem.dateOfLastPriceChange
		

