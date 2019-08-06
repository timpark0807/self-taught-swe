class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return self.data

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    
    def enQueue(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.tail = self.head
            self.size += 1
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next
            self.size += 1

    def deQueue(self):
        if self.is_empty():
            return print('Queue is empty')
        else:
            value = self.head
            self.head = self.head.next
            self.size -= 1
            return value

    def length(self):
        return self.size

    def peek(self):
        return self.head

q = Queue()
q.enQueue('1')
q.enQueue('2')
q.enQueue('3')
q.deQueue()
q.deQueue()
q.deQueue()
q.deQueue()
