class crazyQueue:
	def __init__(self):
		self.first = []
		self.last = []

	def enqueue(self, value):
		# move all elements from first stack tp last stack
		while len(self.first) > 0:
			self.last.append(self.first.pop())
		# Add the new value to the last stack
		self.last.append(value)
		return self

	def dequeue(self):
		# Move all elements from last stack back to first stack
		while len(self.last) > 0:
			self.first.append(self.last.pop())
		# remove the top element from the stack
		if len(self.first) > 0:
			self.first.pop()
		return self

	def peek(self):
		# Rwturn the top of the stack that contains the next element to be dequeued
		if len(self.first) > 0:
			return self.first[-1]
		if len(self.last) > 0:
			return self.last[0]
		return None

my_queue = crazyQueue()
print(my_queue.peek())
print(my_queue.enqueue('ben').last)
print(my_queue.enqueue('Brent').last)
print(my_queue.enqueue('Justice').last)
print(my_queue.peek())
print('========')
print(my_queue.dequeue())
print(my_queue.dequeue())
print('========')
print(my_queue.peek())