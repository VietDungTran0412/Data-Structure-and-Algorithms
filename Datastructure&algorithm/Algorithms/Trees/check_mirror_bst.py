from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root1 = build_tree([6,2,9,12,4,1,8])
        root2 = BinarySearchTreeNode(6)
        root2.left = BinarySearchTreeNode(9)
        root2.right = BinarySearchTreeNode(2)
        root2.left.left= BinarySearchTreeNode(12)
        root2.left.right = BinarySearchTreeNode(8)
        root2.right.right = BinarySearchTreeNode(1)
        root2.right.left = BinarySearchTreeNode(4)
        return str(self.areMirrors(root1,root2))
    def areMirrors(self,root1:BinarySearchTreeNode,root2:BinarySearchTreeNode)->bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.data != root2.data:
            return False
        return self.areMirrors(root1.left,root2.right) and self.areMirrors(root1.right,root2.left)
print(Solution())