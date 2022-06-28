from numpy import size


class TwoStacks:
    def __init__(self,size) -> None:
        self.capacity = size
        self.ar = [None for i in range(size)]
        self.top1 = -1
        self.top2 = self.capacity
    def push1(self,val):
        if self.top1 == self.top2 - 1:
            return
        


