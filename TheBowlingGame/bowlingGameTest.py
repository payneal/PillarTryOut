import unittest

from bowlingGame import Game

class TestBowlingGame(unittest.TestCase):
	def setUp(self):
		self.game = Game()  

	def test_to_check_all_gutter_balls_game(self):
		for x in range(20): 
			self.game.roll(0)
		self.assertEqual(self.game.score(), 0)

	def test_to_check_all_ones(self):
		for x in range(20): 
			self.game.roll(1)
		self.assertEqual(self.game.score(), 20)


if __name__ == '__main__':
    unittest.main()
