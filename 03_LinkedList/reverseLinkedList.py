class Node:
    def __init__(self, value):
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

    def prepend(self, value):
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
        print(array)

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)

        new_node = Node(value)
        leader = self.traverse_to_index(index - 1)
        holding_pointer = leader.next
        leader.next = new_node
        new_node.next = holding_pointer
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
        leader = self.traverse_to_index(index - 1)
        unwanted_node = leader.next
        leader.next = unwanted_node.next
        self.length -= 1
        return self.print_list()

    def reverse(self):
        if not self.head.next:
            return self.head

        first = self.head
        self.tail = self.head
        second = first.next

        while second:
            temp = second.next
            second.next = first
            first = second
            second = temp

        self.head.next = None
        self.head = first
        return self.print_list()


# Example usage
my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.prepend(1)
my_linked_list.print_list()
my_linked_list.insert(2, 99)
my_linked_list.insert(20, 88)
my_linked_list.print_list()
my_linked_list.remove(2)
my_linked_list.reverse()
