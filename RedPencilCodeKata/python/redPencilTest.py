import unittest

from redPencil import Shop

class TestRedPencil(unittest.TestCase):
	def setUp(self):
		self.store = Shop()

	def test_adding_item_to_store(self): 
		
		self.store.addItem('shoe')
		items = self.store.getAllItems()
		self.assertEqual(items, ["shoe"])

	def test_adding_two_items_to_store(self): 
		self.store.addItem('shoe')
		self.store.addItem('tie')
		items = self.store.getAllItems()
		self.assertEqual(items, ["shoe", "tie"])

if __name__ == '__main__':
    unittest.main()
