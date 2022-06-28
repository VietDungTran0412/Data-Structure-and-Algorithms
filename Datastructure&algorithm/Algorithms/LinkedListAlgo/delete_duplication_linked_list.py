from LinkedList import SinglyLinkedList, Node
class Solution:
    def printSolution(self):
        ll = SinglyLinkedList()
        ll.insert_values([1,2,3,4,5])
        ll.head = self.reverseBetween(ll.head,2,4)
        ll.print()
    def deleteDuplicates(self,head: Node) -> Node:
        if head is None:
            return head
        newNode = Node(-1)
        newNode.next = head
        cur = newNode
        temp = head
        dup = set()
        while temp.next:
            if temp.val in dup:
                temp = temp.next
                cur.next = cur.next.next
                continue
            if temp.val == temp.next.val:
                dup.add(temp.val)
                temp = temp.next
                cur.next = cur.next.next
            else:
                cur = cur.next
                temp = temp.next
        if temp.val in dup:
            cur.next = cur.next.next
        return newNode.next
    def getKthNode(self,head: Node, k: int)-> Node:
        i = 1
        while head and i < k:
            head = head.next
            i+=1
        return head
    def reverseBetween(self,head: Node, left: int, right: int)-> Node:
        if head is None:
            return head
        cur = head
        for i in range(left-1):
            cur = cur.next
        prev = self.getKthNode(head,right+1)
        for j in range(right-left+1):
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        if left == 1:
            return prev
        else:
            end = self.getKthNode(head,left-1)
            end.next = prev
            return head

if __name__ == "__main__":
    Solution().printSolution()