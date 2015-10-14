class item(object):
	def __init__(self, name, price):
		self.name = name
		self.price = price 
		self.redPencilStatus = False

	def changeRedPencilStatus(self):
		self.redPencilStatus = True