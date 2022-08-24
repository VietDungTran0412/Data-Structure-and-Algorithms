from Heap import MinHeap,MaxHeap

class Solution:
    def __repr__(self) -> str:
        heap = MinHeap(15)
        nums = [6,2,10,12,20,25,23,7,14,19]
        for num in nums:
            heap.insert(num)
        print(heap.ar)
        self.deleteAtIndex(heap,5)
        newAr = []
        for i in range(len(nums)):
            newAr.append(heap.delete())
        print(newAr)
        return str(heap.ar)
    def deleteAtIndex(self,heap: MaxHeap,pos):
        if pos >= heap.length:
            return -1
        last = heap.length - 1
        heap.ar[pos], heap.ar[last] = heap.ar[last], heap.ar[pos]
        heap.length -=1
        temp = heap.ar[last]
        heap.ar[last] = None
        heap.percolateDown(pos)
        return temp
print(Solution())