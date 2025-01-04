class Node:
	def __init__(self,value):
		self.value = value
		self.next = None

class LinkedList:
	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length = 1

	def append(self, value):
		new_node = Node(value)
		self.tail.next = new_node
		self.tail = new_node
		self.length += 1
		return self

	def prepnd(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head = new_node
		self.length += 1
		return self

	def print_list(self):
		array = []
		current_node = self.head
		while current_node is not None:
			array.append(current_node.value)
			current_node = current_node.next
		return array

	def insert(self, index, value):
		if index >= self.length:
			self.append(value)
			return self.print_list()

		new_node = Node(value)
		leader = self.traverse_to_index(index-1)
		holding_pointer = leader.next
		leader.next = new_node
		new_node.next = holding_pointer
		self.length += 2
		return self.print_list()

	def traverse_to_index(self, index):
		counter = 0
		current_node = self.head
		while counter != index:
			current_node = current_node.next
			counter += 1
		return current_node
	def remove(self, index):
		leader = self.traverse_to_index(index-1)
		unwanted_node = leader.next
		leader.next = unwanted_node.next
		self.length -= 1
		return self.print_list()

my_linked_list = LinkedList(10)
print(my_linked_list.print_list())
print(my_linked_list.append(5).print_list())
print(my_linked_list.append(16).print_list())
print(my_linked_list.prepnd(1).print_list())
print(my_linked_list.insert(2,99))
print(my_linked_list.remove(2))
print(my_linked_list.print_list())