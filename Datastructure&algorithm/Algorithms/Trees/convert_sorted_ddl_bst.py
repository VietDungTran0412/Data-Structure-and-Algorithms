from Tree import BinarySearchTreeNode, build_tree
class DoublyNode:
    def __init__(self,x) -> None:
        self.val = x
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
    def prepend(self,val):
        if self.head is None:
            self.head = DoublyNode(val)
        else:
            newNode = DoublyNode(val)
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
class Solution:
    def __repr__(self) -> str:
        ll = DoublyLinkedList()
        nums = [9,7,5,3,1,0,-1]
        for num in nums:
            ll.prepend(num)
        root = self.convertDDLtoBSTAlter(ll.head)
        return str(root.preorder())
    def findMiddle(self,head)->DoublyNode:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def convertDDLtoBST(self,head: DoublyNode)->BinarySearchTreeNode:
        if head is None:
            return head
        if head.next is None:
            return BinarySearchTreeNode(head.val)
        temp = self.findMiddle(head)
        p = head
        while p.next != temp:
            p = p.next
        p.next = None
        q = temp.next
        temp.next = None
        root = BinarySearchTreeNode(temp.val)
        root.left = self.convertDDLtoBST(head)
        root.right = self.convertDDLtoBST(q)
        return root
    globalNode = None
    def convertDDLtoBSTAlter(self,head: DoublyNode):
        n = 0
        temp = head
        while temp:
            n +=1
            temp = temp.next
        self.globalNode = head
        return self.convertToBalancedBSTRecur(n)
    def convertToBalancedBSTRecur(self,n):
        if n == 0:
            return None
        leftSubTree = self.convertToBalancedBSTRecur(n//2)
        root = BinarySearchTreeNode(self.globalNode.val )
        self.globalNode = self.globalNode.next
        root.left = leftSubTree
        root.right = self.convertToBalancedBSTRecur(n-n//2-1)
        return root

print(Solution())
a = {"a":1,"b":3}
a.pop("a")
print(a)