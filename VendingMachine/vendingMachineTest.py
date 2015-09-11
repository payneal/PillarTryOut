# System test
import unittest

#so that I can test the money
from vendingMachine import machine

#so that I can make buys
from Products import products

#used for random testing 
from random import randint

# create the test
test = machine()
# create the test  that can test buying
test2 = machine()

#this creates required prducts via pillar kata
items =  products()

class TestMachine(unittest.TestCase):
	def setUp(self): 
		pass

	def test_initial_display(self):	
		display = test.getVendDisplay() 
		self.assertEqual(display, "INSERT COINS")

	def test_initial_amount(self): 
		display = test.getTotalInserted()
		self.assertEqual(display, 0)

	def test_items_in_Vmachine(self): 
		inMachine = test.getAllItems()
		self.assertEqual(inMachine, {})

	def test_look_in_return_Bin(self): 
		binCoin = test.getReturnCoin()
		self.assertEqual(binCoin, None)

	def test_insert_coins(self):
		test.insertCoin('dime')
		checkReturn=  test.getReturnCoin()
		self.assertEqual(checkReturn, None)
		amountInserted = test.getTotalInserted()
		self.assertEqual(amountInserted, .10)

		#test inserting multiple coins
		test.insertCoin('nickle')
		checkReturn=  test.getReturnCoin()
		self.assertEqual(checkReturn, None)
		amountInserted = test.getTotalInserted()
		self.assertEqual(amountInserted, .15)

	def test_updated_display(self):	
		display = test.getVendDisplay() 
		self.assertEqual(display, "$0.15")

	def test_instert_bad_coin(self): 
		test.insertCoin('fake')
		checkReturn=  test.getReturnCoin()
		self.assertEqual(checkReturn, 'fake')

		#make sure you clear return bin
		test.clearReturnedCoin()
		
		amountInserted = test.getTotalInserted()
		self.assertEqual(amountInserted, .15)	

	def test_insert_invalid_Coin(self): 
		test.insertCoin('half')
		checkReturn=  test.getReturnCoin()
		self.assertEqual(checkReturn, 'half')

		#make sure you clear return bin
		test.clearReturnedCoin()
		
		amountInserted = test.getTotalInserted()
		self.assertEqual(amountInserted, .15)	

	def test_adding_item_to_vending_vendingMachine(self): 			
		#this puts all products in a varible
		allProducts = items.getAllProducts()
		#this puts all products in the machine
		test2.addAllItems()
		#hold all items form vending machine
		theItemsInMachine = test2.getAllItems()
		
		# we want to test this to see if all Products are stored now in vending machine
		self.assertEqual(theItemsInMachine,allProducts)

	def test_showing_items_in_Vmachine(self): 
		#this diplays all items in machin is this form
		buyables = "1.) cola = $1.00, 2.) chips = $0.50, 3.) candy = $0.65"
		result = test2.showItems()
		self.assertEqual(result,buyables)

	def test_buy_button_Bad_functionality(self): 
		#give machine money $.50 so can only buy one item
		test2.insertCoin('quarter')
		test2.insertCoin('quarter')
		amountInserted = test2.getTotalInserted()
		self.assertEqual(amountInserted, .50)

		#this is if buying cola thats too expensive
		test2.buyItem(1)
		result= test2.getVendDisplay()
		self.assertEqual(result, 'PRICE = $1.00')

		result= test2.getVendDisplay()
		self.assertEqual(result, 'INSERT COINS')


	def test_buy_button_good_functionality(self):
		amountInserted = test2.getTotalInserted()
		self.assertEqual(amountInserted, .50)
		 
		#this is if buying chips that you can afford
		result = test2.buyItem(2)

		#check amont in machine
		result= test2.getTotalInserted()
		self.assertEqual(result, 0)
		
		#check that item has been given
		result= test2.checkQty(2)
		self.assertEqual(result, 9)

		#check display message
		result= test2.getVendDisplay()
		self.assertEqual(result, 'THANK YOU')

		#second check of display
		result= test2.getVendDisplay()
		self.assertEqual(result, 'INSERT COINS')

	def test_buy_button_good_functionality_with_change_left(self): 
		#make sure that 0 is the amount in machine
		result= test2.getTotalInserted()
		self.assertEqual(result, 0.0)

		#insert $.60
		test2.insertCoin('quarter')
		test2.insertCoin('quarter')
		test2.insertCoin('dime')
		
		amountInserted = test2.getTotalInserted()
		self.assertEqual(amountInserted, .60)
		 
		#this is if buying chips that you can afford
		result = test2.buyItem(2)

		#check amont in machine
		result= test2.getTotalInserted()
		self.assertEqual(result, .10)
		
		#check that item has been given
		result= test2.checkQty(2)
		self.assertEqual(result, 8)

		#check display message
		result= test2.getVendDisplay()
		self.assertEqual(result, 'THANK YOU')

		#second check of display
		result= test2.getVendDisplay()
		self.assertEqual(result, "$0.10")





	

if __name__ == '__main__':
    unittest.main()