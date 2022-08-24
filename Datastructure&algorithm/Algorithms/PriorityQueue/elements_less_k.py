from Heap import MinHeap,MaxHeap

class Solution:
    def __repr__(self) -> str:
        heap = MaxHeap(10)
        nums = [6,2,8,10,15,11,7,1,4]
        heap.convertArToHeap(nums)
        return str(self.elementsLessThanK(heap,10,0))
    def elementsLessThanK(self,heap: MaxHeap,k: int, i: int)->list[int]:
        if heap.length == 0 or i >= heap.length:
            return []
        elements = []
        if heap.ar[i] < k:
            elements.append(heap.ar[i])
        left = 2*i+1
        right = 2*i+2
        elements += self.elementsLessThanK(heap,k,left)
        elements += self.elementsLessThanK(heap,k,right)
        return elements

print(Solution())