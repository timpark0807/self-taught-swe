import unittest

class Stack:
    def __init__(self):
        self.stack = []
        self.temp = []

    def __repr__(self):
        return repr(self.stack)
        
    def push(self, data):

        if self.is_empty():
            self.stack.append(data)
            
        elif data < self.stack[-1]:
            self.stack.append(data)

        else:
            while self.stack != [] and data > self.stack[-1]:
                self.temp.append(self.stack.pop())

            self.stack.append(data)
            
            while self.temp != []:
                self.stack.append(self.temp.pop())     

    def pop(self):
        if self.is_empty():
            return 'Stack is Empty!'
        else:
            return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return 'Stack is Empty!'
        else:
            return self.stack[-1]

    def is_empty(self):
        return self.stack == []


class TestSolution(unittest.TestCase):
    
    def test_empty_stack(self):
        s = Stack()
        s.push(2)
        s.pop()
        self.assertEqual(s.stack, [])
    
    def test_stack(self):
        s = Stack()
        for num in [10, 8, 11, 13, 1, 15]:
            s.push(num)
        self.assertEqual(s.stack, [15, 13, 11, 10, 8, 1])

if __name__ == '__main__':
    unittest.main()
