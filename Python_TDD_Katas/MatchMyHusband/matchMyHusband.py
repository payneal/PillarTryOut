class MatchMyHusband:

    def __init__(self, mansNumbers, womensOnlineLength):
       self.mansNumbers = mansNumbers
       self.womansOnlineLength = womensOnlineLength
       self.manSum = self.__calculateMansNumber()
       self.womansNumber = self.__calculateWomansNumber()

    def __calculateMansNumber(self):
        amount = 0
        for x in self.mansNumbers:
            amount = amount + x
        return amount

    def __calculateWomansNumber(self):
         amount = 100
         for x in range(0, self.womansOnlineLength):
             discount = int(amount * .15)
             amount = amount - discount
         return amount 

    def result(self):
        if self.manSum >= self.womansNumber:
            return "Match!"
        else:
            return "No Match!"
