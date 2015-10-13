
class Shop(object): 
	def __init__(self): 
		self.items = [] 

	def addItem(self, item): 
		self.items.append(item)

	def getAllItems(self): 
		return self.items
