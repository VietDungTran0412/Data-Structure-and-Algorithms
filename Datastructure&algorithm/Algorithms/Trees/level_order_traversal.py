from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,2,4,1,7,6,8,10,9,12])
        res = self.levelOrder(root)
        return str(res)
    def levelOrder(self,root: BinarySearchTreeNode)->list[list[int]]:
        if root is None:
            return []
        q = [root,None]
        res = [[]]
        while len(q)>0:
            temp = q[0]
            q = q[1:]
            if temp is None:
                if len(q)>0:
                    q.append(None)
                    res.append([])
            else:
                res[-1].append(temp.data)
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                l = len(res)
        half = len(res)//2
        i = 0
        while i < half:
            temp = res[i]
            res[i] = res[len(res)-1-i]
            res[len(res)-1-i] = temp
            i+=1
        return res
print(Solution())