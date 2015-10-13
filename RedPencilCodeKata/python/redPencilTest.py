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

if __name__ == '__main__':
    unittest.main()
