from Tree import BinarySearchTreeNode, build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,3,8,6,9,4,2,19,7])
        return str(self.levelWithMaxSum(root))
    def levelWithMaxSum(self,root: BinarySearchTreeNode)->int:
        max = -1000000
        maxLevel = 0
        curLevel = 0
        q = [root,None]
        sum = 0
        while len(q)>0:
            temp = q[0]
            q = q[1:]
            if temp is None:
                if len(q)>0:
                    q.append(None)
                if sum > max:
                    max = sum
                    sum = 0
                    maxLevel = curLevel
                curLevel += 1 
            else:
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                sum += temp.data
        return maxLevel
print(Solution())