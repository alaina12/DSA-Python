class Node:
	def __init__(self, value):
		self.value = value
		self.prev = None
		self.next = None

class DoublyLinkedList:
	def __init__(self, value):
		new_node = Node(value)
		self.head = new_node
		self.tail = new_node
		self.length = 1

	def append(self, value):
		new_node = Node(value)
		new_node.prev = self.tail
		self.tail.next = new_node
		self.tail = new_node
		self.length += 1
		return self

	def prepend(self, value):
		new_node = Node(value)
		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node
		self.length += 2
		return self

	def print_list(self):
		array = []
		current_node = self.head
		while current_node is not None:
			array.append(current_node.value)
			current_node = current_node.next
		print(array)

	def insert(self, index, value):
		if index >= self.length:
			return self.append(value)

		new_node = Node(value)
		leader = self.traverse_to_index(index-1)
		follower = leader.next
		leader.next = new_node
		new_node.prev = leader
		new_node.next = follower
		if follower:
			follower.prev = new_node
		self.length += 1
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
		if unwanted_node.next:
			unwanted_node.next.prev = leader
		self.length -=1
		return self.print_list()

# Example usage
my_linked_list = DoublyLinkedList(10)
print(my_linked_list.append(5))
print(my_linked_list.append(16))
print(my_linked_list.prepend(1))
print(my_linked_list.print_list())
print(my_linked_list.insert(2, 99))
# Uncomment to test removal or further inserts
# my_linked_list.remove(2)