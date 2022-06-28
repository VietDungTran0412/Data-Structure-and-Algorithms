from LinkedList import Node, SinglyLinkedList
class Solution:
    def printSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([1,2,3,4,5])
        ll.head = self.reverseBlockOfKNodes(ll.head,3)
        ll.print()
    def isHasKthNode(self,head: Node,k: int):
        idx = 0
        cur = head
        while cur and idx < k:
            cur = cur.next
            idx+=1
        if idx == k:
            return True
        return False
    def reverseBlockOfKNodes(self,head: Node,k: int):
        if self.isHasKthNode(head,k) is False:
            return head
        prev = None
        cur = head
        next = None
        i = 0
        while cur and i < k:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            i+=1
        if next is not None:
            head.next = self.reverseBlockOfKNodes(next,k)
        return prev

if __name__ == "__main__":
    Solution().printSolution()

