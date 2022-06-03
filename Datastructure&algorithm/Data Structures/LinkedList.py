class Node:
	def __init__(self, data =None, next = None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None

	def insert_at_begining(self,data):
		node = Node(data,self.head)
		self.head = node
	def print(self):
		if self.head is None:
			print('LinkedList is empty')
			return
		itr = self.head
		llstr = ''
		while itr:
			llstr += str(itr.data) + '-->'
			itr = itr.next
		print(llstr)
	def insert_at_end(self,data):
		if self.head is None:
			self.head = Node(data,None)
			return

		itr = self.head
		while itr.next:
			itr = itr.next
		itr.next = Node(data,None)
	def insert_values(self,data_list):
		self.head = None
		for data in data_list:
			self.insert_at_end(data)
	def get_length(self):
		count = 0 
		itr = self.head
		while itr:
			count +=1
			itr = itr.next
		return count
	def remove_at(self, index):
		if index < 0 or index>= self.get_length():
			raise Exception('Invalid index')
		if index ==0:
			self.head = self.head.next
			return
		count = 0 
		itr = self.head
		while itr:
			if count == index -1 :
				itr.next = itr.next.next
				break
			itr = itr.next
			count += 1
	def insert_at(self,index,data):
		if index < 0 or index >= self.get_length():
			raise Exception('Invalid index')
		if index == 0:
			self.insert_at_begining(data)
			return
		count = 0
		itr = self.head
		while itr:
			if count == index -1:
				node = Node(data,itr.next)
				itr.next = node
				break
			itr = itr.next
			count +=1
	def reverse(self):
		itr = self.head
		prev = None
		while itr :
			temp = itr.next
			itr.next = prev
			prev = itr  
			itr = temp
		self.head = prev
	def mergeNodes(self):
		itr = self.head
		sum = Node(0,None)
		ans = Node(0,sum)
		while itr:
			if itr.data and itr.next:
				sum.next = Node(0,None)
				sum = sum.next
			sum.data += itr.data
			itr = itr.next
		return ans.next.next
	def convert(self):
		itr = self.head
		for i in range(2):
			itr = itr.next
		return itr
	#Merge sort in linked list
	def get_middle(self,head):
		if head is None:
			return head
		slow = head
		fast = head
		while fast.next and fast.next.next:
			slow = slow.next
			fast = fast.next
		return slow
	def sortedMerge(self,ll1,ll2):
		if ll1 is None:
			return ll2
		if ll2 is None:
			return ll1
		if ll1.data < ll2.data:
			temp = ll1
			temp.next = self.sortedMerge(ll1.next,ll2)
		else:
			temp = ll2
			temp.next = self.sortedMerge(ll1,ll2.next)
		return temp

	def mergeSort(self,head):
		if head is None or head.next is None:
			return head
		middle = self.get_middle(head)
		head2 = middle.next

		middle.next = None
		left = self.mergeSort(head)
		right = self.mergeSort(head2)
		final_list = self.sortedMerge(left,right)
		return final_list
if __name__ == '__main__':
	ll = LinkedList()
	ll.insert_at_begining(5)
	ll.insert_at_begining(82)
	ll.insert_at_end(19)
	ll.insert_at_end(21)
	ll.insert_at_end(15)
	ll.head = ll.mergeSort(ll.head)
	ll.print()

	ll2 = LinkedList()
	ll2.insert_values(['Hello','World','Chemical','Math'])
	ll2.remove_at(1)
	ll2.insert_at(2,'Yeu Thanh An')
	ll2.reverse()
	ll2.print()

	ll3 = LinkedList()
	ll3.insert_values([1,2,3,4,5,6])
	



