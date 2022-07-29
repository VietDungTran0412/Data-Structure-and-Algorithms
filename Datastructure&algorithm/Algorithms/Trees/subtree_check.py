from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = BinarySearchTreeNode(3)
        root.right = BinarySearchTreeNode(5)
        subRoot = BinarySearchTreeNode(4)
        subRoot.right = BinarySearchTreeNode(2)
        subRoot.left = BinarySearchTreeNode(1)
        root.left = BinarySearchTreeNode(4)
        root.left.left = BinarySearchTreeNode(1)
        root.left.right = BinarySearchTreeNode(2)
        root.left.right.left = BinarySearchTreeNode(0)
        return str(self.isSubtreeAlter(root,subRoot))
    def isIdentical(self,root1: BinarySearchTreeNode,root2: BinarySearchTreeNode):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return (root1.data == root2.data) and self.isIdentical(root1.left,root2.left) and self.isIdentical(root1.right,root2.right)
    def isSubtree(self,root: BinarySearchTreeNode, subRoot: BinarySearchTreeNode)->bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        if root.data ==subRoot.data:
            if self.isIdentical(root,subRoot):
                return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
    def preOrder(self,root: BinarySearchTreeNode)->str:
        if root is None:
            return "#"
        res = str(root.data)
        res += self.preOrder(root.left)
        res += self.preOrder(root.right)
        return res
    def inOrder(self,root: BinarySearchTreeNode)->str:

        if root is None:
            return "#"
        res = ""
        res += self.inOrder(root.left)
        res += str(root.data)
        res += self.inOrder(root.right)
        return res
    def isSubstring(self,main,sub):
        i = 0
        while i < len(main):
            if main[i] == sub[0]:
                j = 0
                while j < len(sub) and i + j < len(main):
                    if sub[i] != main[j]:
                        break
                    j+=1
                    i+=j
                if j == len(sub)-1:
                    return True
            i+=1
        return False
    def isSubtreeAlter(self,root: BinarySearchTreeNode, subRoot: BinarySearchTreeNode)->bool:
        if subRoot is None:
            return True
        if root is None:
            return False
        preOrderRoot = self.preOrder(root)
        preOrderSubroot = self.preOrder(subRoot)
        inOrderRoot = self.inOrder(root)
        inOrderSubroot = self.inOrder(subRoot)
        if self.isSubstring(preOrderRoot,preOrderSubroot) and self.isSubstring(inOrderRoot,inOrderSubroot):
            return True
        return False


print(Solution())