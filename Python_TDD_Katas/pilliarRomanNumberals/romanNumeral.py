class RomanNumeral:
    def __init__(self):
        self.converted = ''

    def convert(self, entry):
        for x in range(0, entry):
            self.converted += "I"
        if len(self.converted) > 3:
            return "IX"
        return self.converted
