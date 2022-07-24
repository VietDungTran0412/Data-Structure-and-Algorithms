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
def build_tree(elements):
    if len(elements) == 0:
        return None
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.insert(elements[i])
    return root  

