import unittest

from redPencil import Shop

class TestRedPencil(unittest.TestCase):
	def setUp(self):
		pass

	def test_adding_item_to_store(self): 
		store = Shop()
		store.addItem('shoe')

		items = store.getAllItems()

		self.assertEqual(items, ["shoe"])



if __name__ == '__main__':
    unittest.main()
