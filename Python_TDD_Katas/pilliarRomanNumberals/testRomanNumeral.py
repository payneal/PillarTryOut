import unittest
from romanNumeral import RomanNumeral


class TestRomalNumeralConverter(unittest.TestCase):
    def setUp(self):
        self.romanNumeral = RomanNumeral()

    def tearDown(self):
        self.romanNumeral = None

    def test_convert_0_to_None(self):
        self.assertEqual(self.romanNumeral.convert(0), "")

    def test_convert_1_to_I(self):
        self.assertEqual(self.romanNumeral.convert(1), "I")

    def test_convert_3_to_III(self):
        self.assertEqual(self.romanNumeral.convert(3), "III")

    def test_convert_4_to_IV(self):
        self.assertEqual(self.romanNumeral.convert(4), "IV")

    def test_convert_9_to_IX(self):
        self.assertEqual(self.romanNumeral.convert(9), "IX")

    def test_convert_12_to_XII(self):
        self.assertEqual(self.romanNumeral.convert(12), "XII")

    def test_convert_13_to_XII(self):
        self.assertEqual(self.romanNumeral.convert(13), "XIII")

    def test_convert_16_to_XVI(self):
        self.assertEqual(self.romanNumeral.convert(16), "XVI")

if __name__ == '__main__':
    unittest.main()
