#start empty
class Sitter(object):
	def __init__ (self):	
		self.startToBedPay = 12
		self.bedToMidnightPay = 8 

	def calculatePay(self, startTime, leaveTime, bedTime): 
		if startTime != bedTime:
			pay = self.startToBedPay * (leaveTime - startTime)
		else:
			pay = self.bedToMidnightPay * (leaveTime - startTime)

		return pay 


