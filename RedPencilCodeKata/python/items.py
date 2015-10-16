from datetime import timedelta, date

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
			self.dateOfLastPriceChange = date.today()

   	def updateDate(self):
   		self.dateOfLastPriceChange = date.today()