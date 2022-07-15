from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        res = []
        root = build_tree([7,3,5,8,9,4,2,10,15,12])
        self.getRootToPath(root,[],0,res)
        return str(res)
    def getRootToPath(self,root: BinarySearchTreeNode,path: list, pathLen: int, res: list):
        if root is None:
            return 
        if len(path)>pathLen:
            path[pathLen] = root.data
        else:
            path.append(root.data)
        pathLen+=1
        if root.left is None and root.right is None:
            p = self.addRootToPath(path,pathLen)
            res.append(p)
        else:
            self.getRootToPath(root.left,path,pathLen,res)
            self.getRootToPath(root.right,path,pathLen,res)
    def addRootToPath(self,path: list, length: int):
        pathStr = ""
        for i in range(length-1):
            pathStr += str(path[i])+"->"
        return pathStr+str(path[length-1])
print(Solution())
