class StopSpinningMyWords:

    def __init__(self, string):
        string = string.split(" ")
        self.string = self.__reverse(string)

    def __reverse(self, string):
        for idx, x in enumerate(string):
            if len(x) >= 5:
                string[idx] = x[::-1]
        return " ".join(string)
