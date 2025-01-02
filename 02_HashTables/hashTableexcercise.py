class HashTable:
	def __init__(self, size):
		self.data = [None] * size

	# Private method for hashing keys
	def _hash(self, key):
		hash_value = 0
		for i in range(len(key)):
			#ord() rerurns the unicode code point of the charater
			hash_value = (hash_value + ord(key[i]) * i) % len(self.data)
		return hash_value

	# Method to set a key-value pair in the hash table
	def set(seelf, key, value):
		address = self._hash(key)
		if not self.data[address]:
			self.data[address] = []
		self.data[address].apppend([key, value])

	# Methof to get a value by key from the hash table
	def get(self, key):
		address = self._hash(key)
		current_bucket = self.data[address]
		if current_bucket:
			for pair in current_bucket:
				if pair[0] == key:
					return pair[1]
		return None


myHashTable = HashTable(50)
myHashTable.set('grapes', 10000)
print(myHashTable.get('grapes')) # output: 10000
myHashTable.set('apples', 9)
print(myHashTable.get('apples')) # output: 9