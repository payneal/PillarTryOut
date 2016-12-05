class BotDisabler:
    def __init___(self):
        self.log = None

    def search_disable(self, log):
        log = log.split(' ')
        self.log = self.createDictOfLog(log)
        self.addPrimeStatusToLog()
        self.addCheckForDigitLength(4)
        self.verify3rdDigitIs2Or3()
        self.checkHighThan3ForCount()
        return self.getAnswer()

    def getAnswer(self):
        total = 0
        for x in self.log:
            prime = self.log[x]['prime']
            high = self.log[x]['highEnoughCount']
            threeOrTwo = self.log[x]['verify3rdDigit']
            digits = self.log[x]['length']

            if prime is True and high is True and\
                    threeOrTwo is True and digits is True:
                total += self.log[x]['count']
        if total > 50:
            return 'match disable bot'
        return 'no match continue'

    def checkHighThan3ForCount(self):
        for x in self.log:
            if self.log[x]['count'] > 3:
                self.log[x]['highEnoughCount'] = True
            else:
                self.log[x]['highEnoughCount'] = False

    def verify3rdDigitIs2Or3(self):
        for x in self.log:
            digit = None
            try:
                digit = x[2]
                if digit == '2' or digit == '3':
                    self.log[x]['verify3rdDigit'] = True
                else:
                    self.log[x]['verify3rdDigit'] = False
            except:
                self.log[x]['verify3rdDigit'] = False

    def addCheckForDigitLength(self, length):
        for x in self.log:
            if len(x) == length:
                self.log[x]['length'] = True
            else:
                self.log[x]['length'] = False

    def addPrimeStatusToLog(self):
        for x in self.log:
            primeStatus = self.checkIfNumIsPrime(int(x))
            self.log[x]['prime'] = primeStatus

    def createDictOfLog(self, log):
        data = {}
        for x in log:
            if x not in data:
                data[x] = {'count': 1}
            else:
                data[x]['count'] += 1
        return data

    def checkIfNumIsPrime(self, num):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    return False
            else:
                return True
        else:
            return False
