# Tests
import unittest
from titleCreator import TitleCreator

class TestStockHighNyse(unittest.TestCase):
    
    
    def test_if_one_argument_passed__then_return_same_string(self):
        string = '';
        createdTitle = TitleCreator(string)
        self.assertEqual(string, createdTitle.titleCreator())
    # itle_case('a clash of KINGS', 'a an the of') # should return: 'A Clash of Kings'
    def test_one_A_Clash_of_Kings(self):
        string = 'a clash of Kings'
        caps = 'a an the of'
        createdTitle = TitleCreator(string, caps)
        self.assertEqual('A Clash of Kings', createdTitle.titleCreator())

    def test_THE_WIND_IN_THE_WILLOWS(self):
        string = 'THE WIND IN THE WILLOWS'
        caps = 'The In'
        createdTitle = TitleCreator(string, caps)
        self.assertEqual('The Wind in the Willows', createdTitle.titleCreator())

if __name__ == '__main__':
    unittest.main()
