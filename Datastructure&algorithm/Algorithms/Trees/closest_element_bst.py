from turtle import right
from Tree import BinarySearchTreeNode,build_tree
import math
class Result:
    def __init__(self) -> None:
        self.dis = math.inf
class Solution:
    def __repr__(self) -> str:
        root = build_tree([4,2,8,7,10])
        res = self.closestElementBST(root,6)
        return str(res.data)
    def closestElementBST(self,root: BinarySearchTreeNode,key: int):
        if root is None:
            return None
        if root.data == key:
            return root
        if root.data > key:
            if root.left is None:
                return root
            temp = self.closestElementBST(root.left,key)
            if abs(root.data-key) > abs(temp.data-key):
                return temp
            return root
        else:
            if root.right is None:
                return root
            temp = self.closestElementBST(root.right,key)
            if abs(root.data-key) > abs(temp.data-key):
                return temp
            return root
print(Solution())