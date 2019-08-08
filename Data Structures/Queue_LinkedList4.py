class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return repr(self.data)
    
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        new_node = Node(value) 
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty!'
        else:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value

    def peek(self):
        if self.is_empty():
            return 'Queue is empty!'
        else:
            return self.head.data

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(6)
print(len(q))
print(q.tail)

