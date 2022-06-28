from LinkedList import CircularLinkedList

class Solution:
    def printSolution(self):
        ll = CircularLinkedList()
        n = 4
        ll.insert_values([x for x in range(n)])
        self.getJosephusPosition(n,4,ll.head)
    def getJosephusPosition(self,n,m,head):
        temp = head
        for i in range(n):
            for j in range(m):
                temp = temp.next
            temp.next = temp.next.next
        print(f"The last person stand left: {temp.val}")
if __name__ == "__main__":
    Solution().printSolution()