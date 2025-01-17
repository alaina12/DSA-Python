class Node:
	def __init__(self, value):
		self.value = value
		self.next = None


class Queue:
	def __init__(self):
		self.first = None
		self.last = None
		self.length = 0

	def peek(self):
		return self.first

	def enqueue(self, value):
		new_node = Node(value)
		if self.first == None:
			self.first = new_node
			self.last = self.first
			self.length += 1
		else:
			self.last.next = new_node
			self.last = new_node
			self.length += 1

	def dequeue(self):
		temp = self.first.next
		dequeued_eleement = self.first
		if temp == None:
			self.first = None
			self.length -= 1
			return 
		self.first.enxt = None
		self.first = temp
		self.length -= 1

	def printt(self):
		temp = self.first
		while temp != None:
			print(temp.value, end = ' -> ')
			temp = temp.next
		print()
		print(self.length)

#Example usage
my_queue = Queue()
my_queue.enqueue('Ben')
my_queue.enqueue('Brent')
my_queue.enqueue('pierson')
my_queue.enqueue('Lexi')
my_queue.printt()
my_queue.dequeue()
my_queue.dequeue()
my_queue.printt()
x = my_queue.peek()
print(x)