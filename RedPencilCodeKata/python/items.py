from datetime import timedelta, date , datetime


class item(object):
	def __init__(self, name, price, date= None):
		self.name = name
		self.price = price 
		self.dateOfLastPriceChange = date  
		self.redPencilStatus = False
		self.setDate()

	def changeRedPencilStatus(self):
		self.redPencilStatus = True

	def setDate(self):
		if self.dateOfLastPriceChange == None:
			self.dateOfLastPriceChange = str(date.today())

   	def updateDate(self):
   		self.dateOfLastPriceChange = str(date.today())

   	def getStablePriceDays(self): 
   		date_object = datetime.strptime( self.dateOfLastPriceChange,'%Y-%m-%d')
   		d0 = date_object 
   		d1 = datetime.now() 
   		delta = d1 - d0
   		return delta.days

   	def hadStablePriceFor30Days(self):
   		days = self.getStablePriceDays()
   		if days >= 30: 
   			return True 
   		else:
   			return False