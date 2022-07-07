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
            elements += self.preorder()
        if self.right:
            elements += self.preorder()
        return elements
    def inorder(self)->list:
        elements = []
        if self.left:
            elements += self.preorder()
        elements.append(self.data)
        if self.right:
            elements += self.preorder()
        return elements
    def postorder(self)->list:
        elements = []
        if self.left:
            elements += self.preorder()
        if self.right:
            elements += self.preorder()
        elements.append(self.data)
        return elements
def build_tree(elements):
    if len(elements) == 0:
        return None
    root = BinarySearchTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.insert(elements[i])
    return root        