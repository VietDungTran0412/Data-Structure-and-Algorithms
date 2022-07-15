from stack import DynamicStack
class Solution:
    def printSolution(self):
        prices = [4,2,6,3,1,2]
        print(self.findingSpans(prices,5))
    def findingSpans(self,prices: list,n: int)->list:
        res = [1 for i in range(len(prices))]
        stack = DynamicStack()
        stack.push(0)
        res[0] = 1
        # [1,3,4,5,2]
        # i = 1 --> prices[0] <= prices[1] = False
        # stack not empty
        # res[1] = i - 0
        for i in range(1,len(prices)):
            while stack.isEmpty() is False and prices[stack.peek()]<= prices[i]:
                stack.pop()
            if stack.isEmpty():
                res[i] = i + 1
            else:
                res[i] = i - stack.peek()
            stack.push(i)
        return res

                
Solution().printSolution()
