from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,2])
        return str(self.getSumOfBSTNoRecur(root))
    def getSumOfBST(self,root:BinarySearchTreeNode)->int:
        if root is None:
            return
        sum = root.data
        if root.left:
            sum += self.getSumOfBST(root.left)
        if root.right:
            sum += self.getSumOfBST(root.right)
        return sum
    def getSumOfBSTNoRecur(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return
        q = [root]
        sum = 0
        while len(q)>0:
            temp = q[0]
            q = q[1:]
            sum += temp.data
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        return sum
print(Solution())