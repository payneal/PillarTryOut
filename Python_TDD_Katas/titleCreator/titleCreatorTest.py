# Tests
import unittest
from titleCreator import TitleCreator

class TestStockHighNyse(unittest.TestCase):
    
    
    def test_if_one_argument_passed__then_return_same_string(self):
        string = '';
        createdTitle = TitleCreator(string)
        self.assertEqual(string, createdTitle.titleCreator())
    
if __name__ == '__main__':
    unittest.main()
