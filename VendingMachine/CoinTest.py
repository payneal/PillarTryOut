# so that I can test the vaild inserts of money
import unittest

#so that I can test the money
from Coin import coins

#used for random testing 
from random import randint

money = coins()

class TestMoneyUnits(unittest.TestCase):
	def setUp(self): 
		pass

	def test_if_penny_exist(self):		
		#test that penny exist
		amount = money.getAmount('penny')
		self.assertEqual(amount, .01)		

	def test_if_nickle_exist(self):	
		#test that nickle exist
		amount = money.getAmount('nickle')
		self.assertEqual(amount, .05)

	def test_if_dime_exist(self):	
		#test that dime exist
		amount = money.getAmount('dime')
		self.assertEqual(amount, .1)

	def test_if_quarter_exist(self):	
		#test that dime exist
		amount = money.getAmount('quarter')
		self.assertEqual(amount, .25)

	def test_if_half_exist(self):	
		#test that dime exist
		amount = money.getAmount('half')
		self.assertEqual(amount, .5)

	def test_if_coinDollar_exist(self):	
		#test that dime exist
		amount = money.getAmount('dollar')
		self.assertEqual(amount, 1.00)

	def test_if_FakeCoin_exist(self):	
		#test that dime exist
		amount = money.getAmount('fake')
		self.assertEqual(amount, None)
	
	#create random test once done (below is old one)
	if False:	
		def test_Random_valid_Coins(self):		
			#random test
			#valid numbers
			valid = [.05, .10, .25] 
			for i in range(100):
				#get random number 0-25
				number = randint(0,25)
				#make decimal (.0 to .25)
				testDec = float(number)/100
				#error check number sbeing used
				#print testDec

				testRandom = coins(testDec)

				self.assertEqual(testRandom.getAmount(), testDec)

				if testDec in valid:
					self.assertEqual(testRandom.check(), testDec)
				else: 
					self.assertEqual(testRandom.check(), False)								

if __name__ == '__main__':
    unittest.main()

