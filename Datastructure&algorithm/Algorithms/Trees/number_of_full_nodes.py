from Tree import BinarySearchTreeNode, build_tree
class Solution:
    def __repr__(self) -> str:
        nums = [2,5,9,6,7,8,3,4,15,12,14,9,20,16,18,17]
        root = build_tree(nums)
        return str(self.getNumberOfFullNodes(root))
    def getNumberOfFullNodes(self,root: BinarySearchTreeNode)-> int:
        if root is None:
            return 0
        ans = 0
        if root.left and root.right:
            ans += 1
        if root.left:
            ans += self.getNumberOfFullNodes(root.left)
        if root.right:
            ans += self.getNumberOfFullNodes(root.right)
        return ans
    def getNumberOfFullNodesNoRecursive(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        q = [root]
        res = 0
        i = 0
        while i < len(q):
            temp = q[i]
            if temp.left and temp.right:
                res += 1
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
            i+=1
        return res
print(Solution())