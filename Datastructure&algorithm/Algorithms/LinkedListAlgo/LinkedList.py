from multiprocessing.dummy import Array
from typing import List


class Node:
    def __init__(self,x) -> None:
        self.val = x
        self.next = None
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None
    def append(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)
    def insert_values(self,ar: List):
        for element in ar:
            self.append(element)
    def print(self):
        if self.head is None:
            print("Empty list!!!")
        else:
            temp = self.head
            while temp:
                print(temp.val,end="-->")
                temp = temp.next
            print()
class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            node = Node(data)
            node.next = self.head
            temp.next = node
    def insert_values(self,ar):
        for element in ar:
            self.append(element)
    def print(self):
        if self.head is None:
            print("Empty list!!!")
        else:
            temp = self.head
            while temp.next != self.head:
                print(temp.val,end="-->")
                temp = temp.next
            print(temp.val)
