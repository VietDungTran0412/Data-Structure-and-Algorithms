class Node:
	def __init__(self,data):
		self.data = data
		self.next = None
class CircularLinkedList:
	def __init__(self):
		self.head = None
	
	def append(self,val):
		if self.head is None:
			self.head = Node(val)
			self.head.next = self.head
		else:
			node = Node(val)
			itr = self.head
			while itr.next != self.head:
				itr = itr.next
			itr.next = node
			node.next = self.head

	def prepend(self,val):
		node = Node(val)
		itr = self.head
		node.next = self.head
		if self.head is None:
			node.next = node
		else:
			while itr.next != self.head:
				itr = itr.next
			itr.next = node 
		self.head = node

	def print_list(self):
		itr = self.head
		while itr:
			print(str(itr.data),end="-->")
			itr = itr.next
			if itr == self.head:
				break
def insert_at_end(head,val):
	if head is None:
		head = Node(val)
		head.next = head
		return head
	itr = head
	node = Node(val)
	while itr.next != head:
		itr = itr.next
	itr.next = node
	node.next = head
	return head

def printLinkedList(head):
	itr = head
	while itr.next != head:
		print(itr.data,end="-->")
		itr = itr.next
	print(head.data)

def getLength(head):
	count = 0
	itr = head
	while itr.next != head:
		count +=1
		itr = itr.next
	return count
if __name__ == "__main__":
	llist = CircularLinkedList()
	llist.head = insert_at_end(llist.head,9)
	llist.head = insert_at_end(llist.head,4)
	llist.head = insert_at_end(llist.head,7)
	llist.head = insert_at_end(llist.head,12)
	printLinkedList(llist.head)
	print(getLength(llist.head))