from Tree import BinarySearchTreeNode,build_tree
import math
class Sum:
    def __init__(self) -> None:
        self.s =-math.inf
class Solution:
    def __repr__(self) -> str:
        root = BinarySearchTreeNode(-100)
        return str(self.maxPathSum(root))
    def maxPathSum(self,root: BinarySearchTreeNode):
        res = Sum()
        self.findPathSumUtil(root,res)
        return res.s
    def findPathSumUtil(self,root: BinarySearchTreeNode, res: Sum()):
        if root is None:
            return 0

        l = self.findPathSumUtil(root.left,res)
        r = self.findPathSumUtil(root.right,res)
        
        maxPath = max(root.data,max(l,r)+root.data)
        maxSum = max(maxPath,l+r+root.data)

        res.s = max(maxSum,res.s)

        return maxPath
    
    


print(Solution())