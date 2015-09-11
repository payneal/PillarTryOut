# System test
import unittest

#so that I can test the money
from vendingMachine import machine

#so that I can make buys
from Products import products

#used for random testing 
from random import randint

class TestMoneyUnits(unittest.TestCase):
	def setUp(self): 
		pass

	def test_initial_display(self):	
		# create the test
		test1 = machine()
		display = test1.getVendDisplay() 
		self.assertEqual(display, "INSERT COIN")

	def test_initial_amount(self): 
		test2 = machine()
		display = test2.getTotalInserted()
		self.assertEqual(display, 0)
	
	#change all of these to highest number I get to
	def test_adding_coin_Walkthrough(self):
		test3 = machine()

		#this is an attemt to insert a dime
		test3.insertCoin(.10)

		checkReturn=  test3.getReturnCoin()
		#check to make sure nothing is returned as in not accepeted
		self.assertEqual(checkReturn, None)

		#check to see that correct amount has been inserted
		amountInserted = test3.getTotalInserted()
		self.assertEqual(amountInserted, .10)

		#make sure that the display is correct and in the right formate
		test3.setVendDisplay()
		display = test3.getVendDisplay()
		self.assertEqual(display, "0.10")

		#Prolly should of seperated test here 
		#attempt to add a bad number and check everything
		test3.insertCoin(.01)

		#this should return the bad entry
		checkReturn=  test3.getReturnCoin()
		self.assertEqual(checkReturn, .01)

		#Prolly should of seperated test here 
		#now lets test the return coin clear function
		checkReturn=test3.clearReturnedCoin()
		self.assertEqual(checkReturn, None)

		#this should show that the told hasnt changed 
		amountInserted = test3.getTotalInserted()
		self.assertEqual(amountInserted, .10)

		#this should show that the display hasnt changed
		display = test3.getVendDisplay()
		self.assertEqual(display, "0.10")

		#Prolly should of seperated test here 
		#now lets add another coin and see if it works
		test3.insertCoin(.05)

		#this should return None because above was a good entry
		checkReturn=  test3.getReturnCoin()
		self.assertEqual(checkReturn, None)

		#this should show that the told has changed to .10 + .05  = 0.15
		amountInserted = test3.getTotalInserted()
		self.assertEqual(amountInserted, .15)

		#this should show that the display hasnt changed
		test3.setVendDisplay()
		display = test3.getVendDisplay()
		self.assertEqual(display, "0.15")

	def test_ability_to_display_Thanks(self):
		test4 = machine()
		test4.setVendDisplay(True)
		self.assertEqual(test4.getVendDisplay(),'THANKS')


	def test_adding_item_to_vending_vendingMachine(self): 
		#this creates vending machine
		test5 = machine()
		#this creates required prducts via pillar kata
		items =  products()
		#this puts all products in a varible
		allProducts = items.getAllProducts()
		#this puts all products in the machine
		test5.addAllItems(allProducts)
		#hold all items form vending machine
		theItemsInMachine = test5.getAllItems()
		
		# we want to test this to see if all Products are stored now in vending machine
		self.assertEqual(theItemsInMachine,allProducts)









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