import unittest
from doubleCola import DoubleCola


class TestDoubleCola(unittest.TestCase):
    def setUp(self):
        self.doubleCola = DoubleCola()

    def test_first_cola_is_a_double(self):
        names = ['Mike', 'Jon']
        double = 1
        answer = 'Mike'
        winner = self.doubleCola.whoIsNext(names, double)
        self.assertEqual(winner, answer)

if __name__ == '__main__':
    unittest.main()
