from Tree import BinarySearchTreeNode,build_tree
import math
class Carry:
    def __init__(self) -> None:
        self.mini = math.inf
        self.maxi = -math.inf
class Solution:
    def __repr__(self) -> str:
        root = build_tree([8,3,10,1,6,4,7,14,13,])
        return str(self.maxAncestorDiff(root))
    def maxAncestorDiffUtil(self,root: BinarySearchTreeNode,mini,maxi):
        if root is None:
            return abs(mini-maxi)
        left = self.maxAncestorDiffUtil(root.left,min(root.data,mini),max(root.data,maxi))
        right = self.maxAncestorDiffUtil(root.right,min(root.data,mini),max(root.data,maxi))
        return max(left,right)


    def maxAncestorDiff(self,root: BinarySearchTreeNode):
        maxi = -math.inf
        mini = math.inf
        return self.maxAncestorDiffUtil(root,mini,maxi)
print(Solution())