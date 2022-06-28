class Node:
    def __init__(self,length) -> None:
        self.length = length
        self.ar = [0 for i in range(self.length)]
        self.next = None
class UnrolledLinkedList:
    def __init__(self,n) -> None:
        self.head = None
        self.length = n
    def append(self,val):
        if self.head is None:
            node = Node(self.length)
            node.ar[0] = val
            self.head = node
        else:
            while itr.next:
                itr = itr.next
            for i in range(itr.length):
                if itr.ar[i] == None:
                    itr.ar[i] = val
                    break
            else:
                node = Node(self.length)
                node.ar[0] = val
                itr.next = node
    def insert_values(self,ar):
        for num in ar:
            self.append(num)
    def print(self):
        itr = self.head
        while itr:
            print(itr.ar, end = "-->")
            itr = itr.next
if __name__ == "__main__":
    ll = UnrolledLinkedList(5)
    ll.append(5)
    ll.append(6)
    # ll.insert_values([1,2,3,7,9,12])
    ll.print()

