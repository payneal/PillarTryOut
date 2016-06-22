import unittest
from stopSpinningMyWords import StopSpinningMyWords


class TestSpinningMyWords(unittest.TestCase):

    def test_No_word_should_be_changed(self):
        string = "I"
        spinner = StopSpinningMyWords(string)
        self.assertEqual(string, spinner.string)

    def test_one_word_should_be_changed(self):
        string = "Welcome"
        spinner = StopSpinningMyWords(string)
        self.assertEqual("emocleW", spinner.string)

    def test_two_words_one_reverse_one_not(self):
        string = "This is another test"
        spinner = StopSpinningMyWords(string)
        self.assertEqual("This is rehtona test", spinner.string)

    def test_case_1(self):
        string = "Hey fellow warriors"
        spinner = StopSpinningMyWords(string)
        self.assertEqual("Hey wollef sroirraw", spinner.string)

    def test_case_2(self):
        string = "This is a test"
        spinner = StopSpinningMyWords(string)
        self.assertEqual("This is a test", spinner.string)

    def test_case_3(self):
        string = "when Just the words or name or when " + \
            "five word function and be one is"
        reverse = "when Just the sdrow or name or when " + \
            "five word noitcnuf and be one is"

        spinner = StopSpinningMyWords(string)
        self.assertEqual(reverse, spinner.string)

if __name__ == '__main__':
    unittest.main()
