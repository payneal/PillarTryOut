import unittest
from matchMyHusband import MatchMyHusband

class TestMatchMyHusband(unittest.TestCase):


# Test.assert_equals(match([15,24,12], 4), "No match!")
    def test_case1(self):
        mansNumbers = [15,24,12]
        womansOnlineLength = 4
        matchMyHusband = \
            MatchMyHusband(mansNumbers, womansOnlineLength)
        self.assertEqual(matchMyHusband.result(), "No Match!")

# Test.assert_equals(match([26,23,19], 3), "Match!")
    def test_case2(self):
        mansNumbers = [26,23,19]
        womansOnlineLength = 3
        matchMyHusband = \
            MatchMyHusband(mansNumbers, womansOnlineLength)
        self.assertEqual(matchMyHusband.result(), "Match!")

# Test.assert_equals(match([11,25,36], 1), "No match!")
    def test_case3(self):
        mansNumbers = [11,25,36]
        womansOnlineLength = 1
        matchMyHusband = \
            MatchMyHusband(mansNumbers, womansOnlineLength)
        self.assertEqual(matchMyHusband.result(), "No Match!")

# Test.assert_equals(match([22,9,24], 5), "Match!")
    def test_case4(self):
        mansNumbers = [22,9,24]
        womansOnlineLength = 5
        matchMyHusband = \
            MatchMyHusband(mansNumbers, womansOnlineLength)
        self.assertEqual(matchMyHusband.result(), "Match!")

# Test.assert_equals(match([8,11,4], 10), "Match!")
    def test_case5(self):
        mansNumbers = [8,11,4]
        womansOnlineLength = 10
        matchMyHusband = \
            MatchMyHusband(mansNumbers, womansOnlineLength)
        self.assertEqual(matchMyHusband.result(), "Match!")

# Test.assert_equals(match([17,31,21], 2), "No match!")
    def test_case6(self):
        mansNumbers = [17,31,21]
        womansOnlineLength = 2
        matchMyHusband = \
            MatchMyHusband(mansNumbers, womansOnlineLength)
        self.assertEqual(matchMyHusband.result(), "No Match!")

# Test.assert_equals(match([34,25,36], 1), "Match!")
    def test_case7(self):
        mansNumbers = [34,25,36]
        womansOnlineLength = 1
        matchMyHusband = \
            MatchMyHusband(mansNumbers, womansOnlineLength)
        self.assertEqual(matchMyHusband.result(), "Match!")

# Test.assert_equals(match([35,35,29], 0), "No match!")
    def test_case8(self):
        mansNumbers = [35,35,29]
        womansOnlineLength = 0
        matchMyHusband = \
            MatchMyHusband(mansNumbers, womansOnlineLength)
        self.assertEqual(matchMyHusband.result(), "No Match!")

# Test.assert_equals(match([35,35,30], 0), "Match!")
    def test_case9(self):
        mansNumbers = [35,35,30]
        womansOnlineLength = 0
        matchMyHusband = \
            MatchMyHusband(mansNumbers, womansOnlineLength)
        self.assertEqual(matchMyHusband.result(), "Match!")

#Test.assert_equals(match([35,35,31], 0), "Match!")
    def test_case10(self):
        mansNumbers = [35,35,31]
        womansOnlineLength = 0
        matchMyHusband = \
            MatchMyHusband(mansNumbers, womansOnlineLength)
        self.assertEqual(matchMyHusband.result(), "Match!")

if __name__ == '__main__':
    unittest.main()

