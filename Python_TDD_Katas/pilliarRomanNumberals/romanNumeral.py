class RomanNumeral:
    def __init__(self):
        self.converted = ''
        self.roman = [{'letter': 'I', 'value': 1, 'limit': 3},
                      {'letter': 'V', 'value': 5, 'limit': 1},
                      {'letter': 'X', 'value': 10, 'limit': 3}]

    def convert(self, number):
        indexOfRoman = self.__findClosestValueToNumber(number)
        self.__startConversionProcess(indexOfRoman, number)
        return self.converted

    def __startConversionProcess(self, indexOfRoman, number):
        if number == self.roman[indexOfRoman]['value']:
            self.converted = self.roman[indexOfRoman]['letter']
        elif number < self.roman[indexOfRoman]['value']:
            self.__createConversionNumberLowerThanRoman(indexOfRoman, number)
        else:
            self.__createConversionNumberHigherThanRoman(indexOfRoman, number)

    def __findClosestValueToNumber(self, number):
        for index, x in enumerate(self.roman):
            if x['value'] >= number:
                return index
        return len(self.roman) - 1

    def __createConversionNumberLowerThanRoman(self, indexOfRoman, number):
        if number <= self.roman[indexOfRoman - 1]['limit']:
            self.__addToConvertedString(False, number)
        else:
            self.__considerRomanNumeralRules(indexOfRoman, number)

    def __createConversionNumberHigherThanRoman(self, indexOfRoman, number):
        self.converted += self.roman[indexOfRoman]['letter']
        number -= self.roman[indexOfRoman]['value']
        self.__startConversionProcess(indexOfRoman - 1, number)

    def __considerRomanNumeralRules(self, indexOfRoman, number):
        self.converted += self.roman[indexOfRoman]['letter']
        difference = self.roman[indexOfRoman]['value'] - number
        self.__addToConvertedString(True, difference)

    def __addToConvertedString(self, addToFront, loopCount):
        for x in range(0, loopCount):
            if addToFront:
                self.converted = "I" + self.converted
            else:
                self.converted += "I"
