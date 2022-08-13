from heapq import heapify
from heapq import heappush
from heapq import heappop
class Heap:
    def _parent(self,pos):
        if pos % 2  == 0: return pos//2-1
        return pos//2
    def _swap(self,pos1,pos2,nums):
        nums[pos1], nums[pos2] = nums[pos2], nums[pos1]
    def minHeapify(self,pos,nums):
        if pos == 0:
            return
        parent = self._parent(pos)
        if nums[parent] >= nums[pos]:
            self._swap(pos,parent,nums)
            self.minHeapify(parent,nums)
    def _leftChild(self,pos):
        return pos*2+1
    def _rightChild(self,pos):
        return (pos+1)*2
    def _isLeaf(self,pos,nums):
        return self._leftChild(pos) >= len(nums) or self._rightChild(pos) >=len(nums)
    def heappop(self,nums):
        if len(nums) == 0:
            return 
        temp = nums[0]
        self._swap(0,len(nums)-1,nums)
        nums.pop()
        i = 0
        while not self._isLeaf(i,nums):
            left = self._leftChild(i)
            right = self._rightChild(i)
            if not self._isLeaf(left,nums) and not self._isLeaf(right,nums):
                if nums[i] > nums[left] and nums[i] > nums[right]:
                    if nums[left] > nums[right]:
                        self._swap(i,right,nums)
                        i = right
                    elif nums[right] > nums[left]:
                        self._swap(i,left,nums)
                        i = left
                elif nums[i] > nums[left] or nums[i] > nums[right]:
                    if nums[i] > nums[left]:
                        self._swap(i,left,nums)
                        i = left
                    elif nums[i] > nums[right]:
                        self._swap(i,right,nums)
                        i = right
                elif nums[i] < nums[left] and nums[i] < nums[right]:
                    return temp
            elif not self._isLeaf(left,nums) or not self._isLeaf(right,nums):
                if not self._isLeaf(left,nums):
                    if nums[i] > nums[left]:
                        self._swap(i,left,nums)
                        i = left
                    else:
                        return temp
                elif not self._isLeaf(right,nums):
                    if nums[i] > nums[right]:
                        self._swap(i,right,nums)
                        i = right
                    else:
                        return temp
        return temp
 
l = [5,7,9,1,3,8]
heap = Heap()
for i in range(len(l)-1,-1,-1):
    heap.minHeapify(i,l)
ar = []
for j in range(len(l)):
    temp = heap.heappop(l)
    ar.append(temp)
print(ar)