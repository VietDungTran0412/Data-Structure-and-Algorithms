from Heap import MinHeap
class Solution:
    def __repr__(self) -> str:
        nums = [[1,3,7,10,15],[4,5,12,17,18],[6,8,11,16,19]]
    def mergeArrays(self,nums: list[list[int]]):
        n = len(nums[0])
        heap = MinHeap(len(nums))
        res = []
        for i in range(len(nums)):
            heap.insert(nums[i])
        
