from Tree import build_tree,BinarySearchTreeNode
class Solution:
    def __repr__(self) -> str:
        nums = [5,2,8,6,7,10,12,11,9,4,3]
        root = build_tree(nums)
        return str(self.bfsearchInBST(root,5))
    def dfsearchInBST(self,root: BinarySearchTreeNode,val: int)->bool:
        if root is None:
            return False
        if root.data == val:
            return True
        temp = self.dfsearchInBST(root.left,val)
        if temp:
            return temp
        return self.dfsearchInBST(root.right,val)
    def bfsearchInBST(self, root: BinarySearchTreeNode, val: int)->bool:
        if root is None:
            return False
        q = [root]
        i = 0
        while i < len(q):
            if q[i].data == val:
                return True
            if q[i].left:
                q.append(q[i].left)
            if q[i].right:
                q.append(q[i].right)
            i+=1
        return False
if __name__ =="__main__":
    print(Solution())
        