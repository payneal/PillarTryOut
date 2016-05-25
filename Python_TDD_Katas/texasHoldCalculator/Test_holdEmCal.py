import unittest

from holdEmCal import tableHand

class TestHoldemCalculator(unittest.TestCase):
	def setUp(self):
		pass

	def test_check_the_odds_of_getting_pair_when_pair_was_dealt(self): 
		hand = tableHand()
		cards = {"cardOne": {"rank":"ace", "suit":"dimond"}, "cardTwo":{"rank":"ace", "suit":"spade"}}
		hand.myCards(cards)
		percent = hand.chancesOfPair()
		self.assertEqual(percent, 100)

	def test_check_the_odds_of_getting_pair_when_pair_not_dealt(self): 
		hand = tableHand()
		cards = {"cardOne":{"rank":"ace", "suit":"dimond"}, "cardTwo":{"rank":"2", "suit":"spade"}}
		hand.myCards(cards)
		percent = hand.chancesOfPair()
		self.assertEqual(percent, 49)

if __name__ == '__main__':
    unittest.main()