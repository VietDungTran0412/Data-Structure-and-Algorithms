class TwoStacks:
    def __init__(self,x) -> None:
        self.capacity = x
        self.top1 = 0
        self.top2 = self.capacity-1
        self.stack = [None for i in range(self.capacity)]
    def isFull(self)->bool:
        return self.top1 == self.top2
    def push1(self,val):
        if self.isFull():
            return
        top1 = self.top1
        self.stack[top1] = val
        self.top1+=1
    def push2(self,val):
        if self.isFull():
            return
        top2 = self.top2
        self.stack[top2] = val
        self.top2 -= 1
    def isEmpty(self,stackNumber: int)->bool:
        if stackNumber == 1:
            return self.top1 == 0
        else:
            return self.top2 == self.capacity-1
    def print(self):
        print(self.stack)

