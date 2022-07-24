from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([6,2,10,8,12,4,5])
        res = self.LCABinaryTreeRecur(root,BinarySearchTreeNode(12),BinarySearchTreeNode(8))
        return str(res.data)
    def LCABinaryTreeRecur(self,root: BinarySearchTreeNode,p: BinarySearchTreeNode,q: BinarySearchTreeNode)->BinarySearchTreeNode:
        if root is None:
            return None
        if root.data == p.data or root.data == q.data:
            return root
        left = self.LCABinaryTreeRecur(root.left,p,q)
        right = self.LCABinaryTreeRecur(root.right,p,q)
        if left and right:
            return root
        if left:
            return left
        if right:
            return right
print(Solution())