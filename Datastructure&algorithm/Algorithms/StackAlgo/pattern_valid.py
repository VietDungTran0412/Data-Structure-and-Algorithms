from Stack import CreateDynStack
# Given a string containing n S's and n X's where S indicates a push operation
# and X indicates a pop operation, and with the stack initially empty, formulate
# the rule to check whether a given string of S operation is admissable or not

class Solution:
    def printSolution(self):
        pattern = "XSSSSS"
        stack = CreateDynStack(20)
        print(self.isPatternValid(pattern,stack))
    def isPatternValid(self,pattern,stack):
        for char in pattern:
            if char == "S":
                stack.push(char)
            if char == "X" and stack.isEmptyStack():
                return False
            elif char == "X" and stack.isEmptyStack() == False:
                stack.pop()
        return True

if __name__ == "__main__":
    Solution().printSolution()

