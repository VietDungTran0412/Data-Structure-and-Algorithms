# Reorder the linked list {A1,A2,...,An} to {A1,An,A2,An-1}
from LinkedList import SinglyLinkedList
from LinkedList import Node
class Solution:
    def printSolution(self):
        ll1 = SinglyLinkedList()
        ll1.insert_values([1,2,3,4,5,6,7,8,9,10,14,15,19,20])
        ll1.head = self.reorderLinkedList(ll1.head)
        ll1.print()
    def reverse(self,head):
        if head is None:
            return None
        prev = None
        cur = head
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    def reorderLinkedList(self,head):
        if head is None:
            return None
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_head = slow.next
        slow.next = None
        second_head = self.reverse(second_head)
        newNode = Node(-1)
        cur = newNode
        while head and second_head:
            cur.next = head
            head = head.next
            cur = cur.next
            cur.next = second_head
            second_head = second_head.next
            cur = cur.next
        if head is None:
            cur.next = second_head
        if second_head is None:
            cur.next = head
        return newNode.next
if __name__ == "__main__":
    Solution().printSolution()