from LinkedList import SinglyLinkedList
class Solution:
    def getSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([1,2,3,4,5,6,7,8,9,10])
        ll.head = self.reverseBlockOfKNodes(ll.head,5)
        ll.print()
    def getKNodePlusOne(self,head,k):
        kNode = head
        i = 0
        if head is None:
            return head
        while i < k and kNode:
            kNode = kNode.next
            i+=1
        if i == k and kNode:
            return kNode
        return head.next
    def isKNodeExist(self,head,k):
        i = 0
        itr = head
        while itr and i < k:
            i+=1
            itr = itr.next
        if i == k:
            return True
        return False
    def reverseBlockOfKNodes(self,head,k):
        cur = head
        if k == 1:
            return head
        if self.isKNodeExist(cur,k-1):
            new_head = self.getKNodePlusOne(cur,k-1)
        else:
            new_head = head
        while cur and self.isKNodeExist(cur,k):
            temp = self.getKNodePlusOne(cur,k)
            for i in range(k):
                next = cur.next
                cur.next = temp
                temp = cur
                cur = next
        return new_head
if __name__ == "__main__":
    Solution().getSolution()

