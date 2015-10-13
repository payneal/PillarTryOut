
class item(object):
	def __init__(self, name, price):
		self.name = name
		self.price = price 
		self.redPencileStatus = False

	def changeRedPencileStatus(self):
		self.redPencileStatus = True
		 
class Shop(object): 
	def __init__(self): 
		self.inStoreItem = [] 

	def addItem(self, name, price): 
		newItem = item(name,price)
		self.inStoreItem.append(newItem)

	def getAllItems(self): 
		allItems = []
		for x in self.inStoreItem:
			hold = {x.name:{'price': x.price}}
			allItems.append(hold)
		return allItems

	def changePrice(self, name, price):
		previousPrice= None

		for x in self.inStoreItem:
			if x.name == name:
				previousPrice = x.price
				x.price = price

				if price <= (previousPrice - (previousPrice * .05)):
					x.changeRedPencileStatus()
					
	
	def isOnRedPencileSale(self,name): 
		for x in self.inStoreItem:
			if x.name == name:
				return x.redPencileStatus 
		return False

