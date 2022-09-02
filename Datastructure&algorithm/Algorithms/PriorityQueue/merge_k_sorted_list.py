from heapq import heapify
class Node:
    def __init__(self,val, next = None) -> None:
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            return
        cur = self.head 
        while cur.next:
            cur = cur.next
        cur.next = Node(val)
    def insert_values(self,nums):
        for num in nums:
            self.insert(num)
    def print(self):
        if self.head is None:
            print("")
            return
        cur = self.head
        while cur:
            print(cur.val,end="->")
            cur = cur.next
        print()
class MinHeap:
    def __init__(self,maxsize) -> None:
        self.ar = [None]*maxsize
        self.length = 0
        self.capacity = maxsize
    def parent(self,pos):
        if pos >= self.length or pos <= 0:
            return -1
        return (pos-1)//2
    def left_child(self,pos):
        left = 2*pos+1
        if left >= self.length:
            return -1
        return left
    def right_child(self,pos):
        right = 2*pos +2
        if right >= self.length:
            return -1
        return right
    def percolate_down(self,pos):
        l = self.left_child(pos)
        r = self.right_child(pos)
        if l != -1 and self.ar[l].val < self.ar[pos].val:
            min = l
        else:
            min = pos
        if r!= -1 and self.ar[r].val < self.ar[min].val:
            min = r
        if min != pos:
            self.ar[pos], self.ar[min] = self.ar[min], self.ar[pos]
            self.percolate_down(min)
    def delete(self):
        if self.length == 0:
            return -1
        temp = self.ar[0]
        self.ar[0] = self.ar[self.length-1]
        self.ar[self.length-1] = None
        self.length-=1
        self.percolate_down(0)
        return temp

    def insert(self,node):
        if self.length == self.capacity:
            return
        self.length +=1
        i = self.length-1
        self.ar[i] = node
        while i != 0:
            parent = self.parent(i)
            if self.ar[i].val < self.ar[parent].val:
                self.ar[i], self.ar[parent] = self.ar[parent], self.ar[i]
                i = parent
            else:
                break

class Solution:
    def print_solution(self):
        nums = [[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]
        ll1 = LinkedList()
        ll1.insert_values([-8,-7,-7,-5,1,1,3,4])
        ll2 = LinkedList()
        ll2.insert_values(nums[1])
        ll3 = LinkedList()
        ll3.insert_values(nums[2])
        ll4 = LinkedList()
        ll4.insert_values(nums[3])
        listLL =  [ll1.head,ll2.head,ll3.head,ll4.head]
        ll1.head = self.mergeArrays(listLL)
        ll1.print()
    def mergeArrays(self,lists: list[Node]):
        if len(lists) == 0:
            return None
        dummy = Node(-1)
        cur = dummy
        heap = MinHeap(len(lists))
        for i in range(len(lists)):
            if lists[i]:
                heap.insert(lists[i])
        while heap.length != 0:
            temp = heap.delete()
            cur.next = temp
            cur = cur.next
            if temp and temp.next:
                heap.insert(temp.next)
        cur.next = None
        return dummy.next

Solution().print_solution()

        
