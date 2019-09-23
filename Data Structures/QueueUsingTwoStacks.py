class Stack:
    def __init__(self):
        """Initialize an empty stack"""
        self.items = []

    def push(self, item):
        """Push a new item onto the stack"""
        self.items.append(item)
        
    def pop(self):
        """Remove and return the last item"""
        # If the stack is empty, return None
        # (it would also be reasonable to throw an exception)
        if not self.items:
            return None

        return self.items.pop()
    
    def peek(self):
        """Return the last item without removing it"""
        if not self.items:
            return None
        return self.items[-1]


class Queue:
    def __init__(self):
        """Initialize an empty stack"""
        self.stack1 = Stack()
        
    def dequeue(self):
        if not self.stack1:
            return None
        return self.stack1.pop()
    
    def enqueue(self, value):
        stack2 = Stack()

        if self.stack1.items == []:
            stack2.push(value)
        else:
            while self.stack1.items != []:
                stack2.push(self.stack1.pop())
            stack2.push(value)

        while stack2.items != []:
            self.stack1.push(stack2.pop())
        
if __name__ == '__main__':
    q = Queue()
    q.enqueue(3)
    q.enqueue(2)
    q.enqueue(1)
    q.enqueue('go')
    print(q.stack1.items)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
