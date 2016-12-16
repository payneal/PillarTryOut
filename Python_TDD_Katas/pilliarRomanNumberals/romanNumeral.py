class RomanNumeral:
    def __init__(self):
        self.converted = ''

    def convert(self, entry):
        for x in range(0, entry):
            self.converted += "I"
        return self.__check()

    def __check(self):
        if len(self.converted) > 3:
            return "IX"
        return self.converted
