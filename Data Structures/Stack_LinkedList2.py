class Stack:
    def __init__(self, head):
        self.head = head

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        value = self.head.data
        self.head = self.head.next
        return value

    def peek(self):
        return self.head.data 

    def isEmpty(self):
        return print(self.head is None)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
