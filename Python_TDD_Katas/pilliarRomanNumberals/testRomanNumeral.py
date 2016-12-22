import unittest
from romanNumeral import RomanNumeral


class TestRomalNumeralConverter(unittest.TestCase):
    def setUp(self):
        self.romanNumeral = RomanNumeral()

    def tearDown(self):
        self.romanNumeral = None

    # feature 1

    def test_convert_0_to_None(self):
        self.assertEqual(self.romanNumeral.convert(0), "")

    def test_convert_1_to_I(self):
        self.assertEqual(self.romanNumeral.convert(1), "I")

    def test_convert_3_to_III(self):
        self.assertEqual(self.romanNumeral.convert(3), "III")

    def test_convert_4_to_IV(self):
        self.assertEqual(self.romanNumeral.convert(4), "IV")

    def test_convert_6_to_VI(self):
        self.assertEqual(self.romanNumeral.convert(6), "VI")

    def test_convert_9_to_IX(self):
        self.assertEqual(self.romanNumeral.convert(9), "IX")

    def test_convert_12_to_XII(self):
        self.assertEqual(self.romanNumeral.convert(12), "XII")

    def test_convert_13_to_XII(self):
        self.assertEqual(self.romanNumeral.convert(13), "XIII")

    def test_convert_16_to_XVI(self):
        self.assertEqual(self.romanNumeral.convert(16), "XVI")

    def test_convert_19_to_XIX(self):
        self.assertEqual(self.romanNumeral.convert(19), "XIX")

    def test_convert_20_to_XX(self):
        self.assertEqual(self.romanNumeral.convert(20), "XX")

    def test_convert_24_to_XXIV(self):
        self.assertEqual(self.romanNumeral.convert(24), "XXIV")

    def test_convert_27_to_XXIV(self):
        self.assertEqual(self.romanNumeral.convert(27), "XXVII")

    def test_convert_29_to_XXIX(self):
        self.assertEqual(self.romanNumeral.convert(29), "XXIX")

    def test_convert_39_to_XXXIX(self):
        self.assertEqual(self.romanNumeral.convert(39), "XXXIX")

    def test_convert_40_to_XL(self):
        self.assertEqual(self.romanNumeral.convert(40), "XL")

    # feature 2
    def test_convert_I_to_1(self):
        self.assertEqual(self.romanNumeral.convert('I'), 1)

if __name__ == '__main__':
    unittest.main()
