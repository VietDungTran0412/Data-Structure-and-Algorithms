class Node:
	def __init__(self,val,next = None,prev = None) -> None:
		self.val = val
		self.next = next
		self.prev = prev
class DoublyCircularLinkedList:
	def __init__(self) -> None:
		self.head = None
	def append(self,data):
		if self.head is None:
			self.head = Node(data)
			self.head.next = self.head
			self.head.prev = self.head
		else:
			itr = self.head
			while itr.next != self.head:
				itr = itr.next
			node = Node(data)
			itr.next = node
			node.prev = itr
			node.next = self.head
			self.head.prev = node
	def prepend(self,data):
		if self.head is None:
			self.head = Node(data)
			self.head.next = self.head
			self.head.prev = self.head
		else:
			itr = self.head
			while itr.next != self.head:
				itr = itr.next
			node = Node(data)
			itr.next = node
			node.prev = itr
			node.next = self.head
			self.head.prev = node
			self.head = node
	def print(self):
		if self.head is None:
			print(None)
		itr = self.head
		while itr.next != self.head:
			print(f"<-{itr.val}->",end="")
			itr = itr.next
		print()
	def length(self)->int:
		if self.head is None:
			return 0
		count  = 0
		itr = self.head
		while itr.next != self.head:
			count+=1
			itr = itr.next
		return count
	def convert_array(self,nums):
		for num in nums:
			self.append(num)
	def delete(self,val):
		if self.head.val == val:
			self.head = self.head.next
		itr = self.head
		while itr.next != self.head:
			if itr.next.val == val:
				temp = itr.next.next
				itr.next = temp
				temp.prev = itr
			else:
				itr = itr.next

if __name__ == "__main__":
	llist = DoublyCircularLinkedList()
	llist.convert_array([1,6,2,3,7,4])
	llist.prepend(5)
	llist.delete(5)
	llist.print()
	print(llist.length())
		

