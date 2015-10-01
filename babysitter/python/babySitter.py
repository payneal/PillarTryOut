#start empty
class Sitter(object):
	def __init__ (self):	
		self.startToBedPay = 12
		self.bedToMidnightPay = 8 
		self.midnightPay = 16

	def calculatePay(self, startTime, leaveTime, bedTime): 
		if startTime < 5: 
			raise Exception("Baby sitting starts no earlier than 5:00PM") 
		elif startTime == 12:
			return ((12+leaveTime) - startTime) * self.midnightPay
		elif startTime != bedTime:
			pay = self.startToBedPay * (leaveTime - startTime)
		else:
			pay = self.bedToMidnightPay * (leaveTime - startTime)

		return pay 


