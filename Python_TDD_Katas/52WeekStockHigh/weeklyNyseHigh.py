import json
import requests
from bs4 import BeautifulSoup
import datetime

class StockDaily52:
    
    def __init__(self, year, month, day):
        self.__checkIfEntryValid(year, month, day)
        self.url = 'http://online.wsj.com/mdc/public/page/2_3021-newhinyse-newhighs-{}{}{}.html?mod=mdc_pastcalendar'.\
                format(str(year), str(month), str(day)) 
        self.year = year
        self.month = month
        self.day = day
        self.highs = None
        self.lows = None
        self.stockData = None
        self.__getStockData()

    def __checkIfEntryValid(self, year, month, day):
        entries = [year, month, day]
        self.__invalidInputNotANumber(entries)
        requestDate = datetime.date(int(year), int(month), int(day)) 
        self.__invalidRequestDate(requestDate)
        
    def __invalidInputNotANumber(self, entries):
        for x in entries:
            if x.isdigit() == False:
                raise Exception('invalid entry')

    def __invalidRequestDate(self, requestDate):
        if requestDate > datetime.date.today():
            raise Exception("No information for future dates") 
        if requestDate < datetime.date(2007, 5, 1):
            raise Exception("No data prior to 2007 May 1st")
        weekday = datetime.datetime(requestDate.year, \
            requestDate.month, requestDate.day)
        if weekday.weekday() > 4:
            raise Exception("this is not weekday")

    def __getStockData(self):
        r = requests.get(self.url)
        soup = BeautifulSoup(r.content, "html.parser")
        stockInfo= soup.find_all('td', {'class': ['text', 'num','nnum' ,'pnum']})
        self.__setLowAndHigh(stockInfo)
        self.stockData = stockInfo

    def __setLowAndHigh(self, stockInfo):
        self.highs = int(stockInfo[0].text.split(':')[1]) 
        self.lows = int(stockInfo[(self.highs*6)+1].text.split(':')[1])
    
    def __cleanStringOfStockNameAndSymbol(self, itemNum):
        entry = self.stockData[itemNum].text.replace('\n', ' ').\
            replace('\r', '').replace('\t', '').replace('\v', '').replace('\f', '')
        entry = entry.rstrip().lstrip().strip()
        entry = entry.rsplit('(', 1)
        stockName = entry[0][:-1]
        stockSymbol = entry[1][:-1]
        stockName, stockSymbol = self.__doubleChecktheSymbol(stockName, stockSymbol)
        return stockName, stockSymbol

    def __doubleChecktheSymbol(self, stockName, stockSymbol):
        if ')' in stockSymbol:
            stockSymbol = stockSymbol.rsplit(')')[0]
            stockName = stockName[:-1]
        if '@' in stockSymbol:
            stockSymbol = stockSymbol.rsplit('@')[0]
        return stockName, stockSymbol

    def __getStockNameAndSymbol(self, itemNum, data):
        stockName, stockSymbol = self.__cleanStringOfStockNameAndSymbol(itemNum)
        data[stockSymbol] = {}
        data[stockSymbol]['name']= stockName
        data[stockSymbol]['webGraph'] = 'http://quotes.wsj.com/{}'.format(stockSymbol)
        return  stockSymbol

    def __getStockStatistics(self, info, count, symbol, data):
        if count%6 == 2: 
            data[symbol]['52weekHigh'] = float(info)
        if count%6 == 3:
            if  info[0] == '$':
                 info = info[1:]
            data[symbol]['price'] = float(info)
        if count%6  == 4:
            data[symbol]['changeAmount'] = float(info)
        if count%6 == 5:
            data[symbol]['changePrecent'] = float(info)
        if count%6 == 0: 
            data[symbol]['volume'] = int(info.replace(',', ''))

    def __determineWhatToDoWithStockInfo(self, count, data, stockSymbol):
        if count%6 == 1:
            stockSymbol = self.__getStockNameAndSymbol(count, data)
        else:
            info = self.stockData[count].text
            self.__getStockStatistics(info, count, stockSymbol, data)
        return stockSymbol

    def stockHighs(self):
        data = {}
        stockSymbol = None
        for count in range(1, (self.highs*6+1)):  
            stockSymbol = self.__determineWhatToDoWithStockInfo(count, data, stockSymbol)
        return json.dumps([ {'{}{}{}'.format(self.year, self.month, self.day) : data }])
