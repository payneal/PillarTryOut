from datetime import timedelta, date , datetime

class item(object):
	def __init__(self, name, price, date= None):
		self.name = name
		self.price = price 
		self.dateOfLastPriceChange = date  
		self.redPencilStatus = False
		self.setDateForToday()
		self.daysPriceCanBeOnRedPencil = 30

	def changeRedPencilStatus(self):
		self.redPencilStatus = True

	def getRedPencilStatus(self, futureDate=None):
		if futureDate: 
			days = self.getStablePriceDays(futureDate)
   			if days <= self.daysPriceCanBeOnRedPencil:
   				return True 
   			else:
   				return False
		else:
			return self.redPencilStatus


	def setDateForToday(self):
		if self.dateOfLastPriceChange == None:
			self.dateOfLastPriceChange = str(date.today())

   	def updateDateToToday(self):
   		self.dateOfLastPriceChange = str(date.today())

   	def getStablePriceDays(self,futureDate= None): 
   		if futureDate:
   			date_object = datetime.strptime( futureDate,'%Y-%m-%d')
   			d1 = date_object 
   		else: 
   			d1 = datetime.now() 

   		date_object = datetime.strptime( self.dateOfLastPriceChange,'%Y-%m-%d')
   		d0 = date_object 
   		
   		delta = d1 - d0
   		return delta.days

   	def hadStablePriceFor30Days(self):
   		days = self.getStablePriceDays()
   		if days >= self.daysPriceCanBeOnRedPencil: 
   			return True 
   		else:
   			return False

   	







