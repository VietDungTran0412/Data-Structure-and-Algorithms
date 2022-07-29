from Tree import BinarySearchTreeNode, build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,2,8,7,10])
        root = self.removeNodesInRange(root,5,9)
        return str(root.preorder())
    def findMin(self,root: BinarySearchTreeNode):
        if root .left is None:
            return root
        return self.findMin(root.left)
    def deleteNode(self,root: BinarySearchTreeNode):
        if root is None:
            return None
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        min = self.findMin(root.right)
        root.data = min.data
        root.right = self.deleteNode(min)

        
    def removeNodesInRange(self,root: BinarySearchTreeNode,x: int,y: int):
        if root is None: 
            return None
        
        root.left = self.removeNodesInRange(root.left,x,y)
        root.right = self.removeNodesInRange(root.right,x,y)
        if (root.data > x and root.data < y) or (root.data <x and root.data > y):
            return self.deleteNode(root)
        return root
print(Solution())
nums = [1,2,3]
print(nums[:0])