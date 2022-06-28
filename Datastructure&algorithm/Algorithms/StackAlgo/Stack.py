class ArrayStack:
    def __init__(self,capacity) -> None:
        self.top = -1
        self.capacity = capacity
        self.ar = [-1 for i in range(capacity)]
class CreateDynStack:
    def __init__(self,len) -> None:
        self.stack = ArrayStack(len)
    def isFullStack(self):
        return self.stack.top == self.stack.capacity-1
    def doubleStack(self):
        self.stack.capacity *= 2
    def push(self,val):
        if self.isFullStack():
            self.doubleStack()
        self.stack.top +=1
        top = self.stack.top
        self.stack.ar[top] = val
    def isEmptyStack(self):
        return self.stack.top == -1
    def pop(self):
        if self.isEmptyStack():
            return -1
        self.stack.top -= 1
        top = self.stack.top
        return self.stack.ar[top+1]
    def size(self):
        return (self.stack.top+1)
    def print(self):
        print(self.stack.ar)


