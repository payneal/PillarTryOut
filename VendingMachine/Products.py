# coins that vending machine can accept

#so that I can eventual connect this to use inserted money
from vendingMachine import machine


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
		

if __name__ == '__main__':
	test = products() 

	#attempt to by cola 
	itemName = test. getItemNameWithNumber(1)
	print itemName

	#get price 
	price = test.getItemPriceQty('price', itemName)
	print price
	#get qty
	qty= test.getItemPriceQty('qty', itemName)
	print qty

	# attemp to by chips
	itemName = test. getItemNameWithNumber(2)
	print itemName

	#get price 
	price = test.getItemPriceQty('price', itemName)
	print price
	#get qty
	qty= test.getItemPriceQty('qty', itemName)
	print qty

	# attemp to by candy 
	itemName = test. getItemNameWithNumber(3)
	print itemName

	#get price 
	price = test.getItemPriceQty('price', itemName)
	print price
	#get qty
	qty= test.getItemPriceQty('qty', itemName)
	print qty

	# attempt to by something not on the menu
	itemName = test. getItemNameWithNumber(4)
	print itemName

	


	