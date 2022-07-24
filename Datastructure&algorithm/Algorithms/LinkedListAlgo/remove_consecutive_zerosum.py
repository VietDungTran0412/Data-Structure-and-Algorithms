from LinkedList import SinglyLinkedList,Node
class Solution:
    def printSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([2,3,-3,4,1,-2,-3,2,5,1])
        ll.head = self.removeZeroConsecutive(ll.head)
        ll.print()
    def removeZeroConsecutive(self,head: Node)->Node:
        dummy = Node(0)
        hm = {}
        dummy.next = head
        pSum = 0
        hm[pSum] = dummy
        while head:
            pSum += head.val
            if pSum not in hm:
                hm[pSum] = head
            else:
                removeNode = hm[pSum].next
                sum = pSum
                while removeNode != head:
                    sum += removeNode.val
                    hm.pop(sum)
                    removeNode = removeNode.next
                hm[pSum].next = head.next
            head = head.next
        return dummy.next
Solution().printSolution()