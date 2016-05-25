import unittest
from matrix import Matrix

class TestMatrix(unittest.TestCase):
	def setUp(self):
		self.matrix = Matrix()

	def test_simple_Input(self): 
		self.matrix.rowOfMatrix(4)
		self.matrix.columnOfMatrix(4)

		self.matrix.storeMatrix(1,1,0,0)
		self.matrix.storeMatrix(0,1,1,0)
		self.matrix.storeMatrix(0,0,1,0)
		self.matrix.storeMatrix(1,0,0,0)

		score = self.matrix.score()
		self.assertEqual(score, 5)
	# Sample Input:
# 4
# 4
# 1 1 0 0
# 0 1 1 0
# 0 0 1 0
# 1 0 0 0

# Sample Output:
# 5

if __name__ == '__main__':
    unittest.main()