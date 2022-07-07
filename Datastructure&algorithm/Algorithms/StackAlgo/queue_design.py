from stack import DynamicStack
class Queue:
    def __init__(self) -> None:
        self.stack = DynamicStack()
    def enqueue(self,val):
        if self.isEmpty():
            self.stack.push(val)
            return
        temp = self.stack.pop()
        self.enqueue(val)
        self.stack.push(temp)
    def dequeue(self)->int:
        if self.isEmpty():
            return
        return self.stack.pop()
    def isEmpty(self)->bool:
        return self.stack.isEmpty()
    def size(self)->int:
        return self.stack.size()
    def rear(self):
        return self.stack.peek()
    def front(self):
        temp = self.stack.pop()
        self.stack.push(temp)
        return temp
q = Queue()
q.enqueue(5)
q.enqueue(10)
print(q.front())
print(q.stack)