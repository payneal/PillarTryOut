
# coins that vending machine can accept
class coins(object):  
	def __init__(self): 
		#self.validCoins= {"nickle":.05, 'dime': .10, 'quarter': .25} 
		self.allCoins={'penny': .01, 'nickle': .05, 'dime': .10, 'quarter': .25, 'half': .50, 'dollar': 1.00}

	def getAmount(self, name): 
		if name in self.allCoins: 		
			return self.allCoins[name]
		else: 
			return None