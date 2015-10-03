#start empty
class Sitter(object):
	def __init__ (self):	
		self.startToBedPay = 12
		self.bedToMidnightPay = 8 
		self.midnightPay = 16

		self.babySitterStartsNoEarlierThan = {'hour': 5, 'min': 0, "meridiem":"PM"}
		self.babySitterLeavesNoEarlierThan = {'hour': 4, 'min': 0, "meridiem":"AM"}
		self.midnight = {'hour': 12, 'min': 0, "meridiem":"AM"}

		self.secondsInHr = 60 
		
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
		if self.start['hour'] < self.babySitterStartsNoEarlierThan['hour']:
			raise Exception("Baby sitting starts no earlier than 5:00PM") 
		elif self.leave['hour'] > self.babySitterLeavesNoEarlierThan['hour'] and self.leave['hour'] != self.midnight['hour'] and self.leave['meridiem'] == "AM" : 
			 raise Exception("Baby sitting ends no later than 4:00AM") 

	def calculateTotalHours(self): 
		hours = self.dealWithHrsInRegardToTotalHours() 
		return self.dealWithMinsInRegardToTotalHours(hours)

	def dealWithHrsInRegardToTotalHours(self):
		hours= 0  
		if self.leave['hour'] >  self.start['hour']: 
			hours = self.leave['hour'] - self.start['hour']
		else: 
			hours = (self.midnight['hour'] + self.leave['hour']) - self.start['hour']
		return hours

	def dealWithMinsInRegardToTotalHours(self, hours): 
		if (self.start['min'] + self.leave['min']) % self.secondsInHr != 0 and self.start['min'] > self.leave['min']: 
			hours -=1
		
		if self.bed != None: 
		 	if (self.start['min'] + self.bed['min']) % self.secondsInHr != 0 and self.leave['min'] < self.bed['min']: 
				hours -=1 
		return hours

	def addMidnightPayAmount(self, pay, current): 
		pay +=  self.midnightPay
		if current['hour'] == self.midnight['hour']: 
			current['hour'] = 1 
			current['meridiem'] = "AM"
		else: 
			current['hour'] += 1	
		return pay, current

	def addBed2MidnightPayAmount(self, pay, current): 
		if self.bed['min'] > 0 and current['hour'] == self.midnight['hour'] -1 :
			current['hour'] += 1
		else:
			pay += self.bedToMidnightPay 	
			current['hour'] += 1	
		return pay, current

	def addStart2BedPayAmount(self, pay, current): 
		pay += self.startToBedPay
		current['hour'] += 1
		return pay, current

	def addStart2BedPayAmountOrBed2MidnightPayAmount(self, pay, current): 
		if self.start['min'] + self.bed['min'] >= self.secondsInHr: 
			pay += self.startToBedPay
		elif self.bed['min'] > 0 and current['hour'] == self.midnight['hour'] -1:
			current['hour'] += 1
		else:
			pay += self.bedToMidnightPay 
		current['hour'] += 1
		return pay, current

	def calculatePay(self, startTime, leaveTime, bedTime= None): 
		self.setBabysittingTimes(startTime, leaveTime, bedTime) 

		current = self.start
		pay = 0
		for x in range( self.calculateTotalHours()):
			if current['hour'] == self.midnight['hour'] or current['hour'] < self.babySitterStartsNoEarlierThan['hour']:
				pay, current = self.addMidnightPayAmount(pay, current)	
			elif self.bed == None or current['hour'] < self.bed['hour'] and current['hour'] < self.midnight['hour']:
				pay, current = self.addStart2BedPayAmount(pay, current)
			elif current['hour'] == self.bed['hour']: 
				pay, current = self.addStart2BedPayAmountOrBed2MidnightPayAmount(pay, current)
			elif current['hour'] > self.bed['hour'] and current['hour'] < self.midnight['hour']:
				pay, current = self.addBed2MidnightPayAmount(pay, current)		
		return pay




