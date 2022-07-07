from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        nums = []
        root = build_tree(nums)
        return str(self.getNumberOfLeavesRecursive(root))
    def getNumberOfLeavesRecursive(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        ans = 0
        if root.left:
            ans += self.getNumberOfLeavesRecursive(root.left)
        if root.right:
            ans += self.getNumberOfLeavesRecursive(root.right)
        return ans
    def getNumberOfLeavesNoRecursive(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        q = [root]
        ans = 0
        while len(q)>0:
            temp = q[0]
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            if temp.left is None and temp.right is None:
                ans += 1
            q = q[1:]
        return ans

print(Solution())

        
        