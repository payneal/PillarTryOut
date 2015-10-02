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
		if bedTime == None: 
			self.bed = None
		else: 
			self.bed['hour'], self.bed['meridiem'] = self.getAMorPMfromTimeString(bedTime)

	def checkValidStartAndLeave(self): 
		if self.start['hour'] < 5:
			raise Exception("Baby sitting starts no earlier than 5:00PM") 
		elif self.leave['hour'] > 4 and self.leave['hour'] != 12 and self.leave['meridiem'] == "AM" : 
			 raise Exception("Baby sitting ends no later than 4:00AM") 

	def calculateTotalHours(self): 
		if self.leave['hour'] >  self.start['hour']: 
			return self.leave['hour'] - self.start['hour']
		else: 
			return (12 + self.leave['hour']) - self.start['hour']

	def calculatePay(self, startTime, leaveTime, bedTime= None): 
		self.setBabysittingTimes(startTime, leaveTime, bedTime) 
		
		current = self.start
		pay = 0

		for x in range( self.calculateTotalHours()):
			if current['hour'] == 12 or current['hour'] < 5:
				pay +=  self.midnightPay
				if current['hour'] == 12: 
					current['hour'] = 1 
					current['meridiem'] = "AM"
				else: 
					current['hour'] += 1
			elif self.bed == None or current['hour'] < self.bed['hour'] and current['hour'] < 12:
				pay += self.startToBedPay
				current['hour'] += 1
			
			elif current['hour'] >= self.bed['hour'] and current['hour'] < 12:
				pay += self.bedToMidnightPay 	
				current['hour'] += 1	
		return pay




