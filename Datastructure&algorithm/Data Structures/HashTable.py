class HashTable:
	def __init__(self):
		self.max  = 10
		self.arr = [[] for i in range(self.max)]
	def get_hash(self,key): #get the hash
		hash = 0
		for char in key:
			hash += ord(char)
		return hash % self.max
	def __setitem__(self,key,value): #add the value and key into hash table
		h = self.get_hash(key)
		found = False

		for idx, element in enumerate(self.arr[h]):
			if len(element) == 2 and element[0] == key:
				self.arr[h][idx] = (key,value)
				found = True
				break
		if not found:
			self.arr[h].append((key,value))
	def __getitem__(self, key): #get the value based on the key
		h = self.get_hash(key)
		for element in self.arr[h]:
			if element[0] == key:
				return element[1]
	def __delitem__(self,key):
		h = self.get_hash(key)
		for idx, element in enumerate(self.arr[h]):
			if element[0] == key:
				del self.arr[h][idx]
if __name__ == '__main__':
	t = HashTable()
	t['march 6'] = 130
	t['march 6'] = 78
	t['dec 13'] = 140
	t['dec 13'] = 20
	t['Yeu Thanh An'] = 40
	t['march 17'] = 459
	del t['march 17']
	print(t.arr)
