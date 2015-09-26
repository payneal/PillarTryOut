import unittest

from babySitter import Sitter


class TestBabySitter(unittest.TestCase):
	def setUp(self):
		self.sitter = Sitter()

	def test_startTime_5_leaveTime_6_bedTime_7_hours_1_pay_12(self):
		sitterPay = self.sitter.calculatePay(5,6,7)
		self.assertEqual(sitterPay, 12)

	def test_startTime_5_leaveTime_7_bedtime_8_hours_2_pay_24(self):
		sitterPay = self.sitter.calculatePay(5,7,8)
		self.assertEqual(sitterPay, 24)

	def test_startTime_11_leaveTime_12_bedtime_11_hours_1_pay_8(self):
		sitterPay = self.sitter.calculatePay(11,12,11)
		self.assertEqual(sitterPay, 8)

	def test_startTime_10_leaveTime_12_bedtime_10_hours_2_bedTimeToMidnight_pay_16(self):
		sitterPay = self.sitter.calculatePay(10,12,10)
		self.assertEqual(sitterPay, 16)






		

if __name__ == '__main__':
    unittest.main()