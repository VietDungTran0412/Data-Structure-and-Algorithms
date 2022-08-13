import heapq
class SoldierInfo:
    def __init__(self,row,numSoldiers) -> None:
        self.row = row
        self.count = numSoldiers
class Solution:
    def __init__(self,nums) -> None:
        self.ar = nums
    def _parent(self,pos,nums):
        if pos % 2 ==1: return pos//2
        return pos//2-1
    def _swap(self,pos1,pos2,nums):
        nums[pos1], nums[pos2] = nums[pos2], nums[pos1] 
    def _minHeapify(self,soldiers,pos):
        if pos == 0:
            return
        parent = self._parent(pos,soldiers)
        if soldiers[pos].count < soldiers[parent].count:
            self._swap(pos,parent)
            self._minHeapify(parent)
        else:
            if soldiers[pos].row < soldiers[parent].row:
                self._swap(pos,parent)
                self._minHeapify(parent) 

        
    def kWeekestRows(self,mat: list[list[int]], k : int)->list:
        soldiers = []
        for i in range(len(mat)):
            count  = 0
            for j in range(len(mat[i])):
                if mat[i][j] == 1:
                    count +=1
            soldiers.append(SoldierInfo(i,count))
        
