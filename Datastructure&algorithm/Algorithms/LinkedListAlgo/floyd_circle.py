class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def prepend(self,val):
        node = Node(val)
        node.next = self.head
        self.head = node
    def print(self):
        if self.head is None:
            print("Empty")
        else:
            itr = self.head
            while itr:
                print(itr.val,end="-->")
                itr = itr.next
            print()
    def insert_values(self,nums):
        for num in nums:
            self.prepend(num)
    def add_cycle(self):
        n = 4
        count = 0
        temp = None
        itr = self.head
        while itr.next:
            count +=1
            if count ==n:
                temp = itr
            itr = itr.next
        itr.next = temp
    def floyd_circle(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                return True
        return False
    def get_start_cycle(self):
        fast = self.head
        slow = self.head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if self.floyd_circle:
            slow = self.head
            while slow != fast:
                slow = slow.next
                fast = fast.next
            return slow
    def detect_cycle(self):
        temp = self.get_start_cycle()
        itr = temp
        while itr.next != temp:
            itr = itr.next
        itr.next = None
    def get_length_cycle(self):
        count = 0
        temp = self.get_start_cycle()
        itr = temp
        while itr.next != temp:
            count +=1
            itr = itr.next
        return count

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_values([1,5,2,8,6,9,10,5,4,7,2,7])
    ll.print()
    ll.add_cycle()
    print(ll.floyd_circle())
    print(ll.get_length_cycle())
    ll.detect_cycle()
    ll.print()
            