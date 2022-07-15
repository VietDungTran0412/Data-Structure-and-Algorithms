from Tree import BinarySearchTreeNode, build_tree

class Solution:
    def __repr__(self) -> str:
        nums = [2,5,9,6,7,8,3,4,15,12,14,9,20,16,18,17]
        root = build_tree(nums)
        return str(self.getNumberOfHalfNodesNoRecursive(root))
    def getNumberOfHalfNodesRecursive(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        res = 0
        if root.left and root.right is None:
            res += 1
        elif root.right and root.left is None:
            res += 1
        if root.left:
            res += self.getNumberOfHalfNodesRecursive(root.left)
        if root.right:
            res += self.getNumberOfHalfNodesRecursive(root.right)
        return res
    def getNumberOfHalfNodesNoRecursive(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        q = [root]
        res = 0
        while len(q)>0:
            temp = q[0]
            if temp.left and temp.right is None:
                res += 1
            elif temp.right and temp.left is None:
                res += 1
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            q = q[1:]
        return res
print(Solution())