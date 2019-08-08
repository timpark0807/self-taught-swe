class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.last = None

    def is_empty(self):
        return self.head == None 
    
    def traversal(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def enQueue(self, data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def deQueue(self):
        if self.head is None:
            return
        else:
            answer = self.head
            self.head = self.head.next 
            return answer


q = Queue()
q.enQueue('1')
q.enQueue('2')
q.enQueue('3')
q.enQueue('4')
q.enQueue('5')
q.traversal()
print('*' * 30)
q.deQueue()
q.traversal()
