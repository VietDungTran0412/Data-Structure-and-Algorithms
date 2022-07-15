from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([1,2,3,4])
        return str(self.hasPathSumAlter(root,6))
    def hasPathSum(self,root: BinarySearchTreeNode, sum: int)->bool:
        if root is None:
            return sum == 0
        if root.data == sum:
            return True
        elif root.data < sum:
            return self.hasPathSum(root.left,sum-root.data) or self.hasPathSum(root.right,sum-root.data)
        else:
            return self.hasPathSum(root.left,sum) or self.hasPathSum(root.right,sum)
    def hasPathSumAlter(self,root: BinarySearchTreeNode, sum: int)->bool:
        if root is None:
            return sum == 0
        remaining = sum - root.data
        if (root.left and root.right) or (root.left is None and root.right is None):
            return self.hasPathSumAlter(root.left,remaining) or self.hasPathSum()
        elif root.left:
            return self.hasPathSum(root.left,remaining)
        else:
            return self.hasPathSum(root.right,remaining)
print(Solution())