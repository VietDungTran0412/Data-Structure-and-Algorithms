from Tree import BinarySearchTreeNode, build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,2,8,1,6,9,10])
        root = self.removeHalfNodes(root)
        return str(root.preorder())
    def removeHalfNodes(self,root: BinarySearchTreeNode):
        if root is None:
            return None
        root.left = self.removeHalfNodes(root.left)
        root.right = self.removeHalfNodes(root.right)
        if root.left is None and root.right is None:
            return root
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left
        return root
print(Solution())