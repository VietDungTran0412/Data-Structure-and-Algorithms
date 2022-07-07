from Queue import LinkedQueue
class Solution:
    def printSolution(self):
        nums = [11,12,13,14,15,16,17,18,19,20]
        q = LinkedQueue()
        for num in nums:
            q.enQueue(num)
        self.interleavingQueue(q)
        self.interleavingArray(nums)
        print(nums)
        print(q)
    def interleavingQueue(self,nums: LinkedQueue)->LinkedQueue:
        if nums.size()%2 != 0: return
        halfSize = nums.size()//2
        stack = []
        for i in range(halfSize):
            stack.append(nums.deQueue())
        while len(stack) != 0:
            nums.enQueue(stack.pop())
        for j in range(halfSize):
            nums.enQueue(nums.deQueue())
        for k in range(halfSize):
            stack.append(nums.deQueue())
        while len(stack)!=0:
            nums.enQueue(stack.pop())
            nums.enQueue(nums.deQueue())

        
    def interleavingArray(self,nums: list)->list:
        if len(nums) % 2 != 0:
            return
        stack =[]
        halfSize = len(nums)//2
        while len(nums) != 0:
            stack.append(nums.pop())
        for i in range(halfSize):
            nums.append(stack[len(stack)-i-1])
            nums.append(stack[halfSize-1-i])
        
        
if __name__ == "__main__":
    Solution().printSolution()
        
