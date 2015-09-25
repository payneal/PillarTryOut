import unittest

from babySitter import Sitter

class TestBabySitter(unittest.TestCase):
	def setUp(self):
		pass

	def test_create_sitter(self):
		sitter = Sitter()

if __name__ == '__main__':
    unittest.main()
