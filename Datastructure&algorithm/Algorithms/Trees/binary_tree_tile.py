from Tree import BinarySearchTreeNode,build_tree
class Sum:
    def __init__(self) -> None:
        self.s = 0
class Solution:
    def __repr__(self) -> str:
        root = BinarySearchTreeNode(1)
        root.left = BinarySearchTreeNode(2)
        root.right = BinarySearchTreeNode(3)
        # root.left.left = BinarySearchTreeNode(3)
        # root.left.right = BinarySearchTreeNode(5)
        # root.right.right = BinarySearchTreeNode(7)
        return str(self.getTiltTree(root,Sum()))
    def getTiltTree(self,root:BinarySearchTreeNode,sum):
        lsum = Sum()
        rsum = Sum()
        if root is None:
            return 0
        res = 0
        left = self.getTiltTree(root.left,lsum)
        right = self.getTiltTree(root.right,rsum)
        sum.s += root.data + lsum.s+rsum.s
        root.data = abs(lsum.s-rsum.s)
        res += root.data + left + right
        return res
print(Solution())