# System test
import unittest

#so that I can test the money
from Products import products

#used for random testing 
from random import randint

class TestMoneyUnits(unittest.TestCase):
	def setUp(self): 
		pass

	def test_assoiate_number_with_product(self):	
		test1 = products() 
		#attempt to get cola using number 1  
		itemName = test1.getItemNameWithNumber(1)
		self.assertEqual(itemName, "cola")

		#attempt to get chips using number 2 
		itemName = test1.getItemNameWithNumber(2)
		self.assertEqual(itemName, "chips")

		#attempt to get candy using number 3
		itemName = test1.getItemNameWithNumber(3)
		self.assertEqual(itemName, "candy")

		# attempt to by something not on the menu
		itemName = test1.getItemNameWithNumber(4)
		self.assertEqual(itemName, None)

	def test_price_qty_of_product(self):
		test2 = products() 
		#test the price & qty for cola 
		itemName = test2.getItemNameWithNumber(1)
		#get price 
		price = test2.getItemPriceQty('price', itemName)
		self.assertEqual(price, 1.00)
		#get qty
		qty= test2.getItemPriceQty('qty', itemName)
		self.assertEqual(qty, 10)

		#test the price & qty for chips
		itemName = test2.getItemNameWithNumber(2)
		#get price 
		price = test2.getItemPriceQty('price', itemName)
		self.assertEqual(price, .50)
		#get qty
		qty= test2.getItemPriceQty('qty', itemName)
		self.assertEqual(qty, 10)

		#test the price & qty  for candy 
		itemName = test2.getItemNameWithNumber(3)
		#get price 
		price = test2.getItemPriceQty('price', itemName)
		self.assertEqual(price, .65)
		#get qty
		qty= test2.getItemPriceQty('qty', itemName)
		self.assertEqual(qty, 10)

	def test_get_all_items(self): 
		test3 = products()

		allItems = test3.getAllProducts()
		self.assertEqual(allItems, {'cola': {'price':1.00, 'qty': 10} , 'chips': {'price': .50, 'qty': 10},  'candy': {'price':.65, 'qty': 10} })

	def test_sub_qty(self): 
		test4 = products()

		qty= test4.getItemPriceQty('qty', 'cola')
		self.assertEqual(qty, 10)

		test4.subQtyofItem('cola')
		qty= test4.getItemPriceQty('qty', 'cola')
		self.assertEqual(qty, 9)






	#create random test later I just wanna hurry up and finsih this thing 


if __name__ == '__main__':
    unittest.main()