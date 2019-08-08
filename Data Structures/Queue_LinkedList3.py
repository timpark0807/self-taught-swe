class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def is_empty(self):
        return self.size == 0
    
    def enqueue(self, data):
        if self.is_empty():
            self.head = Node(data)
            self.tail = self.head
            self.size += 1 
        else:
            new_node = Node(data)
            self.tail.next = new_node
            self.tail = new_node
            self.size += 1 

    def dequeue(self):
        if self.is_empty():
            return print('Queue is empty!')
        else:
            value = self.head.data
            self.head = self.head.next
            self.size -= 1
            return value

    def peek(self):
        if self.is_empty():
            return 'No data'
        else:
            return self.head.data
    

s = Queue()
s.enqueue('2')
print(s.peek())
s.dequeue()
s.enqueue('4')
s.dequeue()
s.dequeue()

