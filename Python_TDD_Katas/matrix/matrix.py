#start empty
class Matrix(object):
	def __init__ (self):
		self.row = None
		self.column = None
		self.theMatrix = []

	def rowOfMatrix(self,number):
		self.row = number

	def columnOfMatrix(self,column):
		self.column = column

	def storeMatrix(self,a,b,c,d):
		x = [a,b,c,d]
		self.theMatrix.append(x) 

	def score(self): 
		
		#LOOOKS LIKE THIS
		'''
		[1, 1, 0, 0]
		[0, 1, 1, 0]
		[0, 0, 1, 0]
		[1, 0, 0, 0]
		'''

		#TURN IT TO ONE LIST
		#1 1 0 0 0 1 1 0 0 0 1 0 1 0 0 0

		#START AT POSITION 0 
		#'1' 1 0 0 0 1 1 0 0 0 1 0 1 0 0 0

		#CHECK ALL FOUR SPOTS 
		'''
		[1, "1", 0, 0]
		["0", "1", 1, 0]
		[0, 0, 1, 0]
		[1, 0, 0, 0]
		'''

		# {longestStreakStart:"0,0", total:2 {'paths':{1:[] }, {2: } } }



