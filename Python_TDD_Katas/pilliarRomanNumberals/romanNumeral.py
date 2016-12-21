class RomanNumeral:
    def __init__(self):
        self.converted = ''
        self.roman = [{'letter': 'I', 'value': 1, 'limit': 3},
                      {'letter': 'V', 'value': 5, 'limit': 1},
                      {'letter': 'X', 'value': 10, 'limit': 3}]
        self.numberGiver = None
        self.total = 0

    def convert(self, number):
        self.numberGiven = number
        indexOfRoman = self.__findClosestValueToNumber(number)
        self.__startConversionProcess(indexOfRoman, number)
        if "-" in self.converted:
            return self.__formatRomanNumeral()
        return self.converted

    def __formatRomanNumeral(self):
        numbers = self.converted.split('-')
        if len(numbers[0]) == 2:
            return numbers[1] + numbers[0]
        return numbers[0] + numbers[1]

    def __startConversionProcess(self, indexOfRoman, number):
        if number == self.roman[indexOfRoman]['value']:
            self.converted += self.roman[indexOfRoman]['letter']
        elif number < self.roman[indexOfRoman]['value']:
            self.__createConversionNumberLowerThanRoman(indexOfRoman, number)
        else:
            self.__createConversionNumberHigherThanRoman(indexOfRoman, number)

    def __findClosestValueToNumber(self, number):
        for index, x in enumerate(self.roman):
            subtractBy = 0
            if index > 0:
                subtractBy = self.roman[index - 1]
                subtractBy = subtractBy['limit'] * subtractBy['value']
            if x['value'] >= number - (subtractBy):
                return index
        return len(self.roman) - 1

    def __createConversionNumberLowerThanRoman(self, indexOfRoman, number):
        checkNumber = self.roman[indexOfRoman - 1]
        if number <= checkNumber['limit'] * checkNumber['value']:
            self.__addToConvertedString(False, number)
        else:
            self.__considerRomanNumeralRules(indexOfRoman, number)

    def __createConversionNumberHigherThanRoman(self, indexOfRoman, number):
        self.total += self.roman[indexOfRoman]['value']
        self.converted += self.roman[indexOfRoman]['letter']
        number -= self.roman[indexOfRoman]['value']
        indexOfRoman = self.__findClosestValueToNumber(number)
        self.__startConversionProcess(indexOfRoman, number)

    def __considerRomanNumeralRules(self, indexOfRoman, number):
        self.total += self.roman[indexOfRoman]['value']
        if self.total > self.numberGiven:
            self.converted += '-'
        self.converted += self.roman[indexOfRoman]['letter']
        difference = self.roman[indexOfRoman]['value'] - number
        self.__addToConvertedString(True, difference)

    def __addToConvertedString(self, addToFront, loopCount):
        for x in range(0, loopCount):
            if addToFront:
                self.converted = "I" + self.converted
            else:
                self.converted += "I"
