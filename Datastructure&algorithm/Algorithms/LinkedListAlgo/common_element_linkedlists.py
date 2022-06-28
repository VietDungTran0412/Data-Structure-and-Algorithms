# Given two sorted linked list, given an algorithm for printing the common elements of them
from LinkedList import SinglyLinkedList
from LinkedList import Node
class Solution:
    def printSolution(self):
        ll1 = SinglyLinkedList()
        ll2 = SinglyLinkedList()
        ll1.insert_values([1,3,4,5,6,7,8,10,12,12,19,20,25,26,30,31,35])
        ll2.insert_values([2,4,6,7,8,9,10,14,16,17,20,25,31,35,39,40,50])
        res = SinglyLinkedList()
        res.head = self.commonElements(ll1.head,ll2.head)
        res.print()
        ll1.head = self.reverseRecursive(ll1.head)
        ll1.print()
    def commonElements(self,list1,list2):
        temp = Node(-1)
        head = temp
        while list1 and list2:
            if list1.val == list2.val:
                head.next = Node(list1.val)
                head = head.next
                list1 = list1.next
                list2 = list2.next
            elif list1.val > list2.val:
                list2 = list2.next
            else:
                list1 = list1.next
        return temp.next
    def reverseRecursive(self,head):
        if head is None:
            return None
        if head.next is None:
            return head
        second = head.next
        head.next = None
        rev = self.reverseRecursive(second)
        second.next = head
        return rev
        
if __name__ == "__main__":
    Solution().printSolution()