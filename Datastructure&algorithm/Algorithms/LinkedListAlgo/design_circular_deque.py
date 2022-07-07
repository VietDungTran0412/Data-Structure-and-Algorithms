class Node:
    def __init__(self,val) -> None:
        self.val = val
        self.next = None
        self.prev = None
class CircularDeque:
    def __init__(self,k) -> None:
        self.head = None
        self.capacity = k
        self.size = 0
    def isFull(self)->bool:
        return self.size == self.capacity
    def isEmpty(self)->bool:
        return self.size == 0
    def getFront(self)->int:
        if self.isEmpty():
            return -1
        return self.head.val
    def getRear(self)->int:
        if self.isEmpty():
            return -1
        return self.head.prev.val
    def insertFront(self,value)->bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = Node(value)
            self.head.next = self.head
            self.head.prev = self.head
            self.size += 1
            return True
        node = Node(value)
        cur = self.head.prev
        cur.next = node
        node.prev = cur
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
        return True
    def insertLast(self,value)->bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.head = Node(value)
            self.head.next = self.head
            self.head.prev = self.head
            self.size += 1
            return True
        cur = self.head.prev
        node = Node(value)
        cur.next = node
        node.prev = cur
        node.next = self.head
        self.head.prev = node
        self.size +=1
        return True
    def deleteFront(self)->bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            self.size -=1
            return True
        cur = self.head.prev
        self.head = self.head.next
        cur.next = self.head
        self.head.prev = cur
        self.size -=1
        return True
    def deleteLast(self)->bool:
        if self.isEmpty():
            return False
        if self.size == 1:
            self.head = None
            return True
        cur = self.head.prev.prev
        cur.next = self.head
        self.head.prev = cur
        self.size -=1
        return True
obj = CircularDeque(3)
res = [obj.insertFront(8)
        ,obj.getFront(),obj.isEmpty(),obj.deleteFront()
        ,obj.insertLast(10),
        obj.insertFront(4),obj.deleteLast(),obj.isEmpty()]
print(obj.size)
print(res)