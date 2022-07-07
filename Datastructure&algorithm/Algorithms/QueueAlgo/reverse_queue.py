from Queue import LinkedQueue
from stack import DynamicStack
class Solution:
    def printSolution(self):
        ar = [1,2,3,4,5,6]
        q = LinkedQueue()
        for num in ar:
            q.enQueue(num)
        self.reverseQueue(q)
        print(q)
    def reverseQueue(self,queue: LinkedQueue):
        if queue.isEmpty():
            return 
        stack = DynamicStack()
        for i in range(queue.size()):
            temp = queue.deQueue()
            stack.push(temp)
        for j in range(stack.size()):
            temp = stack.pop()
            queue.enQueue(temp)
        
Solution().printSolution()