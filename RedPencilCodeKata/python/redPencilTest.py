import unittest

from redPencil import Shop

class TestRedPencil(unittest.TestCase):
	def setUp(self):
		self.store = Shop()

	def test_adding_two_items_with_prices(self):
		self.store.addItem({'shoe':5.00})
		self.store.addItem({'tie':4.00})
		items = self.store.getAllItems()
		self.assertEqual(items, [{'shoe':5.00}, {'tie':4.00}])

if __name__ == '__main__':
    unittest.main()
