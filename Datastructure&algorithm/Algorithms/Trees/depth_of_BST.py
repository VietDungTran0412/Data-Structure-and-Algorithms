from Tree import build_tree,BinarySearchTreeNode

class Solution:
    def __repr__(self) -> str:
        nums = [2,5,9,6,7,8,3,4,15,12,14]
        root = build_tree(nums)
        return str(self.heightOfBSTNonRecursive(root))
    def heightOfBST(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        right = self.heightOfBST(root.right)
        left = self.heightOfBST(root.left)
        return max(right,left) + 1
    def heightOfBSTNonRecursive(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        level = 0
        q = [root,None]
        i = 0
        while len(q)>0:
            temp = q[0]
            q = q[1:]
            if temp is None:
                if len(q) > 0:
                    q.append(None)
                level+=1
            else:
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
        return level


print(Solution())