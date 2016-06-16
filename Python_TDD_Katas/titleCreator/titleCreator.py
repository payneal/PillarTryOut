# Class

class TitleCreator:


    def __init__(self, string, lettersToCap=[]):
        self.string = None
        self.caped = []
        self.__setUp(string, lettersToCap)

    def __setUp(self, string, lettersToCap):
        if string != '':
            self.string = string.lower().split(" ")
        if len(lettersToCap) > 0:
            self.caped = lettersToCap.lower().split(" ")

    def __capFirstLetter(self):
        self.string[0] = self.string[0][0].upper() + self.string[0][1:]
    
    def __startCapin(self):
        for x in range(1, len(self.string)):
            if self.string[x] not in self.caped:
                self.string[x] =  self.string[x][0].upper() + self.string[x][1:]

    def titleCreator(self):
        if self.string:
            self.__capFirstLetter()
            self.__startCapin() 
            return ' '.join(self.string)
        return ''
