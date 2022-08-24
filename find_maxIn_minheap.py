from Heap import MinHeap
import math
class Solution:
    def __repr__(self) -> str:
        nums = [5,2,9,12,18,6,2,1,60]
        heap = MinHeap(len(nums))
        for num in nums:
            heap.insert(num)
        return str(self.findMaxInMinHeap(heap))
    def findMaxInMinHeap(self, heap: MinHeap):
        i = (heap.length + 1)//2
        maxVal = -math.inf
        while i < heap.length:
            maxVal = max(heap.ar[i],maxVal)
            i+=1
        return maxVal
print(Solution())
