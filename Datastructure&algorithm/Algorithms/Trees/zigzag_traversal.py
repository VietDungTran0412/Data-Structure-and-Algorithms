from Tree import BinarySearchTreeNode
class Solution:
    def __repr__(self) -> str:
        root = BinarySearchTreeNode(1)
        root.left = BinarySearchTreeNode(2)
        root.right = BinarySearchTreeNode(3)
        root.left.left = BinarySearchTreeNode(4)
        root.left.right = BinarySearchTreeNode(5)
        root.right.right = BinarySearchTreeNode(7)
        root.right.left = BinarySearchTreeNode(6)
        return str(self.zigZagTraversal(root))
    def swap(self,a,b):
        temp = a
        a = b
        b = temp
    def zigZagTraversal(self,root: BinarySearchTreeNode):
        leftToRight = True
        if root is None:
            return
        elements = []
        currentLevel = [root]
        nextLevel = []
        while len(currentLevel)>0:
            temp = currentLevel.pop()
            if temp:
                elements.append(temp.data)
                if leftToRight:
                    if temp.left:
                        nextLevel.append(temp.left)
                    if temp.right:
                        nextLevel.append(temp.right)
                else:
                    if temp.right:
                        nextLevel.append(temp.right)
                    if temp.left:
                        nextLevel.append(temp.left)
                if len(currentLevel) == 0:
                    leftToRight = False
                    self.swap(currentLevel,nextLevel)
        return elements
print(Solution()) 
        
