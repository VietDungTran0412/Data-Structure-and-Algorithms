from Tree import BinarySearchTreeNode,build_tree
class Height:
    def __init__(self) -> None:
        self.h = 0
class QueueElements:
    def __init__(self,node,level) -> None:
        self.node = node
        self.level = level
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,1,6])
        return str(self.isCousins(root,6,1))
    def isParents(self,root: BinarySearchTreeNode,x,y):
        if root is None:
            return False
        if root.left and root.right:
            if root.left.data == x and root.right.data == y:
                return True
            elif root.right.data == x and root.left.data == y:
                return True
        return False
    def isCousins(self,root: BinarySearchTreeNode,x :int, y: int)->bool:
        firstElement = QueueElements(root,0)
        q = [firstElement,None]
        curLevel = 0
        x_level = -1
        y_level = -1
        while len(q)>0:
            temp = q[0]
            q = q[1:]
            if temp is None:
                if len(q)>0:
                    curLevel += 1
                    q.append(None)
            else:
                node = temp.node
                level = temp.level
                if self.isParents(node,x,y):
                    return False
                if node.left:
                    newElement = QueueElements(node.left,level+1)
                    q.append(newElement)
                if node.right:
                    newElement = QueueElements(node.right,level+1)
                    q.append(newElement)
                if node.data == x:
                    x_level = level
                if node.data == y:
                    y_level = level
        return x_level == y_level
                


        
print(Solution())