class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    
    def __init__(self):
        self.head = None
        self.size = 0
        
    def is_empty(self):
        return self.size == 0 

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def pop(self):
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        return self.head.data

s = Stack()
s.push('1')
s.push('2')
print(s.peek())
s.push('3')
print(s.peek())
s.pop()
print(s.peek())

