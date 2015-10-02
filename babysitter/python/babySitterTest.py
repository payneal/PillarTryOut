import unittest

from babySitter import Sitter


class TestBabySitter(unittest.TestCase):
	def setUp(self):
		self.sitter = Sitter()

	def test_inputing_no_bedtime(self): 
		sitterPay = self.sitter.calculatePay("5PM","6PM")
		self.assertEqual(sitterPay, 12)

	def test_no_bedtime_work_full_day(self):
		sitterPay = self.sitter.calculatePay("5PM", "4AM")
		self.assertEqual(sitterPay, 148)

	def test_startTime_5_leaveTime_6_bedTime_7_hours_1_pay_12(self):
		sitterPay = self.sitter.calculatePay("5PM","6PM","7PM")
		self.assertEqual(sitterPay, 12)

	def test_startTime_5_leaveTime_7_bedtime_8_hours_2_pay_24(self):
		sitterPay = self.sitter.calculatePay("5PM","7PM","8PM")
		self.assertEqual(sitterPay, 24)

	def test_throws_execption_error_if_babysitter_start_time_before_5(self):
		with self.assertRaises(Exception) as context:
			self.sitter.calculatePay("4PM","6PM","7PM")
		self.assertTrue("Baby sitting starts no earlier than 5:00PM" in context.exception)

	def test_startTime_11_leaveTime_12_bedtime_11_hours_1_pay_8(self):
		sitterPay = self.sitter.calculatePay("11PM","12AM","11PM")
		self.assertEqual(sitterPay, 8)

	def test_startTime_10_leaveTime_12_bedtime_10_hours_2_bedTimeToMidnight_pay_16(self):
		sitterPay = self.sitter.calculatePay("10PM","12AM","10PM")
		self.assertEqual(sitterPay, 16)

	def test_1_hour_working_start_to_bed_and_one_hour_working_bed2midnight_pay_20(self):
		sitterPay = self.sitter.calculatePay("10PM","12AM","11PM")
		self.assertEqual(sitterPay, 20)

	def test_2_hours_working_start_to_bed_and_one_hour_working_midnight_pay_40(self):
		sitterPay = self.sitter.calculatePay("10PM","1AM","12AM")
		self.assertEqual(sitterPay, 40)

	def test_startTime_12am_leaveTime_1_bedtime_11_hours_1_testing_16_hour_pay_from_12am_to_end_of_Job(self): 
		sitterPay = self.sitter.calculatePay("12AM","1AM","11PM")
		self.assertEquals(sitterPay, 16)

	def test_startTime_12am_leaveTime_2_bedtime_11_hours_2_testing_32_hour_pay_from_12am_to_end_of_Job(self):
		sitterPay = self.sitter.calculatePay("12AM","2AM","11PM")
		self.assertEquals(sitterPay, 32)	

	def test_1hr_start2bed_1hr_bed2midnight_1hrmidnight2leave_pay36(self): 
		sitterPay = self.sitter.calculatePay("10PM","1AM","11PM")	
		self.assertEquals (sitterPay, 36)

	def test_work_full_day_bed_time_at_8pm_pay132(self): 
		sitterPay = sitterPay = self.sitter.calculatePay("5PM", "4AM", "8PM")
		self.assertEquals (sitterPay, 132)

	def test_gets_paid_for_full_hours_will_start_5_leave_6_15_Pay_12(self):
		sitterPay = sitterPay = self.sitter.calculatePay("5PM", "6:15PM")
		self.assertEquals (sitterPay, 36)


	def test_throws_execption_error_if_babysitter_leave_time_after_4(self):
		with self.assertRaises(Exception) as context:
			self.sitter.calculatePay("12AM","5AM","11PM")
		self.assertTrue("Baby sitting ends no later than 4:00AM" in context.exception)

if __name__ == '__main__':
    unittest.main()
