class Solution:
	def get_val(self,ar,row,col,length,height) -> int:
		if row < 0 or row >= length or col < 0 or col >= height:
			return 0
		return ar[row][col]
	def find_max_block(self,ar,row,col,length,height,size,cntarr,maxsize):
		if row >= length or col >= height:
			return
		cntarr[row][col] = True
		size +=1
		if size > maxsize:
			maxsize = size
		direction = [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]
		for i in range(len(direction)):
			new_row = row + direction[i][0]
			new_col = col + direction[i][1]
			val = self.get_val(ar,new_row,new_col,length,height)
			if val > 0 and cntarr[new_row][new_col] == False:
				self.find_max_block(ar,new_row,new_col,length,height,size,cntarr,maxsize)
		cntarr[row][col] = False
	def get_length_connection(self,ar,length,height) -> int:
		maxsize = -1000000
		size = 0
		cntarr = [[False for j in range(length)] for i in range(height)]
		for i in range(length):
			for j in range(height):
				if ar[i][j] == 1:
					self.find_max_block(ar,i,j,length,height,size,cntarr,maxsize)
		return maxsize

if __name__ == "__main__":
	solution = Solution()
	ar = [[1,1,0,0,0],[0,1,1,0,1],[0,0,0,1,1],[1,0,0,1,1],[0,1,0,1,1]]
	print(solution.get_length_connection(ar,5,5))

