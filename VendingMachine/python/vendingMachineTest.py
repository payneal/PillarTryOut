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

#did this for new test because test werent ran in order 
test3 = machine()

#this creates required prducts via pillar kata
items =  products()

class TestMachine(unittest.TestCase):
	def setUp(self): 
		pass

	def test_initial_display(self):	
		#check the display
		display = test.getVendDisplay() 
		self.assertEqual(display, 'EXACT CHANGE ONLY')

	def test_initial_amount(self): 
		#make sure that that no money has been inserted
		display = test.getTotalInserted()
		self.assertEqual(display, 0.00)

	def test_items_in_Vmachine(self): 
		#make sure there are no itemsin the machine
		inMachine = test.getAllItems()
		self.assertEqual(inMachine, {})

	def test_look_in_return_Bin(self): 
		#make sure that the return bin is emty
		binCoin = test.getReturnCoins()
		self.assertEqual(binCoin, [])

	def test_insert_coins(self):
		#insert a dime in the vending machine
		test.insertCoin('dime')
		#make sure there is nothing in the return coin bin
		checkReturn=  test.getReturnCoins()
		self.assertEqual(checkReturn, [])
		#make sure that therehas been $.10 inserted in the vending machine
		amountInserted = test.getTotalInserted()
		self.assertEqual(amountInserted, .10)

		display = test.getVendDisplay() 
		self.assertEqual(display, "$0.10")

		#test inserting multiple coins
		test.insertCoin('nickle')
		#check the return bin make sure its empty
		checkReturn=  test.getReturnCoins()
		self.assertEqual(checkReturn, [])
		#make sure that there hace been $.15 inserted in the machine
		amountInserted = test.getTotalInserted()
		self.assertEqual(amountInserted, .15)


	def test_updated_display(self):	
		#make sure that display starts $.15 in the machine
		display = test.getVendDisplay() 
		self.assertEqual(display, "$0.15")

		#double check it make sure it says the same
		display = test.getVendDisplay() 
		self.assertEqual(display, "$0.15")


	def test_instert_bad_coin(self): 
		#test inserting a fake coin
		test.insertCoin('fake')
		#make sure that fake coin is automatically inserted in return bin
		checkReturn=  test.getReturnCoins()
		self.assertEqual(checkReturn, ['fake'])

		#clear return bin
		test.clearReturnedCoin()
		#make sure there is still .15 in machine
		amountInserted = test.getTotalInserted()
		self.assertEqual(amountInserted, .15)	

		display = test.getVendDisplay() 
		self.assertEqual(display, "$0.15")

	def test_insert_invalid_Coin(self):
		#test inserting an invalid coin 
		test.insertCoin('half')
		#check the return coin bin make sure that non-valid con is in there 
		checkReturn=  test.getReturnCoins()
		self.assertEqual(checkReturn, ['half'])
		#make sure that there is .50 cents  in the return bin=
		checkReturn=  test.getReturnCoinAmount()
		self.assertEqual(checkReturn, .50)

		#mclear return bin
		test.clearReturnedCoin()
		#make sure only $.15 cents inserted
		amountInserted = test.getTotalInserted()
		self.assertEqual(amountInserted, .15)	

		display = test.getVendDisplay() 
		self.assertEqual(display, "$0.15")

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
		#make sure dispay matches this
		result = test2.showItems()
		self.assertEqual(result,buyables)

	def test_buy_button_Bad_functionality(self): 
		#give machine money $.50 so can only buy one item
		test2.insertCoin('quarter')
		test2.insertCoin('quarter')
		#make sure the inserted amount is $.50
		amountInserted = test2.getTotalInserted()
		self.assertEqual(amountInserted, .50)

		#display should say amount
		display = test2.getVendDisplay() 
		self.assertEqual(display, "$0.50")

		#this is if buying cola thats too expensive
		#buy a cola
		test2.buyItem(1)
		#make sure display shows price of item
		result= test2.getVendDisplay()
		self.assertEqual(result, 'PRICE = $1.00')


		result= test2.getVendDisplay()
		self.assertEqual(display, "$0.50")


	def test_buy_button_good_functionality(self):
		amountInserted = test2.getTotalInserted()
		self.assertEqual(amountInserted, .50)

		coinsInserted = test2.getCoinsInserted()
		self.assertEqual(coinsInserted, ['quarter', 'quarter'])
		 
		#this is if buying chips that you can afford
		result = test2.buyItem(2)

		#check amont in machine
		result= test2.getTotalInserted()
		self.assertEqual(result, 0)

		coinsInserted = test2.getCoinsInserted()
		self.assertEqual(coinsInserted, [])
		
		#check that item has been given
		result= test2.checkQty(2)
		self.assertEqual(result, 9)

		#check display message
		result= test2.getVendDisplay()
		self.assertEqual(result, 'THANK YOU')

		#second check of display
		result= test2.getVendDisplay()
		self.assertEqual(result, 'EXACT CHANGE ONLY')

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

		coinsInserted = test2.getCoinsInserted()
		self.assertEqual(coinsInserted, ['quarter', 'quarter', 'dime'])

		#this is if buying chips that you can afford
		test2.buyItem(2)

		#check that item has been given
		result= test2.checkQty(2)
		self.assertEqual(result, 8)

		#check display message
		result= test2.getVendDisplay()
		self.assertEqual(result, 'THANK YOU')

		#second check of display
		result= test2.getVendDisplay()
		self.assertEqual(result, 'EXACT CHANGE ONLY')

		
		#check amount returned
		result= test2.getReturnCoinAmount()
		self.assertEqual(result, .10)

		result= test2.getReturnCoins()
		self.assertEqual(result, ['dime'])

		#grab the change
		test2.clearReturnedCoin()
		result= test.getReturnCoinAmount()
		self.assertEqual(result, 0.00)	
		result= test2.getReturnCoins()
		self.assertEqual(result, [])	


		#i think this is the issue

	def test_return_Coins(self): 
		#insert $.25
		test2.insertCoin('quarter')

		#make sure there is a quarter (value) in machine
		amountInserted = test2.getTotalInserted()
		self.assertEqual(amountInserted, .25)

		#make sure there is a quarter in the machine
		coinsInserted = test2.getCoinsInserted()
		self.assertEqual(coinsInserted, ['quarter'])

		display = test2.getVendDisplay() 
		self.assertEqual(display, "$0.25")


		#hit the return button
		test2.returnButton()

		#see change in return bin
		returnCoins = test2.getReturnCoins()
		self.assertEqual(returnCoins, ['quarter'])

		returnAmount = test2.getReturnCoinAmount()
		self.assertEqual(returnAmount, .25)

		# get change out of return bin 
		test2.clearReturnedCoin()

		#make sure machine inserted money is 0 
		amountInserted = test2.getTotalInserted()
		self.assertEqual(amountInserted, 0)

		#make sure coins in machine = []
		coinsInserted = test2.getCoinsInserted()
		self.assertEqual(coinsInserted, [])

		#make sure display is insert coins
		result= test2.getVendDisplay()
		self.assertEqual(result, 'EXACT CHANGE ONLY')

	def test_sold_out(self): 
		#check how many chips are left 
		#although I started a new class for this there will still only be 8 
		#bags of chips because of line: 12 on vendingMachine.py
		result= test3.checkQty(2)
		self.assertEqual(result, 8)

		insertMoneyCheck = .50 
		insertCheck = ['quarter', 'dime', 'dime', 'nickle']
		cashInMachin =  0
		checkagainst = []
		#make sure display is insert coins
		result= test3.getVendDisplay()
		self.assertEqual(result, 'EXACT CHANGE ONLY')
		
		chips= 8
		#we need to buy 10 candies to get sold out
		for i in range(8): 
			#insert $.50
			test3.insertCoin('quarter')
			test3.insertCoin('dime')
			test3.insertCoin('dime')
			test3.insertCoin('nickle')

			#adding to what im checking the machine against
			checkagainst.append('quarter')
			for x in range(2):
				checkagainst.append('dime')
			checkagainst.append('nickle')

			coinsInserted = test3.getCoinsInserted()
			self.assertEqual(coinsInserted, insertCheck)

			cashInMachin = cashInMachin +.5

			amountInserted = test3.getTotalInserted()
			self.assertEqual(amountInserted, insertMoneyCheck)


			#this is if buying chips that you can afford
			test3.buyItem(2)

			result = test3.getAmountInMachine()
			self.assertEqual(result, cashInMachin)

			coinsInserted = test3.getCoinsInserted()
			self.assertEqual(coinsInserted, [])



			result = test3.getCoinsInMachine()
			self.assertEqual(checkagainst, result)


			#lower the chips varible
			chips= chips - 1

			#check that item has been taken away in amount in stock
			result= test3.checkQty(2)
			self.assertEqual(result, chips)

			#check display message
			result= test3.getVendDisplay()
			self.assertEqual(result, 'THANK YOU')

			result = test3.getCoinsInMachine()
			self.assertEqual(checkagainst, result)


			#second check of display
			#it should display Insert coins because there should now be money in the machine
			result= test3.getVendDisplay()
			self.assertEqual(result, "INSERT COINS")

		#verify that chips are at 0 
		result= test3.checkQty(2)
		self.assertEqual(result, 0)

		#Insert $.50 cents
		test3.insertCoin('quarter')
		test3.insertCoin('quarter')

		display = test3.getVendDisplay() 
		self.assertEqual(display, "$0.50")

		#make sure there is enough money to buy item
		amountInserted = test3.getTotalInserted()
		self.assertEqual(amountInserted, .5)

		#buy chips again
		test3.buyItem(2)

		#the screen should display out of stock
		result= test3.getVendDisplay()
		self.assertEqual(result, 'SOLD OUT')

		#make sure machine inserted money is 0 
		amountInserted = test3.getTotalInserted()
		self.assertEqual(amountInserted, .50)

		#make sure coins in machine = []
		coinsInserted = test3.getCoinsInserted()
		self.assertEqual(coinsInserted, ['quarter', 'quarter'])

		#check screen again should disply amount of money since $.50 still in machine
		display = test3.getVendDisplay() 
		self.assertEqual(display, "$0.50")

		#hit the return button to empyty the insert
		test3.returnButton()

		#see change in return bin
		returnCoins = test3.getReturnCoins()
		self.assertEqual(returnCoins, ['quarter', 'quarter'])

		#make sure $.50 cents is the amount in return
		returnAmount = test3.getReturnCoinAmount()
		self.assertEqual(returnAmount, .5)

		# get change out of return bin 
		test3.clearReturnedCoin()

		#make sure machine inserted money is 0 
		amountInserted = test3.getTotalInserted()
		self.assertEqual(amountInserted, 0)

		#make sure coins in machine = []
		coinsInserted = test3.getCoinsInserted()
		self.assertEqual(coinsInserted, [])

		#check the display again should show 'INSERT COINS'
		result= test3.getVendDisplay()
		self.assertEqual(result, "INSERT COINS")

		result = test3.getCoinsInMachine()


		self.assertEqual(result, checkagainst)
		
		result = test3.getAmountInMachine()
		self.assertEqual(result, 4.00)

	def test_sure_coins_retuned(self): 
		#make sure money is in machine	
		result = test3.getAmountInMachine()
		self.assertEqual(result, 4.00)

		#make sure doenst require exact change
		result= test3.getVendDisplay()
		self.assertEqual(result, "INSERT COINS")

		#insert 3 quarters in machine
		#Insert $.50 cents
		test3.insertCoin('quarter')
		test3.insertCoin('quarter')
		test3.insertCoin('quarter')

		#make sure machine inserted money 
		amountInserted = test3.getTotalInserted()
		self.assertEqual(amountInserted, .75)

		#make sure display is correct
		display = test3.getVendDisplay() 
		self.assertEqual(display, "$0.75")

		#make sure nothing is in the return bin
		returnCoins = test3.getReturnCoins()
		self.assertEqual(returnCoins, [])

		#make buy of candy
		test3.buyItem(3)

		#make sure .10 is in return bin it will be a dime becuase dimes are in machine
		returnCoins = test3.getReturnCoins()
		self.assertEqual(returnCoins, ['dime'])

		#make sure $.10 cents is the amount in return
		returnAmount = test3.getReturnCoinAmount()
		self.assertEqual(returnAmount, .1)

		#check display message
		result= test3.getVendDisplay()
		self.assertEqual(result, 'THANK YOU')

		#check display message
		result= test3.getVendDisplay()
		self.assertEqual(result, "INSERT COINS")

		#make sure that candy was bought
		result= test3.checkQty(3)
		self.assertEqual(result, 9)		

		#clear return bin 
		test3.clearReturnedCoin()

		#make sure .10 is in return bin it will be a dime becuase dimes are in machine
		returnCoins = test3.getReturnCoins()
		self.assertEqual(returnCoins, [])

		#make sure $.10 cents is the amount in return
		returnAmount = test3.getReturnCoinAmount()
		self.assertEqual(returnAmount, 0)









if __name__ == '__main__':
    unittest.main()



