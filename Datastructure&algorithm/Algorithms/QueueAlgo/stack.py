class DynamicStack:
    def __init__(self) -> None:
        self.array = []
    def __str__(self) -> str:
        return f"{self.array}"
    def isEmpty(self):
        return len(self.array) == 0
    def push(self,val):
        self.array.append(val)
    def pop(self):
        if self.isEmpty():
            return
        return self.array.pop()
    def print(self):
        print(self.array)
    def size(self)->int:
        return len(self.array)
    def peek(self):
        if self.isEmpty():
            return None
        return self.array[-1]
    def insert(self,ar: list):
        for num in ar:
            self.push(num)
class StackNode:
    def __init__(self, val = 0, next = None) -> None:
        self.val = val
        self.next = next
class LinkedListStack:
    def __init__(self) -> None:
        self.head = None
    def isEmpty(self)->bool:
        return self.head == None
    def push(self,val):
        newNode = StackNode(val,self.head)
        self.head = newNode
    def pop(self):
        if self.isEmpty():
            return None
        temp = self.head
        self.head = self.head.next
        return temp.val
    def size(self)->int:
        cur = self.head
        count = 0 
        while cur:
            count +=1
            cur = cur.next
        return count
