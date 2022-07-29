from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        n = 10
        return str(self.countTrees(5))
    def factorial(self,n):
        if n == 1:
            return 1
        return self.factorial(n-1)*n
    def countTrees(self,n:int):
        top = self.factorial(2*n)
        frac = self.factorial(n+1)*self.factorial(n)
        return top//frac
print(Solution())      