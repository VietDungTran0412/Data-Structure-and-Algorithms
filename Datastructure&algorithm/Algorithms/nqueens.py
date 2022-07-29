class Solution:
    def __repr__(self) -> str:
        return str(self.solve())
    def solve(self):
        grid = [[0,0,0,0] for i in range(4)]
        if self.solveUtil(grid,0,0):
            return grid
        else:
            return "No Solution!"
    def isSafe(self,grid,row,col,num):
        for i in range(col):
            if grid[row][i] == num:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if grid[i][j] == 1:
                return False
    
        # Check lower diagonal on left side
        for i, j in zip(range(row, 4, 1), range(col, -1, -1)):
            if grid[i][j] == 1:
                return False
    
        return True
        
    def solveUtil(self,grid,row,col):
        if col >=4:
            return True
        for i in range(4):
            if self.isSafe(grid,i,col,1):
                grid[i][col] = 1
                if self.solveUtil(grid,i,col+1):
                    return True
                grid[i][col] = 0

        return False
print(Solution())