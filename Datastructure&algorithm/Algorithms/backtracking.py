global N
N = 4
def printSolution(board):
	for i in range(N):
		for j in range(N):
			print(board[i][j],end = " ")
		print("")

# A utility function to check if a queen can
# be placed on board[row][col]. Note that this
# function is called when "col" queens are
# already placed in columns from 0 to col -1.
# So we need to check only left side for
# attacking queens

def isSAfe(board,row,col):
	for i in range(col):
		if board[row][i] == 1:
			return False
	#Check the upper left diagonal
	for i,j in zip(range(row,-1,-1),range(col,-1,-1)):
		if board[i][j] == 1:
			return  False
	#Check the lower left diagonal
	for i,j in zip(range(row,N,1), range(col,-1,-1)):
		if board[i][j] == 1:
			return False

	return True

def solveNQUtil(board,col):
	if col >= N:
		return True
	for i in range(N):
		if isSAfe(board,i,col):
			board[i][col] =1
			if solveNQUtil(board,col+1) == True:
				return True
			else:
				# If placing queen in board[i][col
            	# doesn't lead to a solution, then
            	# queen from board[i][col]
				board[i][col] = 0
	#If the queen can't be placed in any row
	#in this col then return False
	return False
	

def solution():
	board = [ [0,0,0,0],
			  [0,0,0,0],
			  [0,0,0,0],
			  [0,0,0,0] ]
	if solveNQUtil(board,0) == False:
		print("Solution does not exist")
		return False
	else:
		printSolution(board)
		return True
solution()
