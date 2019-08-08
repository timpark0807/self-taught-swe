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
        return self.head is None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            return 'Queue is empty!'
        else:
            value = self.head
            self.head = self.head.next
            self.size -= 1
            return value


q = Queue()
print(len(q))
a = q.dequeue()
print(a)
