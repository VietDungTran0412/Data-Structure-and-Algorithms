from Tree import BinarySearchTreeNode, build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,2,9,6,7,12,3,8,15])
        root = self.deleteNodeBST(root,9)
        return str(root.preorder())
    def findMax(self,root: BinarySearchTreeNode)->int:
        if root.right is None:
            return root.data
        return self.findMax(root.right)
    def findMin(self,root: BinarySearchTreeNode)->int:
        if root.left is None:
            return root.data
        return self.findMin(root.left)
    def deleteNodeBST(self,root: BinarySearchTreeNode, val: int):
        if root is None:
            return None
        if val < root.data:
            root.left = self.deleteNodeBST(root.left,val)
        elif val > root.data:
            root.right = self.deleteNodeBST(root.right,val)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            min = self.findMin(root.right)
            root.data = min
            root.right = self.deleteNodeBST(root.right,min)
        return root


        
print(Solution())