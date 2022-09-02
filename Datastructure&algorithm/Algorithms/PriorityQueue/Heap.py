
class MaxHeap:
    def __init__(self,size) -> None:
        self.ar = [None for i in range(size)]
        self.length = 0
        self.capacity = size
    def __parent(self,pos: int)->int:
        if pos <= 0 or pos >= self.length:
            return -1
        return (pos-1)//2
    def __leftChild(self,pos: int)->int:
        left = 2*pos+1
        if left >= self.length:
            return -1
        return left
    def __rightChild(self,pos: int)->int:
        right = 2*pos+2
        if right >= self.length:
            return -1
        return right
    def getMax(self):
        if self.length == 0:
            return -1
        return self.ar[0]
    def percolateDown(self,pos):
        l = self.__leftChild(pos)
        r = self.__rightChild(pos)
        if l != -1 and self.ar[l] > self.ar[pos]:
            max = l
        else:
            max = pos
        if r!= -1 and self.ar[r] > self.ar[max]:
            max = r
        if max != pos:
            self.ar[pos], self.ar[max] = self.ar[max], self.ar[pos]
            self.percolateDown(max)
    def delete(self):
        if self.length == 0:
            return -1
        data = self.ar[0]
        self.ar[0] = self.ar[self.length-1]
        self.ar[self.length-1] = None
        self.length-=1
        self.percolateDown(0)
        return data
    def insert(self,val):
        if self.length == self.capacity:
            return
        self.length +=1
        i = self.length-1
        self.ar[i] = val
        while i !=0:
            parent = self.__parent(i)
            if self.ar[i] > self.ar[parent]:
                self.ar[i], self.ar[parent] = self.ar[parent], self.ar[i]
                i = parent
            else:
                break
    def convertArToHeap(self,nums: list[int]):
        for num in nums:
            self.insert(num)
class MinHeap:
    def __init__(self,size) -> None:
        self.ar = [None for i in range(size)]
        self.length = 0
        self.capacity = size
    def __parent(self,pos: int)->int:
        if pos <= 0 or pos >= self.length:
            return -1
        return (pos-1)//2
    def __leftChild(self,pos: int)->int:
        left = 2*pos+1
        if left >= self.length:
            return -1
        return left
    def __rightChild(self,pos: int)->int:
        right = 2*pos+2
        if right >= self.length:
            return -1
        return right
    def getMin(self):
        if self.length == 0:
            return -1
        return self.ar[0]
    def percolateDown(self,pos):
        l = self.__leftChild(pos)
        r = self.__rightChild(pos)
        if l != -1 and self.ar[l] < self.ar[pos]:
            min = l
        else:
            min = pos
        if r!= -1 and self.ar[r] < self.ar[min]:
            min = r
        if min != pos:
            self.ar[pos], self.ar[min] = self.ar[min], self.ar[pos]
            self.percolateDown(min)
    def delete(self):
        if self.length == 0:
            return -1
        data = self.ar[0]
        self.ar[0] = self.ar[self.length-1]
        self.ar[self.length-1] = None
        self.length-=1
        self.percolateDown(0)
        return data
    def insert(self,val):
        if self.length == self.capacity:
            return
        self.length +=1
        i = self.length-1
        self.ar[i] = val
        while i !=0:
            parent = self.__parent(i)
            if self.ar[i] < self.ar[parent]:
                self.ar[i], self.ar[parent] = self.ar[parent], self.ar[i]
                i = parent
            else:
                break
    def convertArToHeap(self,nums: list[int]):
        for num in nums:
            self.insert(num)
class Parent:
    def __init__(self,val) -> None:
        self.val = val
    def print_value(self):
        print(self.val)

class Child(Parent):
    def __init__(self, val) -> None:
        super().__init__(val)

