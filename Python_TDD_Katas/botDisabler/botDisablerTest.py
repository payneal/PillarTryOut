import unittest
from botDisabler import BotDisabler


class TestBotDisabler(unittest.TestCase):
    def setUp(self):
        self.botDisabler = BotDisabler()

    def tearDown(self):
        self.botDisabler = None

    def test_first_bot_check(self):
        log = '1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031 1031'  # NOQA
        self.assertEqual(
            self.botDisabler.search_disable(log),
            "match disable bot")

    def test_second_bot_check(self):
        log = '2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031 2031'  # NOQA
        self.assertEqual(
            self.botDisabler.search_disable(log),
            "no match continue")

    def test_third_bot_check(self):
        log = '7693 3051 1999 7307 4323 4968 2666 4267 9264 2399 66 5739 300 9119 2399 5177 4649 2492 2471 7301 6192 9981 1828 2698 9386 8967 1502 9014 8799 5098 7155 5090 3909 2096 6296 2835 5746 9291 2312 6419 1740 1998 6281 3328 7590 3903 4197 1804 2223 7495 4483 234 9294 9882 2793 6959 320 3495 3540 5308 6453 8666 921 4174 7987 6834 6755 4487 8396 2577 9191 6323 2684 2914 7651 2941 2897 3401 409 4381 9679 6791 927 6590 1683 2118 423 8844 7565 7052 9809 6121 6263 1614 9606 4078 7386 5360 8982'  # NOQA
        self.assertEqual(
            self.botDisabler.search_disable(log),
            "no match continue")

    def test_fourth_bot_check(self):
        log = '8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923 5639 2423 3929 7723 8923'  # NOQA
        self.assertEqual(
            self.botDisabler.search_disable(log),
            "match disable bot")

    def test_fifth_bot_check(self):
        log = '5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 5639 2423 2423 2423 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929 3929'  # NOQA
        self.assertEqual(
            self.botDisabler.search_disable(log),
            "no match continue")

if __name__ == '__main__':
    unittest.main()