# Implementing Stack usinf arrays

class Stack:
	def __init__(self):
		self.array = []
		self.length = 0

	def __str__(self):
		return str(self.__dict__)

	def peek(self):
		if len(self.array) > 0:
			return self.array[-1]
		return None # Return None if the stack is empty

	def push(self, value):
		self.array.append(value)
		self.length += 1
		return self # Return the stack instance for chaining

	def pop(self):
		if len(self.array) > 0:
			self.array.pop()
		self.length -=1
		return self # Return the stack instance for chaining

my_stack = Stack()
# my_stack.peek()
my_stack.push('discord')
my_stack.push('ztm')
my_stack.push('google')
# my_stack.peek()
print(my_stack)
x = my_stack.peek()
print(x)
my_stack.pop()
print(my_stack)