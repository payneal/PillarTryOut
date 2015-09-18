import unittest

from bowlingGame import Game

class TestBowlingGame(unittest.TestCase):
	
	def test_Start_a_game (self): 
		game  = Game() 

	def test_to_check_gutter_game(self):
		game = Game()
		for x in range(20): 
			game.roll(0)

		self.assertEqual(game.score(), 0)


if __name__ == '__main__':
    unittest.main()
