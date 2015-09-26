import unittest

from babySitter import Sitter


class TestBabySitter(unittest.TestCase):
	def setUp(self):
		self.sitter = Sitter()

	def test_working_one_hour_from_start_Five_to_Leave_at_five(self):
			sitterPay = self.sitter.calculatePay(5,6)
			self.assertEqual(sitterPay, 12)


	
		

if __name__ == '__main__':
    unittest.main()
