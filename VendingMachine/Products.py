# coins that vending machine can accept

class products(object):  
	def __init__(self):
		self.numberOfitems = 3
		#hold all items in one
		self.items= {'cola': {'price':1.00, 'qty': 10} , 'chips': {'price': .50, 'qty': 10},  'candy': {'price':.65, 'qty': 10} }

	def getItemNameWithNumber(self, choice): 
		if choice == 1: 
			return "cola"
		elif choice == 2:
			return "chips"
		elif choice == 3: 
			return "candy"
		else: 
			return None

	def getItemPriceQty(self, priceQty, name):
		return self.items[name][priceQty]

	def getAllProducts(self):
		return self.items
		