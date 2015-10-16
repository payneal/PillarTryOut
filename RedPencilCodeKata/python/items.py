import time

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
			self.dateOfLastPriceChange = time.strftime('%m-%d-%y')

   	def updateDate(self):
   		self.dateOfLastPriceChange = time.strftime('%m-%d-%y')