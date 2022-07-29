import math
from Tree import BinarySearchTreeNode
class Solution:
    def __repr__(self) -> str:
        nums = [3,2,1,6,0,5]
        root = self.constructMaximumBinaryTree(nums)
        return str(root.preorder())
    def constructMaximumBinaryTree(self, nums: list) -> BinarySearchTreeNode:
        if len(nums) == 0:
            return None
        max_num = -math.inf
        max_idx = -1
        for i, num in enumerate(nums):
            max_num = max(num,max_num)
            if max_num == num:
                max_idx = i
        root = BinarySearchTreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(nums[:max_idx])
        root.right = self.constructMaximumBinaryTree(nums[(max_idx+1):])
        return root
print(Solution())