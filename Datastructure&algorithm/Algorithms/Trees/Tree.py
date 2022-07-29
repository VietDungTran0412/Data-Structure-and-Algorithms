class BinarySearchTreeNode:
    def __init__(self,data,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
    def insert(self,val):
        if self.data == val:
            return
        if val < self.data:
            if self.left:
                self.left.insert(val)
            else:
                self.left = BinarySearchTreeNode(val)
        else:
            if self.right:
                self.right.insert(val)
            else:
                self.right = BinarySearchTreeNode(val)
    def preorder(self)->list:
        elements = []
        elements.append(self.data)
        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()
        return elements
    def inorder(self)->list:
        elements = []
        if self.left:
            elements += self.left.preorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.preorder()
        return elements
    def postorder(self)->list:
        elements = []
        if self.left:
            elements += self.left.preorder()
        if self.right:
            elements += self.right.preorder()
        elements.append(self.data)
        return elements
def build_tree(elements):
    if len(elements) == 0:
        return None
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.insert(elements[i])
    return root  
class NAryTreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.parent = None
        self.children = []
    def add_child(self,child):
        child.parent = self
        self.children.append(child)
class TreeNode:
    def __init__(self,data) -> None:
        self.data = data
        self.firstChild = None
        self.secondChild = None
        self.thirdChild = None
        self.fourthChild = None
        self.fifthChild = None
        self.sixthChild = None

class AVLTreeNode:
    def __init__(self,val) -> None:
        self.val = val
        self.left = None
        self.right = None
        self.height = 0

class AVLTree:
    def insert(self,root: AVLTreeNode,val)->AVLTreeNode:
        if root is None:
            root = AVLTreeNode(val)
        if val < root.val:
            root.left = self.insert(root.left,val)
            if self.height(root.left)- self.height(root.right) == 2:
                if val < root.left.val:
                    root = self.leftRotate(root)
                else:
                    root = self.doubleRotateLeft(root)
        elif val > root.val:
            root.right = self.insert(root.right,val)
            if self.height(root.right) - self.height(root.left) == 2:
                if val > root.right.val:
                    root = self.rightRotate(root)
                else:
                    root = self.doubleRotateRight(root)
        root.height = max(self.height(root.left),self.height(root.right))+1
        return root
    def doubleRotateLeft(self,root: AVLTreeNode):
        root.left = self.rightRotate(root.left)
        return self.leftRotate(root)
    
    def doubleRotateRight(self,root: AVLTreeNode):
        root.right = self.leftRotate(root.right)
        return self.rightRotate(root)

    def balance(self,root):
        if root is None:
            return 0
        return self.height(root.left) - self.height(root.right)

    def height(self,root: AVLTreeNode)->int:
        if root is None:
            return 0
        return root.height

    def leftRotate(self,root: AVLTreeNode)->AVLTreeNode:
        newRoot = root.left
        root.left = newRoot.right
        newRoot.right = root
        root.height = max(self.height(root.left),self.height(root.right))+1
        newRoot.height = max(self.height(newRoot.left),self.height(newRoot.right))+1
        return newRoot


    def rightRotate(self,root: AVLTreeNode)->AVLTreeNode:
        newRoot = root.right
        root.right = newRoot.left
        newRoot.left = root
        root.height = max(self.height(root.left),self.height(root.right))+1
        newRoot.height = max(self.height(newRoot.left),self.height(newRoot.right))+1
        return newRoot

    def preorder(self,root):
        if root is None:
            return []
        elements = []
        elements.append(root.val)
        elements += self.preorder(root.left)
        elements += self.preorder(root.right)
        return elements
