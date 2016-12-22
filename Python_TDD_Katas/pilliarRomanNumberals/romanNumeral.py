class RomanNumeral:
    def __init__(self):
        self.converted = ''
        self.roman = [{'letter': 'I', 'value': 1, 'limit': 3},
                      {'letter': 'V', 'value': 5, 'limit': 1},
                      {'letter': 'X', 'value': 10, 'limit': 3}]
        self.numberGiven = None
        self.total = 0

    def convert(self, number):
        self.numberGiven = number
        self.__startConversionProcess(number)
        return self.__returnConvertedRomanNumeral()

    def __returnConvertedRomanNumeral(self):
        if "-" in self.converted:
            return self.__formatRomanNumeral()
        return self.converted

    def __formatRomanNumeral(self):
        numbers = self.converted.split('-')
        totalA = self.__getTotalFromRoman(numbers[0])
        totalB = self.__getTotalFromRoman(numbers[1])
        return self.__alterFormat(totalA, totalB, numbers)

    def __alterFormat(self, totalA, totalB, numbers):
        if totalA < totalB and self.numberGiven > 10:
            hold1 = numbers[0]
            hold2 = numbers[1]
            numbers[0] = hold2
            numbers[1] = hold1
        elif totalA > totalB:
            numbers[0] = numbers[0][::-1]
        return numbers[0] + numbers[1]

    def __getTotalFromRoman(self, number):
        total = 0
        for x in range(0, len(number)):
            if x == 0 and len(number) > 1:
                total -= self.__numeralToNumber(number[x])
            else:
                total += self.__numeralToNumber(number[x])
        return total

    def __numeralToNumber(self, letter):
        for x in self.roman:
            if x['letter'] == letter:
                return x['value']

    def __startConversionProcess(self, number):
        indexOfRoman = self.__findClosestValueToNumber(number)
        if number == self.roman[indexOfRoman]['value']:
            self.converted += self.roman[indexOfRoman]['letter']
        elif number < self.roman[indexOfRoman]['value']:
            self.__createConversionNumberLowerThanRoman(indexOfRoman, number)
        else:
            self.__createConversionNumberHigherThanRoman(indexOfRoman, number)

    def __findClosestValueToNumber(self, number):
        for index, x in enumerate(self.roman):
            subtractBy = self.__getNuberToSubtractBy(index)
            if x['value'] >= number - (subtractBy):
                return index
        return len(self.roman) - 1

    def __getNuberToSubtractBy(self, index):
        if index > 0:
            subtractBy = self.roman[index - 1]
            return subtractBy['limit'] * subtractBy['value']
        return 0

    def __createConversionNumberLowerThanRoman(self, indexOfRoman, number):
        checkNumber = self.roman[indexOfRoman - 1]
        if number <= checkNumber['limit'] * checkNumber['value']:
            self.__addToConvertedString(False, number)
        else:
            self.__considerRomanNumeralRules(indexOfRoman, number)

    def __createConversionNumberHigherThanRoman(self, indexOfRoman, number):
        self.__addToTotalAndConverted(indexOfRoman, number)
        number -= self.roman[indexOfRoman]['value']
        self.__startConversionProcess(number)

    def __considerRomanNumeralRules(self, indexOfRoman, number):
        self.__addToTotalAndConverted(indexOfRoman, number)
        difference = self.roman[indexOfRoman]['value'] - number
        self.__addToConvertedString(True, difference)

    def __addToTotalAndConverted(self, indexOfRoman, number):
        self.total += self.roman[indexOfRoman]['value']
        if self.total > self.numberGiven:
            self.converted += '-'
        self.converted += self.roman[indexOfRoman]['letter']

    def __addToConvertedString(self, addToFront, loopCount):
        for x in range(0, loopCount):
            if addToFront:
                self.converted = "I" + self.converted
            else:
                self.converted += "I"
