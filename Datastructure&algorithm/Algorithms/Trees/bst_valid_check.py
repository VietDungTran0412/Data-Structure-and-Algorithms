from Tree import BinarySearchTreeNode
class Solution:
    def __repr__(self) -> str:
        root = BinarySearchTreeNode(5)
        root.left = BinarySearchTreeNode(2)
        root.right = BinarySearchTreeNode(7)
        root.right.left = BinarySearchTreeNode(4)
        res = self.isValidBST(root)
        return str(res)
    def isValidBST(self,root: BinarySearchTreeNode)->bool:
        min = -1000000
        max = 1000000
        return self.isValidBSTUtil(root,min,max)
    def isValidBSTUtil(self,root: BinarySearchTreeNode,min:int,max:int)->bool:
        if root is None:
            return True
        if root.data < min or root.data > max:
            return False
        return self.isValidBSTUtil(root.left,min,root.data) and self.isValidBSTUtil(root.right,root.data,max)
print(Solution())