import unittest
from datetime import timedelta, date

from redPencil import Shop

class TestRedPencil(unittest.TestCase):
	def setUp(self):
		self.store = Shop()

	def getTodaysDate(self):
		return str(date.today())

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
		self.store.addItem('shoe',100.00, '2015-1-1')
		self.store.changePrice('shoe',99.00)
		answer = self.store.isOnRedPencileSale('shoe')
		self.assertFalse(answer)

	def test_changing_price_by_five_percent_does_start_red_pencil(self): 
		self.store.addItem('shoe',100.00, '2015-1-1')
		self.store.changePrice('shoe',95.00)
		answer = self.store.isOnRedPencileSale('shoe')
		self.assertTrue(answer)

	def test_changing_price_by_31_percent_doesnt_start_red_pencil(self):
		self.store.addItem('shoe',100.00, '2015-1-1')
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
		self.store.addItem('shoe',100.00, '2015-1-1')
		answer = self.store.lastPriceChangeDate('shoe')
		self.assertEqual(answer, '2015-1-1')

	def test_adding_item_past_date_but_change_price_so_price_change_date_is_today(self):
		self.store.addItem('shoe',100.00, '2015-1-1')
		self.store.changePrice('shoe',69.00)
		answer = self.store.lastPriceChangeDate('shoe')
		today = self.getTodaysDate()
		self.assertEqual(answer,today)

	def test_checking_stable_days_of_item_added_awhile_ago(self): 
		yesterday = str(date.today() - timedelta(days=1))
		self.store.addItem('shoe',100.00, yesterday)
		answer = self.store.checkDaysPriceItemStable('shoe')
		self.assertEqual(answer,1)

	def test_changing_price_when_it_hasnt_been_past_30days_no_redPencile_status(self): 
		self.store.addItem('shoe',100.00)
		self.store.changePrice('shoe',90.00)
		answer = self.store.isOnRedPencileSale('shoe')
		self.assertFalse(answer)

	def test_can_we_set_the_day_the_price_changed(self):
		self.store.addItem('shoe',100.00, '2015-1-1')
		self.store.changePrice('shoe',99.00,'2015-10-10')
		answer = self.store.lastPriceChangeDate('shoe')
		self.assertEqual(answer, '2015-10-10')

	def test_Changing_price_when_it_has_been_past_30days_item_status_is_redPencile_status(self):       
		self.store.addItem('shoe',100.00, '2015-1-1')
		self.store.changePrice('shoe',95.00, '2015-1-31')
		answer = self.store.isOnRedPencileSale('shoe')
		self.assertTrue(answer)

	def test_red_pencil_promotion_lasts_30_days_as_the_maximum_Length(self):
		self.store.addItem('shoe',100.00, '2015-1-1')
		self.store.changePrice('shoe',95.00, '2015-1-31')
		answer = self.store.isOnRedPencileSale('shoe')
		self.assertTrue(answer)
		answer = self.store.isOnRedPencileSale('shoe', '2015-3-2')
		self.assertTrue(answer)
		answer = self.store.isOnRedPencileSale('shoe', '2015-3-3')
		self.assertFalse(answer)

	def test_see_if_original_price_is_store(self):
		self.store.addItem('shoe',100.00, '2015-1-1')
		answer = self.store.getOriginalPrice('shoe')
		self.assertEqual(answer, 100)
		self.store.changePrice('shoe',95.00, '2015-1-31')
		answer = self.store.getOriginalPrice('shoe')
		self.assertEqual(answer, 100)

	#If the price is further reduced during the red pencil promotion
	# the promotion will not be prolonged by that reduction
	def test_price_is_reduced_further_while_on_red_pencil_which_ends_red_pencil_status(self): 
		self.store.addItem('shoe',100.00, '2015-1-1')
		self.store.changePrice('shoe',95.00, '2015-1-31')
		answer = self.store.isOnRedPencileSale('shoe', '2015-1-31')
		self.assertTrue(answer)
		self.store.changePrice('shoe',94.00, '2015-2-05')
		answer = self.store.isOnRedPencileSale('shoe','2015-3-01')
		self.assertTrue(answer)
		answer = self.store.isOnRedPencileSale('shoe','2015-3-02')
		self.assertFalse(answer)








if __name__ == '__main__':
    unittest.main()











