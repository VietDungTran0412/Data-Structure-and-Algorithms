from Tree import BinarySearchTreeNode,build_tree

class Solution:
    def __repr__(self) -> str:
        root = BinarySearchTreeNode(1)
        root.left = BinarySearchTreeNode(2)
        root.right = BinarySearchTreeNode(3)
        root.left.left = BinarySearchTreeNode(2)
        root.right.left = BinarySearchTreeNode(2)
        root.right.right = BinarySearchTreeNode(4)
        root = self.removeLeafNodes(root,2)
        return str(root.preorder())
    def _isLeaf(self,root):
        if root.left is None and root.right is None:
            return True
        return False
    def removeLeafNodes(self,root: BinarySearchTreeNode,target)->BinarySearchTreeNode:
        if root is None:
            return root
        root.left = self.removeLeafNodes(root.left,target)
        root.right = self.removeLeafNodes(root.right,target)
        if root.data == target:
            if self._isLeaf(root):
                return None
        return root
print(Solution())