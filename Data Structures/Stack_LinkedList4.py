class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)

class Stack:
    
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def push(self, value):
        if self.is_empty():
            self.head = Node(value)
        else:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
        self.size += 1
        
    def pop(self):
        if self.is_empty():
            return 'Stack is empty!'
        else:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value

    def peek(self):
        if self.is_empty():
            return 'Stack is empty!'
        else:
            return self.head.data

    def is_empty(self):
        return self.head is None


s = Stack()
s.push(30)
s.push(2)
print(len(s))
