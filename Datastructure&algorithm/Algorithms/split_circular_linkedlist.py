from LinkedList import CircularLinkedList
class Solution:
    def print_solution(self):
        ll = CircularLinkedList()
        ll.insert_values([1,2,3,4,5,6,8])
        ll.head = self.split_circular_linkedlist(ll.head)
        ll.print()
    def split_circular_linkedlist(self,head):
        # Turtoise and Rabbit approach
        if head is None:
            return None
        slow = head
        fast = head
        while fast.next != head:
            fast = fast.next.next
            slow = slow.next
        slow.next = head
        return head
if __name__ == "__main__":
    Solution().print_solution()