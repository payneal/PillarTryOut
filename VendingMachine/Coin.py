
# coins that vending machine can accept
class coins(object):  
	def __init__(self, amount): 
		self.amount = float(amount)
		#hold all money in one dic
		self.validCoins= [.05, .10, .25] 

	def getAmount(self): 
		return self.amount

	def check(self):
		if self.amount in self.validCoins:
			return self.amount
		else: 
			return False

	 

