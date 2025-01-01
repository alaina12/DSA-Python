# implementing an array using python

class MyArray:
	def __init__(self):
		self.length = 0
		self.data = {}

	def get(self, index):
		return self.data.get(index)

	def push(self, item):
		self.data[self.length] = item
		self.length += 1
		return self.length

	def pop(self):
		if self.length == 0:
			return None
		last_item = self.data[self.length - 1]
		del self.data[self.length - 1]
		self.length -= 1
		return last_item

	def delete(self, index):
		if index >=  self.length or index < 0:
			return None
		item = self.data[index]
		self.shift_items(index)
		return item

	def shift_items(self, index):
		for i in range(index, self.length -1):
			self.data[i] = self.data[i+1]
		del self.data[self.length -1]
		self.length -= 1


#example usage
new_array = MyArray()
new_array.push('hi')
new_array.push('you')
new_array.push('!')
new_array.delete(0)
new_array.push('are')
new_array.push('nice')
new_array.delete(1)
print(new_array.data)
print(new_array)