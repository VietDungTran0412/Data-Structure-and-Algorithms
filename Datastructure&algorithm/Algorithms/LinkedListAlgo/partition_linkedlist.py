from LinkedList import Node, SinglyLinkedList
class Solution:
    def printSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([2,5,4,3,6,3])
        ll.head = self.partitionLinkedList(ll.head,4)
        ll.print()
    def partitionLinkedList(self,head:Node,x:int):
        lesserHead = None
        lesser = None
        greaterHead = None
        greater = None
        while head:
            if head.val < x:
                if lesserHead is None:
                    lesser = head
                    lesserHead = lesser
                else:
                    lesser.next = head
                    lesser = lesser.next
            else:
                if greaterHead is None:
                    greater = head
                    greaterHead = greater
                else:
                    greater.next = head
                    greater = greater.next
            head = head.next
        lesser.next = greaterHead
        greater.next = None
        return lesserHead
if __name__ == "__main__":
    Solution().printSolution()