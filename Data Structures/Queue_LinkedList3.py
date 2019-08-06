class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self, head):
        self.head = head
        self.tail = head

    def enqueue(self, data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        value = self.head.data
        self.head = self.head.next
        return value
    
    def peek(self):
        return self.head.data
    
head = Node('1')
s = Queue(head)
print(s.peek())
s.enqueue('2')
s.dequeue()
print(s.peek())

s.enqueue('3')
s.dequeue()

print(s.peek())
