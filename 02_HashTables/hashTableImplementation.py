class HashTable:
	def __init__(self, size):
		self.data = [None] * size

	#private method to calculate the hash of a key
	def _hash(self, key):
		hash_value = 0
		for i in range(len(key)):
			# ord() is used to get the ASCII value of a character
			hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
		return hash_value

	# method to set a key-value pair
	def set(self, key, value):
		address = self._hash(key)
		if not self.data[address]:
			self.data[address] = []
		self.data[address].append([key, value])

	# Method to get the value for a given key
	def get(self, key):
		address = self._hash(key)
		current_bucket = self.data[address]
		if current_bucket:
			for pair in current_bucket:
				if pair[0] == key:
					return pair[1]
		return None

my_hash_table = HashTable(50)
my_hash_table.set('grapes', 10000) 
print(my_hash_table.get('grapes'))# output: 10000
my_hash_table.set('apples',9)
print(my_hash_table.get('apples')) # output: 9