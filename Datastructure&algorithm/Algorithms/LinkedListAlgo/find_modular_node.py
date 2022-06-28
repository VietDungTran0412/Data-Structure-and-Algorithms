from LinkedList import SinglyLinkedList
class Solution:
    def printSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([x for x in range(1,20)])
        ll.print()
        res = self.modularNodeFromStart(ll.head,3)
        print(res.val)
    def modularNodeFromStart(self,head,k):
        if k <= 0:
            return None
        modularNode = None
        i = 0
        while head != None:
            if i%k == 0:
                modularNode = head
            head = head.next
            i+=1
        return modularNode
if __name__ == "__main__":
    Solution().printSolution()