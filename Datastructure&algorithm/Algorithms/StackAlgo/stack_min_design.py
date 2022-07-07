from stack import DynamicStack
class AdvancedStack:
    def __init__(self) -> None:
        self.elementStack = DynamicStack()
        self.minStack = DynamicStack()
    def isEmpty(self)->bool:
        return self.elementStack.isEmpty()
    def push(self,val):
        self.elementStack.push(val)
        if self.minStack.isEmpty():
            self.minStack.push(val)
        else:
            if val <= self.minStack.top():
                self.minStack.push(val)
    def pop(self):
        if self.elementStack.isEmpty():
            return
        temp = self.elementStack.pop()
        if temp == self.minStack.peek():
            return self.minStack.pop()
        return temp
    def getMinimum(self)->int:
        return self.minStack.peek()
