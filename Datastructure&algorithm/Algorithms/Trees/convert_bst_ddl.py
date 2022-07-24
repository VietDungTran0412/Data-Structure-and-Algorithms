from Tree import BinarySearchTreeNode,build_tree
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
class Solution:
    def __repr__(self) -> str:
        pass
    def convertBSTtoDDL(self,root:BinarySearchTreeNode,tail):
        if root is None:
            ltail = None
            return None
        