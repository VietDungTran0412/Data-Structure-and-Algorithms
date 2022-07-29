class ListNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.random = None
class Solution:
    def result(self):
        head = ListNode(10)
        head.next = ListNode(20)
        head.random = head.next
        head.next.random = head
        head.next.next = ListNode(30)
        head.next.next.random = head.next
        newHead = self.cloneExtraSpace(head)
        return newHead
    def cloneExtraSpace(self,head: ListNode):
        if head is None:
            return None
        hm = {}
        cur = head
        while cur:
            hm[cur] = ListNode(cur.val)
            cur = cur.next
        cur = head
        while cur:
            temp = hm[cur]
            if cur.next in hm:
                temp.next = hm[cur.next]
            if cur.random in hm:
                temp.random = hm[cur.random]
            cur = cur.next
        return hm[head]
Solution().result()