from Tree import BinarySearchTreeNode,build_tree

class Solution:
    def __repr__(self) -> str:
        nums = [5,2,12,4,6,1,18,9,15]
        root = build_tree(nums)
        return str(self.getSizeBSTRecursive(root))
    def getSizeBSTWithoutRecursive(self,root):
        if root is None:
            return 0
        q = [root]
        i = 0
        while i < len(q):
            if q[i].left:
                q.append(q[i].left)
            if q[i].right:
                q.append(q[i].right)
            i+=1
        return len(q)
    def getSizeBSTRecursive(self,root)->int:
        if root is None:
            return 0
        return 1 + self.getSizeBSTRecursive(root.left) + self.getSizeBSTRecursive(root.right)
print(Solution())