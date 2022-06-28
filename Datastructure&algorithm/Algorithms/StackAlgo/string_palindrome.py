from inspect import stack
from Stack import CreateDynStack
class Solution:
    def printSolution(self):
        string = "jkXkj"
        print(self.reverseStack())
    def isPalindrome(self,string):
        chars = CreateDynStack(len(string))
        i = 0
        while string[i] != "X":
            chars.push(string[i])
            i+=1
        i+=1
        while i < len(string):
            if chars.isEmptyStack() or string[i] != chars.pop():
                return False
            i+=1
        return chars.isEmptyStack()
if __name__ == "__main__":
    Solution().printSolution()

