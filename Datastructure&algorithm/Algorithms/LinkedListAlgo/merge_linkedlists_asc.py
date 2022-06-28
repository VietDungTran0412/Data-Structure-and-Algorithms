from LinkedList import SinglyLinkedList
from LinkedList import Node
class Solution:
    def printSolution(self):
        ll1 = SinglyLinkedList()
        ll2 = SinglyLinkedList()
        ll1.insert_values([2,4,6,8,10,12,14,16,18])
        ll2.insert_values([1,3,5,7,9,11,13,15])
        ll1.head = self.alternateMerge(ll1.head,ll2.head)
        ll1.print()
    def alternateMerge(self,head1: Node,head2: Node):
        resList = None
        res = None
        while head1 and head2:
            if head1.val <= head2.val:
                if resList is None:
                    res = head1
                    resList = res
                else:
                    res.next = head1
                    res = res.next
                head1 = head1.next
            else:
                if resList is None:
                    res = head2
                    resList = res
                else:
                    res.next = head2
                    res = res.next
                head2 = head2.next
        return resList
        
if __name__ == "__main__":
    Solution().printSolution()