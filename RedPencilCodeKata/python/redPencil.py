from items import item

class Shop(object): 
	def __init__(self): 
		self.inStoreItem = [] 

	def addItem(self, name, price, date=None): 
		newItem = item(name,price, date)
		self.inStoreItem.append(newItem)

	def goThroughAllItemsInStore(self,whatToDoWithItem, name=None): 
		allItems = []
		for theItem in self.inStoreItem:
			if whatToDoWithItem == "getAllItems":
				hold = {theItem.name:{'price': theItem.price}}
				allItems.append(hold)
			else: 
				if theItem.name == name:
					if whatToDoWithItem == "getRedPencilStatus":
						return theItem.redPencilStatus
					elif whatToDoWithItem == "getPriceChangeDate":
						return theItem.dateOfLastPriceChange
					elif whatToDoWithItem == "getStablePriceDays":
						return theItem.getStablePriceDays()

					else: 
						newPrice = whatToDoWithItem
						self.executePriceChange(theItem,newPrice)
		return allItems

	def getAllItems(self): 
		return self.goThroughAllItemsInStore("getAllItems")  
	
	def changePrice(self, name, price):
		self.goThroughAllItemsInStore(price, name) 

	def executePriceChange(self,theItem,newPrice):
		previousPrice = theItem.price
		theItem.price = newPrice
		if newPrice <= (previousPrice - (previousPrice * .05)) and  newPrice >= (previousPrice - (previousPrice * .30)):
			theItem.changeRedPencilStatus()

		theItem.updateDate()

	def isOnRedPencileSale(self,name): 
		return self.goThroughAllItemsInStore("getRedPencilStatus", name) 

	def checkDaysPriceItemStable(self,name):
		return self.goThroughAllItemsInStore("getStablePriceDays", name) 

	def lastPriceChangeDate(self,name):
		return self.goThroughAllItemsInStore("getPriceChangeDate", name) 

		

