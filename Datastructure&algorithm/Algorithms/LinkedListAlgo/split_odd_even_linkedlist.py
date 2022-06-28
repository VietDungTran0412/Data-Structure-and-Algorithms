from LinkedList import SinglyLinkedList

class Solution:
    def printSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([1,2,3,4,5,6])
        ll.head = self.segregateEvenOdd(ll.head)
        ll.print()
    def segregateEvenOdd(self,head):
        if head is None:
            return None
        cur = head
        oddStart = None
        oddEnd = None
        evenStart = None
        evenEnd = None
        while cur:
            val = cur.val
            if val % 2 == 1:
                if oddStart is None:
                    oddStart = cur
                    oddEnd = oddStart
                else:
                    oddEnd.next = cur
                    oddEnd = oddEnd.next
            if val % 2 == 0:
                if evenStart is None:
                    evenStart = cur
                    evenEnd = evenStart
                else:
                    evenEnd.next = cur
                    evenEnd = evenEnd.next
            cur = cur.next
        if oddStart is None:
            return evenStart
        if evenStart is None:
            return oddStart

        evenEnd.next = oddStart
        oddEnd.next = None
        return evenStart
if __name__ == "__main__":
    Solution().printSolution()