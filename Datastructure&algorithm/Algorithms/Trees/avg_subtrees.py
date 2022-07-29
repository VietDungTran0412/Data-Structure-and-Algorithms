from Tree import BinarySearchTreeNode,build_tree
class Subnode:
    def __init__(self) -> None:
        self.sum = 0
        self.count = 0
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,2,7,6,8,1,3])
        res = str(self.averageOfSubtree(root))
        return res
    def getAvgOfSubtree(self,root:BinarySearchTreeNode,subnodes:Subnode):
        if root is None:
            subnodes.sum = 0
            subnodes.count = 0
            return 0
        lnodes = Subnode()
        rnodes = Subnode()
        count = 0
        l = self.getAvgOfSubtree(root.left,lnodes)
        r = self.getAvgOfSubtree(root.right,rnodes)
        count += l+r
        totalSum =  root.data + lnodes.sum + rnodes.sum
        totalNodes = 1 + lnodes.count + rnodes.count
        if root.data == totalSum//totalNodes:
            count +=1
        subnodes.sum += root.data
        subnodes.count += 1
        return count
    def averageOfSubtree(self,root):
        subnode = Subnode()
        return self.getAvgOfSubtree(root,subnode)
print(Solution())