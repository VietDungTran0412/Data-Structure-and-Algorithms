from Stack import CreateDynStack
class Solution:
    def printSolution(self):
        stack = CreateDynStack(20)
        vals = [x for x in range(20)]
        for val in vals:
            stack.push(val)
        self.reverseStack(stack)
        stack.print()
    def reverseStack(self,stack):
        if stack.isEmptyStack():
            return
        temp = stack.pop()
        self.reverseStack(stack)
        self.insertAtBottom(stack,temp)

    def insertAtBottom(self,stack,val):
        if stack.isEmptyStack():
            stack.push(val)
            return
        temp = stack.pop()
        self.insertAtBottom(stack,val)
        stack.push(temp)
if __name__ == "__main__":
    Solution().printSolution()