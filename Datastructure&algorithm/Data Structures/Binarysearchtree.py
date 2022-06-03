class BinarySearchTreeNode:
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None
	def add_child(self,data):
		if data == self.data:
			return 
		if data < self.data:
			#add data in left subtree
			if self.left:
				self.left.add_child(data)
			else:
				self.left = BinarySearchTreeNode(data)
		else:
			#add data in right subtree
			if self.right:
				self.right.add_child(data)
			else:
				self.right = BinarySearchTreeNode(data)

	def in_order_traversal(self):
		elements = []

		#visit left tree first
		if self.left:
			elements += self.left.in_order_traversal()
		
		#visit the base node
		elements.append(self.data)
		#visit right
		if self.right:
			elements += self.right.in_order_traversal()

		return elements
	def search(self,val):
		if self.data == val:
			return True
		if val < self.data:
			#val might be in left subtree
			if self.left:
				return self.left.search(val)
			else:
				return False

		if val > self.data:
			#val might me in right subtree
			if self.right:
				return self.right.search(val)
			else:
				return False
	def find_max(self):
		if self.right is None:
			return self.data
		return self.right.find_max()
	def find_min(self):
		if self.left is None:
			return self.data
		return self.left.find_min()
	def calc_sum(self):
		right_sum = 0
		left_sum = 0
		if self.left:
			left_sum += self.left.calc_sum()
		else:
			left_sum += 0
		if self.right:
			right_sum += self.right.calc_sum()
		else:
			right_sum += 0
		return right_sum +left_sum + self.data
	def pre_order_traversal(self):
		elements = []
		elements.append(self.data)
		
		if self.left:
			elements += self.left.pre_order_traversal()
		if self.right:
			elements += self.right.pre_order_traversal()
		return elements
	def post_order_traversal(self):
		elements = []
		
		if self.left:
			elements += self.left.pre_order_traversal()
		if self.right:
			elements += self.right.pre_order_traversal()
		elements.append(self.data)
		return elements
	def delete(self,val):
		if val < self.data:
			if self.left:
				self.left = self.left.delete(val)
			else:
				return None
		elif val > self.data:
			if self.right:
				self.right = self.right.delete(val)
			else:
				return None
		else:
			if self.left is None and self.right is None:
				return None
			if self.left is None:
				return self.right
			if self.right is None: 
				return self.right
			min_val = self.right.find_min()
			self.data = min_val
			self.right = self.right.delete(min_val)
		return self
class Solution:
	def bstToGst(self,root):
		pass

def build_tree(elements):
	root = BinarySearchTreeNode(elements[0])
	for i in range(1,len(elements)):
		root.add_child(elements[i])
	return root

def main():
	numbers = [4,1,6,0,2,5,7,3,8]
	numbers_tree = build_tree(numbers)
	print(numbers_tree.in_order_traversal())
main()






