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
		self.assertEqual(display, "INSERT COIN")

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
		self.assertEqual(display, "0.15")

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

	def test_buy_button_functionality(self): 
		#give machine money $.50 so can only buy one item
		test2.insertCoin('quarter')
		test2.insertCoin('quarter')
		amountInserted = test2.getTotalInserted()
		self.assertEqual(amountInserted, .50)

		#sh

		#go buy item that is $.65 should get display "PRICE: {$}"
		#test2.




	#create random test once done (below is old one)
	if False: 	
		def test_random_adding_coin(self):
			
			print "step 1"
			randomCoins =  [ 0.01, 0.05, 0.10, 0.20, 0.50]
			validCoins = [.05, .10, .25]

			print "step 2"
			for i in range(100): 
				
				testRandom = machine()
				number = randomCoins[randint(0,4)]

				testRandom.insertCoin(number)

				if number in validCoins: 
					checkReturn =  testRandom.getReturnCoin()
					self.assertEqual(checkReturn, None)
					
					#check to see that correct amount has been inserted
					amountInserted = testRandom.getTotalInserted()
					self.assertEqual(amountInserted, number)
					
					#this should None because this is a vaild coin to enter
					checkReturn=  testRandom.getReturnCoin()
					self.assertEqual(checkReturn, None)

					#this check the display
					testRandom.setVendDisplay()
					display = testRandom.getVendDisplay()
					self.assertEqual(float(display), number)

					#add  coin two
					secondNumber = randomCoins[randint(0,4)]
					testRandom.insertCoin(secondNumber)
					if secondNumber in validCoins: 
						#check the display
						testRandom.setVendDisplay()
						secondDisplay = testRandom.getVendDisplay()
						self.assertEqual("{0:.2f}".format(number  + secondNumber), secondDisplay)
					else: 
						checkReturn =  testRandom.getVendDisplay()
						self.assertEqual(float(display), number)

				else: 
					checkReturn =  testRandom.getReturnCoin()
					self.assertEqual(checkReturn, number)
					
					#check to see that correct amount has been inserted
					amountInserted = testRandom.getTotalInserted()
					self.assertEqual(amountInserted, 0)
					
					#this should be the coin inserted because this is an invalid coin 
					checkReturn =  testRandom.getReturnCoin()
					self.assertEqual(number, checkReturn)

					#this check the display
					display = testRandom.getVendDisplay()
					self.assertEqual(display, "INSERT COIN")

	
if __name__ == '__main__':
    unittest.main()