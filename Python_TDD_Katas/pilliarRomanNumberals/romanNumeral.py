class RomanNumeral:
    def __init__(self):
        self.converted = ''
        self.roman = [{'letter': 'I', 'value': 1, 'limit': 3},
                      {'letter': 'V', 'value': 5, 'limit': 1},
                      {'letter': 'X', 'value': 10, 'limit': 3}]

    def convert(self, number):
        indexOfRoman = self.__findClosestValueToNumber(number)
        if number == self.roman[indexOfRoman]['value']:
            self.converted = self.roman[indexOfRoman]['letter']
        else:
            self.__createConversionWithLowerRoman(indexOfRoman, number)
        return self.converted

    def __findClosestValueToNumber(self, number):
        for index, x in enumerate(self.roman):
            if x['value'] >= number:
                return index

    def __createConversionWithLowerRoman(self, indexOfRoman, number):
        if number <= self.roman[indexOfRoman - 1]['limit']:
            for x in range(0, number):
                self.converted += "I"
        else:
            self.converted += self.roman[indexOfRoman]['letter']
            difference = self.roman[indexOfRoman]['value'] - number
            for x in range(0, difference):
                self.converted = "I" + self.converted
