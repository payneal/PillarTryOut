import unittest
import time

from redPencil import Shop

class TestRedPencil(unittest.TestCase):
	def setUp(self):
		self.store = Shop()

	def getTodaysDate(self):
		return time.strftime('%m-%d-%y')

	def test_adding_two_items_with_prices(self):
		self.store.addItem('shoe',5.00)
		self.store.addItem('tie',4.00)
		items = self.store.getAllItems()
		self.assertEqual(items, [{'shoe':{'price':5.00}}, {'tie':{'price':4.00}}])

	def test_changing_the_price_of_an_item(self):
		self.store.addItem('shoe',5.00)
		self.store.changePrice('shoe',4.50)
		items = self.store.getAllItems()
		self.assertEqual(items, [{'shoe':{'price':4.50}}])

	def test_changing_price_by_one_percent_doesnt_start_red_pencil(self):
		self.store.addItem('shoe',100.00)
		self.store.changePrice('shoe',99.00)
		answer = self.store.isOnRedPencileSale('shoe')
		self.assertFalse(answer)

	def test_changing_price_by_five_percent_does_start_red_pencil(self): 
		self.store.addItem('shoe',100.00)
		self.store.changePrice('shoe',95.00)
		answer = self.store.isOnRedPencileSale('shoe')
		self.assertTrue(answer)

	def test_changing_price_by_31_percent_doesnt_start_red_pencil(self):
		self.store.addItem('shoe',100.00)
		self.store.changePrice('shoe',69.00)
		answer = self.store.isOnRedPencileSale('shoe')
		self.assertFalse(answer)

	def test_checking_stable_days_of_just_added_item(self):
		self.store.addItem('shoe',100.00)
		answer = self.store.checkDaysPriceItemStable('shoe')
		self.assertEqual(answer,0)

	def test_adding_item_store_gives_items_price_change_date_of_today(self):
		self.store.addItem('shoe',100.00)
		answer = self.store.lastPriceChangeDate('shoe')
		#TDD like hard values but thats not possible here ddate changes every day
		today = self.getTodaysDate()
		self.assertEqual(answer,today)

	def test_adding_item_to_store_on_cetrain_date(self):
		self.store.addItem('shoe',100.00, '1-1-15')
		answer = self.store.lastPriceChangeDate('shoe')
		self.assertEqual(answer, '1-1-15')

if __name__ == '__main__':
    unittest.main()











