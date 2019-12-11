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
        new = Node(value)
        if self.head is None:
            self.head = new
        else:
            new.next = self.head
            self.head = new
        self.size += 1

    def pop(self):
        value = self.head
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        return self.head


class Queue:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1

    def dequeue(self):
        value = self.head
        self.head = self.head.next
        self.size -= 1
        return value



q = Queue()
q.enqueue('first')
q.enqueue('second')
q.enqueue('third')
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())


s = Stack()
s.push('first')
s.push('second')
s.push('third')
print(s.pop())
print(s.pop())
print(s.pop())
