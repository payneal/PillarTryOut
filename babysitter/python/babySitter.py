#start empty
class Sitter(object):
	def __init__ (self):	
		self.startToBedPay = 12
		self.bedToMidnightPay = 8 
		self.midnightPay = 16

	def calculatePay(self, startTime, leaveTime, bedTime): 
		if startTime == 12:
			return midnightPay
		elif startTime != bedTime:
			pay = self.startToBedPay * (leaveTime - startTime)
		else:
			pay = self.bedToMidnightPay * (leaveTime - startTime)

		return pay 


