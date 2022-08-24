from Heap import MaxHeap
class Solution:
    def __repr__(self) -> str:
        nums = [5,2,7,10,15,3,8,6,5]
        self.heapSort(nums)
        return str(nums)
    def heapSort(self,nums):
        heap = MaxHeap(len(nums))
        for i in range(len(nums)):
            heap.insert(nums[i])
        for j in range(len(nums)):
            nums[j] = heap.delete()
        
print(Solution())