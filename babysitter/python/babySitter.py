#start empty
class Sitter(object):
	def __init__ (self):	
		self.startToBedPay = 12
		self.bedToMidnightPay = 8 
		self.midnightPay = 16
	
		self.start = {'hour': None, 'min': None, "meridiem": None}
		self.leave = {'hour': None, 'min': None, "meridiem": None}
		self.bed = {'hour': None, 'min': None, "meridiem": None}

	def getAMorPMfromTimeString(self, timeString):
		amOrPM = None
		if "AM" in timeString:
			amOrPM = "AM"
			hour, minutes =  self.getTimeFromString("AM", timeString)
		else:
			amOrPM = "PM" 
			hour, minutes = self.getTimeFromString("PM", timeString)
		return hour, minutes, amOrPM
		
	def getTimeFromString(self, meridiem, timeString): 
		timeString = timeString.replace(meridiem, "")
		if ":" in timeString:
			 timeList= timeString.split(':')
			 return int(timeList[0]), int(timeList[1])
		else:	
			return int(timeString), 0

	def setBabysittingTimes(self, startTime, leaveTime, bedTime): 
		self.start['hour'], self.start['min'], self.start['meridiem'] = self.getAMorPMfromTimeString(startTime)
		self.leave['hour'], self.leave['min'], self.leave['meridiem'] = self.getAMorPMfromTimeString(leaveTime)
		self.checkValidStartAndLeave()
		if bedTime == None: 
			self.bed = None
		else: 
			self.bed['hour'], self.bed['min'], self.bed['meridiem'] = self.getAMorPMfromTimeString(bedTime)

	def checkValidStartAndLeave(self): 
		if self.start['hour'] < 5:
			raise Exception("Baby sitting starts no earlier than 5:00PM") 
		elif self.leave['hour'] > 4 and self.leave['hour'] != 12 and self.leave['meridiem'] == "AM" : 
			 raise Exception("Baby sitting ends no later than 4:00AM") 

	def calculateTotalHours(self): 
		if self.leave['hour'] >  self.start['hour']: 
			hours = self.leave['hour'] - self.start['hour']
		else: 
			hours = (12 + self.leave['hour']) - self.start['hour']

		if (self.start['min'] + self.leave['min']) % 60 != 0 and self.start['min'] > self.leave['min']: 
			hours -=1

		return hours 

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



