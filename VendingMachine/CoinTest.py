# so that I can test the vaild inserts of money
import unittest

#so that I can test the money
from Coin import coins

#used for random testing 
from random import randint


class TestMoneyUnits(unittest.TestCase):
	def setUp(self): 
		pass

	def test_Valid_Coins(self):		

		#hard coded test 

		#used  to test invalid Coins 
		test1 = coins(.00) 
		test2 = coins(.35)
		test3 = coins(1.00)
		
		#used to test valid Coins 
		test4 = coins(.05)
		test5 = coins(.10)
		test6 = coins(.25)
			
		#the test 
		#testing if amount entered was correct
		self.assertEqual(test1.getAmount(), .00)

		#testing if valid coin insterted or not
		self.assertEqual(test1.check(), False)
		self.assertEqual(test2.check(), False)
		self.assertEqual(test3.check(), False)
		self.assertEqual(test4.check(), .05)
		self.assertEqual(test5.check(), .1)
		self.assertEqual(test6.check(), .25)
		

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

