import unittest
from romanNumeral import RomanNumeral


class TestRomalNumeralConverter(unittest.TestCase):
    def setUp(self):
        self.romanNumeral = RomanNumeral()

    def tearDown(self):
        self.converter = None

    def test_convert_1_to_I(self):
        self.assertEqual(self.romanNumeral.convert(1), "I")

if __name__ == '__main__':
    unittest.main()
