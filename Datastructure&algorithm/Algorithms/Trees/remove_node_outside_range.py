from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,2,1,3,10,7,6,8,12,15])
        root = self.removeNodesOutRange(root,6,10)
        return str(root.preorder())
    def removeNodesOutRange(self,root: BinarySearchTreeNode, x: int, y :int):
        if root is None:
            return None
        root.left = self.removeNodesOutRange(root.left,x,y)
        root.right = self.removeNodesOutRange(root.right,x,y)
        if (root.data >= x and root.data <= y) or (root.data >= y and root.data <= x):
            return root
        if root.data < x and root.data < y:
            return root.right
        if root.data > x and root.data > y:
            return root.left
print(Solution())