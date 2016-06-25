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

    def test_second_cola_is_a_double(self):
        names = ['Mike', 'Jon']
        double = 2
        answer = 'Jon'
        winner = self.doubleCola.whoIsNext(names, double)
        self.assertEqual(winner, answer)

    def test_case_given_1(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
        double = 52
        answer = "Penny"
        winner = self.doubleCola.whoIsNext(names, double)
        self.assertEqual(winner, answer)

    def test_case_given_2(self):
        names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
        double = 7230702951
        answer = "Leonard"
        winner = self.doubleCola.whoIsNext(names, double)
        self.assertEqual(winner, answer)

if __name__ == '__main__':
    unittest.main()
