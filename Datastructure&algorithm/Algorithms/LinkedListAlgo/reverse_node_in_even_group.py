from LinkedList import SinglyLinkedList, Node
class Solution:
    def printSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([5,2,6,3,9,1,7,3,8,4,12,21])
        ll.head = self.reverseEvenLengthGroups(ll.head)
        ll.print()
    def isHasKthNode(self,head: Node,k: int)->bool:
        cur = head
        idx = 0
        while cur and idx<k:
            cur = cur.next
            idx+=1
        if idx == k:
            return True
        return False
    def reverseGroupKNodes(self,head: Node, k: int)-> Node:
        if self.isHasKthNode(head,k) is False:
            return head
        if k % 2 == 0:
            count = 1
            cur = head
            prev = None
            next = None
            while cur and count < k:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next
                count +=1
            if next is not None:
                head.next = self.reverseGroupKNodes(next,k+1)
            return prev
        else:
            cur = head
            count = 1
            while cur and count < k:
                cur = cur.next
                count +=1
            if cur.next is not None:
                next = cur.next
                cur.next = self.reverseGroupKNodes(next,k+1)
            return head
    def reverseEvenLengthGroups(self,head: Node) -> Node:
        return self.reverseGroupKNodes(head,1)
if __name__ == "__main__":
    Solution().printSolution()