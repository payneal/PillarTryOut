class RomanNumeral:
    def __init__(self):
        pass

    def convert(self, entry):
        roman = ""
        for x in range(0, entry):
            roman += "I"
        return roman
