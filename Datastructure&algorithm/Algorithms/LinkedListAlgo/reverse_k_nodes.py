from LinkedList import Node, SinglyLinkedList
class Solution:
    def printSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([1,2,3,4,5,6])
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
    def getKThNode(self,head: Node,k: int)-> Node:
        count  = 0
        cur = head
        while cur and count < k:
            cur = cur.next
            count +=1
        if count == k:
            return cur
        return None
    def reverseBlockOfKNodesIterative(self,head: Node,k: int)->Node:
        if self.isHasKthNode(head,k) is False:
            return head
        cur = head
        newHead = self.getKThNode(cur,k+1)  
        while cur and self.isHasKthNode(cur,k):
            prev = self.getKThNode(cur,k+1)    
            for i in range(k):
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
        return newHead

    def reverseBlockOfKNodes(self,head: Node,k: int):
        if self.isHasKthNode(head,k) is False:
            return head
        prev = None
        cur = head
        next = None
        count = 0
        while cur and count < k:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            count += 1
        if next:
            head.next = self.reverseBlockOfKNodes(next,k)
        return prev

if __name__ == "__main__":
    Solution().printSolution()

