from LinkedList import SinglyLinkedList
class Solution:
    def printSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([1,2,3,4,5,6])
        ll.head = self.reverseLinkedListRecur(ll.head)
        ll.print()
    def reverseLinkedListRecur(self,head):
        if head is None:
            return None
        if head.next is None:
            return head
        prev = self.reverseLinkedListRecur(head.next)
        temp = head.next
        temp.next = head
        head.next = None
        return prev
Solution().printSolution()