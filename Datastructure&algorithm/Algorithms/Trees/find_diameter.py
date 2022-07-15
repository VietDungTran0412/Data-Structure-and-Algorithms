from Tree import BinarySearchTreeNode,build_tree
class Height:
    def __init__(self) -> None:
        self.h = 0
class Solution:
    def __repr__(self) -> str:
        root = build_tree([7,3,5,9,15,6,4,8,12])
        height = Height()
        res = self.findDiameterBST(root,height)
        return str(res)
    def findDiameterBST(self,root: BinarySearchTreeNode, height):
        lh = Height()
        rh = Height()
        if root is None:
            height.h = 0
            return 0
        ldiameter = self.findDiameterBST(root.left,lh)
        rdiameter = self.findDiameterBST(root.right,rh)
        height.h = max(lh.h,rh.h)+1
        return max(lh.h+rh.h,max(ldiameter,rdiameter))
    def getHeight(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        return 1 + max(self.getHeight(root.left),self.getHeight(root.right))
    def findDiameterBSTAlter(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        lHeight = self.getHeight(root.left)
        rHeight = self.getHeight(root.right)
        lDiameter = self.findDiameterBSTAlter(root.left)
        rDiameter = self.findDiameterBSTAlter(root.right)
        return max(lHeight+rHeight+1,max(lDiameter,lDiameter))
        
print(Solution())