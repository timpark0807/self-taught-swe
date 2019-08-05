class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self, head):
        self.head = head
        self.tail = head
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, data):
        self.tail.next = Node(data)
        self.tail = self.tail.next
        self.size += 1
            
    def dequeue(self):
        value = self.head
        self.head = self.head.next
        self.size -= 1
        return value

    def peek(self):
        return self.head.data
    
head = Node('10')
q = Queue(head)
q.enqueue('11')
a = q.peek()
print(a)
q.enqueue('12')
s = q.dequeue()
b = q.peek()
print(b)
