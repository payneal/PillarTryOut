import unittest

from redPencil import Shop

class TestRedPencil(unittest.TestCase):
	def setUp(self):
		self.store = Shop()

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

if __name__ == '__main__':
    unittest.main()
