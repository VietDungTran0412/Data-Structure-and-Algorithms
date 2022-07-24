from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([6,2,9,12,4,1,8])
        newRoot = self.getMirrorOfBST(root)
        return str(newRoot.preorder())
    def getMirrorOfBST(self,root: BinarySearchTreeNode)->BinarySearchTreeNode:
        if root is None:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.getMirrorOfBST(root.left)
        self.getMirrorOfBST(root.right)
        return root
print(Solution())