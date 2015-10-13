
class item(object):
	def __init__(self, name, price):
		 self.name = name
		 self.price = price 
		 


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
		for x in self.inStoreItem:
			if x.name == name:
				x.price = price

	def isOnRedPencileSale(self,name): 
		return False

