import math
from Tree import BinarySearchTreeNode,build_tree
class Solution:
    def __repr__(self) -> str:
        root = build_tree([236,701,104,227,911])
        res = self.getMinimumDifference(root,-math.inf,math.inf)
        return str(res)
    def getMinimumDifference(self,root: BinarySearchTreeNode,min_val: int,max_val: int)->int:
        if root is None:
            return math.inf
        
        left_min = self.getMinimumDifference(root.left, min_val, root.data)
        right_min = self.getMinimumDifference(root.right, root.data, max_val)
        
        min_diff = min(abs(min_val - root.data), abs(max_val - root.data))
        return min(left_min, right_min, min_diff)
class ListNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
def printll(head: ListNode):
    cur = head
    while cur:
        print(cur.val)
        cur = cur.next
def reverse(head: ListNode):
    if head is None or head.next is None:
        return head
    prev = reverse(head.next)
    temp = head.next
    temp.next = head
    head.next = None
    return prev
head = reverse(head)
printll(head)
print(Solution())
        