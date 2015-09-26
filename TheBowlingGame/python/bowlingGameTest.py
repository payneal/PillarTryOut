import unittest

from bowlingGame import Game

#used to verify scores
#http://www.bowlinggenius.com/
class TestBowlingGame(unittest.TestCase):
	def setUp(self):
		self.game = Game()  

	def test_to_check_all_gutter_balls_game(self):
		self.roll_this_many_times_hit_this_many_pins(20, 0)
		self.assertEqual(self.game.score(), 0)

	def test_to_check_all_ones(self):
		self.roll_this_many_times_hit_this_many_pins(20, 1)
		self.assertEqual(self.game.score(), 20)

	def test_to_check_rolling_one_spare(self):
		self.game.roll(7)
		self.game.roll(3)
		self.game.roll(5)
		self.roll_this_many_times_hit_this_many_pins(17, 0)
		self.assertEqual(self.game.score(), 20)

	def test_to_check_rolling_one_strike(self): 
		self.game.roll(10)
		self.game.roll(3)
		self.game.roll(5)
		self.roll_this_many_times_hit_this_many_pins(16, 0)
		self.assertEqual(self.game.score(), 26)

	def test_to_check_spare_in_the_10th_that_no_more_than_3_balls_can_be_rolled(self): 
		self.roll_this_many_times_hit_this_many_pins(18, 0)
		self.game.roll(7)
		self.game.roll(3)
		self.game.roll(5)
		
		self.assertEqual(self.game.score(), 15)

		self.assertEqual(self.game.roll(5), "no more than three balls can be rolled in tenth frame")
		self.assertEqual(self.game.score(), 15)

	def test_to_check_strike_in_the_10th_that_no_more_than_3_balls_can_be_rolled(self):
		self.roll_this_many_times_hit_this_many_pins(18, 0)
		self.game.roll(10)
		self.game.roll(10)
		self.game.roll(10)

		self.assertEqual(self.game.score(), 30)
		self.assertEqual(self.game.roll(5), "no more than three balls can be rolled in tenth frame")
		self.assertEqual(self.game.score(), 30)

	def test_300_perfect_game(self):
		self.roll_this_many_times_hit_this_many_pins(12, 10)
		self.assertEqual(self.game.score(), 300)

	def test_all_spare_game(self):
		self.roll_this_many_times_hit_this_many_pins(21, 5)
		self.assertEqual(self.game.score(), 150)		

	
	def roll_this_many_times_hit_this_many_pins(self, rolls, pinsHit): 
		for x in range(rolls): 
			self.game.roll(pinsHit)

if __name__ == '__main__':
    unittest.main()
