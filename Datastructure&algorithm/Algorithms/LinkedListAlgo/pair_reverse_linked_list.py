from LinkedList import SinglyLinkedList
# Input: 1-2-3-4-5-6-7-8
# Output: 2-1-4-3-6-5-8-7
class Solution:
    def pair_reverse(self,head):
        cur = head
        temp1 = None
        temp2 = None
        while cur:
            if temp1 != None:
                temp1.next.next = cur.next
            temp1 = cur.next
            cur.next = cur.next.next
            temp1.next = cur
            if temp2 is None:
                temp2 = temp1
            cur = cur.next
        return temp2
    def pair_reverse_recursive(self,head):
        if head is None:
            return None
        if head.next is None:
            return head
        prev = head.next
        head.next = prev.next
        prev.next = head
        head.next = self.pair_reverse_recursive(head.next)
        return prev
        

if __name__ == "__main__":
    ll = SinglyLinkedList()
    ll.insert_values([1,2])
    solve = Solution()
    ll.head = solve.pair_reverse_recursive(ll.head)
    ll.print()


