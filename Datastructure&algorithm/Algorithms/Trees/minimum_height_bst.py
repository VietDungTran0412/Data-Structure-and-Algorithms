from Tree import BinarySearchTreeNode, build_tree
class QueueElements:
    def __init__(self,node:BinarySearchTreeNode,x: int) -> None:
        self.node = node
        self.depth = x
class Solution:
    def __repr__(self) -> str:
        root = build_tree([5,2,8,7,10,12])
        res = self.getMinimumDepthLevelOrder(root)
        return str(res)
    def getMinimumDepth(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return self.getMinimumDepth(root.right)+1
        if root.right is None:
            return self.getMinimumDepth(root.left)+1
        return min(self.getMinimumDepth(root.left),self.getMinimumDepth(root.right))+1
    def getMinimumDepthAlter(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        if root.left is None or root.right is None:
            return self.getMinimumDepthAlter(root.left) + self.getMinimumDepthAlter(root.right)+1
        left = self.getMinimumDepthAlter(root.left)+1
        right = self.getMinimumDepthAlter(root.right)+1
        return min(left,right)
    def getMinimumDepthLevelOrder(self,root: BinarySearchTreeNode)->int:
        if root is None:
            return 0
        q = []
        f_element = QueueElements(root,1)
        q.append(f_element)
        while len(q)>0:
            temp = q[0]
            q = q[1:]
            node = temp.node
            depth = temp.depth
            if node.left is None and node.right is None:
                return depth
            if node.left:
                temp.node = node.left
                temp.depth = depth + 1
                q.append(temp)
            if node.right:
                temp.node = node.left
                temp.depth = depth + 1
                q.append(temp)
        return 0
print(Solution())