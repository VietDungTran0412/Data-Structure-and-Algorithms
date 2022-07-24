from Tree import BinarySearchTreeNode
class Height:
    def __init__(self) -> None:
        self.h = 0
class Solution:
    def __repr__(self) -> str:
        root = BinarySearchTreeNode(5)
        root.left = BinarySearchTreeNode(10)
        root.right = BinarySearchTreeNode(20)
        root.right.right = BinarySearchTreeNode(20)
        root.right.right.right = BinarySearchTreeNode(20)
        height = Height()
        res = self.isBalancedBST(root,height)
        return str(res)
    def isBalancedBST(self,root: BinarySearchTreeNode,height: Height)->bool:
        if root is None:
            return True
        lh = Height()
        rh = Height()
        p  = self.isBalancedBST(root.left,lh)
        q = self.isBalancedBST(root.right,rh)
        height.h = max(lh.h,rh.h)+1
        if abs(lh.h-rh.h)<= 1:
            return p and q
        return False
print(Solution())