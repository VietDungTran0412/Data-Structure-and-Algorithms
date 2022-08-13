from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([1,2])
        return str(self.findMode(root))
    def addElements(self,root: BinarySearchTreeNode,hm: dict):
        if root is None:
            return
        if root.data not in hm:
            hm[root.data] = 1
        else:
            hm[root.data] += 1
        self.addElements(root.left,hm)
        self.addElements(root.right,hm)
    def findMode(self,root: BinarySearchTreeNode)->list:
        if root is None:
            return []
        hm  = {}
        self.addElements(root,hm)
        res = []
        maxcount = 0
        for num in hm:
            if hm[num] > maxcount:
                res = [num]
                maxcount = hm[num]
                continue
            elif hm[num] == maxcount:
                res.append(num)
        return res
