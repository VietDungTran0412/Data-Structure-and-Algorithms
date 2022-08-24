from Heap import MinHeap, MaxHeap

class Solution:
    def __repr__(self) -> str:
        nums = [5,2,10,7,8,12,18,19,20]
        return str(self.kThSmallestElementsNaive(nums,6))
    def kThSmallestElementsNaive(self,nums: list[int], k)->list[int]:
        lenght = len(nums)
        heap = MaxHeap(lenght)
        res = []
        
        for i in range(lenght):
            heap.insert(nums[i]) # log(k)
            if heap.length > k:
                heap.delete()    # log(k) by removing elements from heap of size k
        return heap.ar[:k]
    def kThSmallestElements(self,nums:list[int],k:int)->list[int]:
        length = len(nums)
        heap = MinHeap(length)
        heap.convertArToHeap(nums)
        res = []
        for i in range(k):
            res.append(heap.delete())
        return res
print(Solution())