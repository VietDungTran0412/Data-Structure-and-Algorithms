from Queue import LinkedQueue
class Solution:
    def printSolution(self):
        nums = [10,20,30,40,50,60,70,80,90]
        q = LinkedQueue()
        for num in nums:
            q.enQueue(num)
        self.reverseQueueKElements(q,2)
        print(q)
    def reverseQueueKElements(self,nums: LinkedQueue,k: int)->None:
        if nums is None or k > nums.size(): return
        stack = []
        for i in range(k):
            stack.append(nums.deQueue())
        while len(stack) != 0:
            nums.enQueue(stack.pop())
        for j in range(nums.size()-k):
            nums.enQueue(nums.deQueue())
    
Solution().printSolution()