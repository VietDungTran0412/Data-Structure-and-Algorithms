from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,6])
        root = self.removeLeaves(root)
        return str(root.preorder())
    def removeLeaves(self,root: BinarySearchTreeNode):
        if root is None:
            return None
        if root.left is None and root.right is None:
            return None
        root.left = self.removeLeaves(root.left)
        root.right = self.removeLeaves(root.right)
        return root
print(Solution())