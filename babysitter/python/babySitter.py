#start empty
class Sitter(object):
	def __init__ (self):	
		self.startToBedPay = 12
		self.bedToMidnightPay = 8 
		self.midnightPay = 16
	
		self.start = {'hour': None, "meridiem": None}
		self.leave = {'hour': None, "meridiem": None}
		self.bed = {'hour': None, "meridiem": None}

	def getAMorPMfromTimeString(self, timeString):
		amOrPM = None
		if "AM" in timeString:
			amOrPM = "AM"
			return  self.getTimeFromString("AM", timeString), amOrPM
		else:
			amOrPM = "PM"
			return  self.getTimeFromString("PM", timeString), amOrPM
		
	def getTimeFromString(self, meridiem, timeString): 
		return int(timeString.replace(meridiem, ""))

	def setBabysittingTimes(self, startTime, leaveTime, bedTime): 
		self.start['hour'], self.start['meridiem'] = self.getAMorPMfromTimeString(startTime)
		self.leave['hour'], self.leave['meridiem'] = self.getAMorPMfromTimeString(leaveTime)
		self.checkValidStartAndLeave()
		self.bed['hour'], self.bed['meridiem'] = self.getAMorPMfromTimeString(bedTime)

	def checkValidStartAndLeave(self): 
		if self.start['hour'] < 5:
			raise Exception("Baby sitting starts no earlier than 5:00PM") 
		elif self.leave['hour'] > 4 and self.leave['hour'] != 12 and self.leave['meridiem'] == "AM" : 
			 raise Exception("Baby sitting ends no later than 4:00AM") 

	def calculatePay(self, startTime, leaveTime, bedTime): 
		self.setBabysittingTimes(startTime, leaveTime, bedTime) 
		
		if self.start['hour']  == 12:
			pay =  ((12 + self.leave['hour'] ) - self.start['hour']) * self.midnightPay
		elif self.start['hour'] != self.bed['hour']:
			
			if self.leave['meridiem'] == 'AM' and self.bed['meridiem'] == 'AM': 
				pay = 20
			else: 
				pay = self.startToBedPay * (self.leave['hour'] - self.start['hour'])
		else:
			pay = self.bedToMidnightPay * (self.leave['hour'] - self.start['hour'])

		return pay 







