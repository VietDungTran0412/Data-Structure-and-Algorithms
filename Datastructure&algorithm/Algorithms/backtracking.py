class Solution:
	def printSolution(self):
		grid = [[0 for i in range(9)] for i in range(9)]
		if self.sudokuSolver(grid):
			for i in range(9):
				print(grid[i])
		else:
			print("No Solution Exists!!!")
	def sudokuSolver(self,grid):
		cell = [0,0]
		if self.findEmptySquare(grid,cell):
			return True
		row = cell[0]
		col = cell[1]
		for num in range(1,10):
			if self.isSafe(grid,row,col,num):
				grid[row][col] = num
				if self.sudokuSolver(grid):
					return True
				grid[row][col] = 0
		return False
	def findEmptySquare(self,grid,cell):
		for i in range(9):
			for j in range(9):
				if grid[i][j] == 0:
					cell[0] = i
					cell[1] = j
					return False
		return True
	def isColumnSafe(self,grid,col,num):
		for row in range(9):
			if grid[row][col] == num:
				return False
		return True
	def isRowSafe(self,grid,row,num):
		for col in range(9):
			if grid[row][col] == num:
				return False
		return True
	def isBoxSafe(self,grid,row,col,num):
		for i in range(3):
			for j in range(3):
				if grid[row+i][col+j] == num:
					return False
		return True
	def isSafe(self,grid,row,col,num):
		checkCol = self.isColumnSafe(grid,col,num)
		checkRow = self.isRowSafe(grid,row,num)
		checkBox = self.isBoxSafe(grid,row - row%3, col - col%3,num)
		if checkCol and checkRow and checkBox:
			return True
		return False

if __name__ == "__main__":
	Solution().printSolution()