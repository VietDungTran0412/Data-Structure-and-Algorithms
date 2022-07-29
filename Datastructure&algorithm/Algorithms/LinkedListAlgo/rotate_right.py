from LinkedList import SinglyLinkedList, Node
class Solution:
    def printSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([1,2,3,4,5])
        ll.head = self.rotateRight(ll.head,11)
        ll.print()
    def rotateRight(self,head: Node,k: int):
        if head is None or head.next is None or k == 0:
            return head
        len = 1
        cur = head
        while cur.next:
            cur = cur.next
            len+=1
        cur.next = head
        rot = k % len
        i = len
        while i - rot >0:
            head = head.next
            cur = cur.next
            i -=1
        cur.next = None
        return head
Solution().printSolution()