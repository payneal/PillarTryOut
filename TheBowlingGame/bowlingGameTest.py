import unittest

from bowlingGame import Game

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


	def roll_this_many_times_hit_this_many_pins(self, rolls, pinsHit): 
		for x in range(rolls): 
			self.game.roll(pinsHit)


if __name__ == '__main__':
    unittest.main()
