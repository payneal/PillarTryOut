# Class

class TitleCreator:


    def __init__(self, string, lettersToCap=None):
        self.string = string.split(" ")
        self.letters = lettersToCap
        self.__checkIfNone()

    def __checkIfNone(self):
        if self.letters:
            self.letters = self.letters.split(" ")
    
    def __capFirstLetter(self):
        self.string[0] = self.string[0].upper()
    
    def __getLengthOfLettersAndString(self):
        letterAmount = len(self.letters)
        stringAmount = len(self.string)
        
        return letterAmount, stringAmount

    def __startCapin(self, lettes, string):
        for x in range(1, string):
            if self.string[x] not in self.letters:
                self.string[x] =  self.string[x][0].upper() + self.string[x][1:]
    
    def titleCreator(self):
        if self.letters:        
            letterAmount, stringAmount = \
                self.__getLengthOfLettersAndString()
            self.__capFirstLetter();
            self.__startCapin(letterAmount, stringAmount)
        return ' '.join(self.string)
   
