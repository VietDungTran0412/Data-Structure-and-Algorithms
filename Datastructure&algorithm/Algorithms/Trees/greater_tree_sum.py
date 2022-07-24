from Tree import BinarySearchTreeNode,build_tree
class Sum:
    def __init__(self) -> None:
        self.s = 0
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,2,8,6,9,3,1])
        root = self.transformBSTtoGST(root)
        return str(root.preorder())
    sum = 0
    def transformBSTtoGSTUtil(self,root: BinarySearchTreeNode,sum):
        if root is None:
            return
        self.transformBSTtoGSTUtil(root.right,sum)
        self.sum += root.data
        root.data = self.sum
        self.transformBSTtoGSTUtil(root.left,sum)
    def transformBSTtoGST(self,root):
        sum = Sum()
        self.transformBSTtoGSTUtil(root,sum)
        return root
print(Solution())