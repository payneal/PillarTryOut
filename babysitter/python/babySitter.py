#start empty
class Sitter(object):
	def __init__ (self):	
		self.startToBedPay = 12
		self.bedToMidnightPay = 8 
		self.midnightPay = 16

	def calculatePay(self, startTime, leaveTime, bedTime): 

		amOrPMStart = None
		if "AM" in startTime: 
			amOrPMStart = "AM"
			startTime = startTime.replace("AM", "")
		else:
			amOrPMStart = "PM"
			startTime = startTime.replace("PM", "")
		
		startTime = int(startTime)

		amOrPMLeave = None
		if "AM" in leaveTime: 
			amOrPMLeave = "AM"
			leaveTime = leaveTime.replace("AM", "")
		else:
			amOrPMLeave = "PM"
			leaveTime =  leaveTime.replace("PM", "")
		
		leaveTime = int(leaveTime)

		bedTime = bedTime.replace("PM", "")
		bedTime = int(bedTime)
		

		if startTime < 5:
			raise Exception("Baby sitting starts no earlier than 5:00PM") 
		elif leaveTime > 4 and leaveTime != 12 and amOrPMLeave == "AM" : 
			 raise Exception("Baby sitting ends no later than 4:00AM") 
		elif startTime == 12:
			return ((12+leaveTime) - startTime) * self.midnightPay
		elif startTime != bedTime:
			pay = self.startToBedPay * (leaveTime - startTime)
		else:
			pay = self.bedToMidnightPay * (leaveTime - startTime)

		return pay 


