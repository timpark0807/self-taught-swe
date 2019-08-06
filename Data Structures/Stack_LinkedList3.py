class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
    
head = Node('1')
s = Stack(head)
print(s.peek())
s.push('2')
print(s.peek())
s.push('3')
print(s.peek())
s.pop()
print(s.peek())

