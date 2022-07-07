class SinglyNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None

class DoublyNode:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.prev = None

class LinkedQueue:
    def __init__(self) -> None:
        self.front = None
        self.rear = self.front
    def isEmpty(self)->bool:
        return self.front == None
    def enQueue(self,val):
        if self.isEmpty():
            self.front = SinglyNode(val)
            self.rear = self.front
            return
        self.rear.next = SinglyNode(val)
        self.rear = self.rear.next
    def deQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = self.front.next
        return temp.val
    def __repr__(self) -> str:
        if self.isEmpty():
            return "Empty Queue!"
        res = ""
        cur = self.front
        while cur:
            res += str(cur.val) + "->"
            cur = cur.next
        return res
    def getFront(self):
        if self.isEmpty():
            return None
        return self.front.val
    def getRear(self):
        if self.isEmpty():
            return None
        return self.rear.val
    def size(self)->int:
        count = 0
        cur = self.front
        while cur:
            count +=1
            cur = cur.next
        return count

class Deque:
    def __init__(self) -> None:
        self.head = None
    def isEmpty(self)->bool:
        return self.head == None
    def pushBack(self,val):
        if self.isEmpty():
            self.head = DoublyNode(val)
            self.head.prev = self.head
            self.head.next = self.head
        else:
            tail = self.head.prev
            newNode = DoublyNode(val)
            newNode.prev = tail
            newNode.next = self.head
            self.head.prev = newNode
            tail.next = newNode
    def pushFront(self,val):
        self.pushBack(val)
        self.head = self.head.prev
    def popBack(self)->any:
        data = -1
        if self.head is None:
            return data
        elif self.head.prev == self.head:
            data = self.head.val
            self.head = None
            return data
        else:
            newTail = self.head.prev.prev
            data = self.head.prev.val
            newTail.next = self.head
            self.head.prev = newTail
            return data
    def popFront(self):
        if self.head is None:
            return
        self.head = self.head.next
        return self.popBack()
    def size(self)->int:
        if self.head is None:
            return 0
        count = 1
        cur = self.head
        while cur.next != self.head:
            count +=1
            cur = cur.next
            
        return count
    def __repr__(self) -> str:
        if self.head is None:
            return "Empty Queue!"
        res = ""
        cur = self.head
        while cur.next != self.head:
            res += str(cur.val) + "->"
            cur = cur.next
        res += str(cur.val)
        return res

