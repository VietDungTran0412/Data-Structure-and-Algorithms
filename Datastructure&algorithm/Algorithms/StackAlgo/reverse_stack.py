from stack import DynamicStack
class Solution:
    def printSolution(self):
        stack = DynamicStack()
        stack.insert([1,2,3,4,5,6,7,8])
        stack = self.insertAtBottom(stack,10)
        stack = self.reversedStack(stack)
        stack.print()
    def reversedStack(self,stack: DynamicStack)->DynamicStack:
        if stack.isEmpty(): 
            return 
        val = stack.pop()
        rev = self.reversedStack(stack)
        stack = self.insertAtBottom(stack,val)
        return stack
    def insertAtBottom(self, stack: DynamicStack, val: int)->DynamicStack:
        if stack.isEmpty():
            stack.push(val)
            return
        temp = stack.pop()
        self.insertAtBottom(stack,val)
        stack.push(temp)
        return stack
if __name__ == "__main__":
    Solution().printSolution()