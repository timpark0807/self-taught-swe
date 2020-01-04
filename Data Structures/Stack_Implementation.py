import unittest

class Stack:
    
    def __init__(self):
        self.items = []
        self.size = 0

    def __len__(self):
        return self.size

    def __str__(self):
        return f'{self.items}'

    def is_empty(self):
        return self.size == 0
    
    def push(self, val):
        self.items.append(val)
        self.size += 1

    def peek(self):
        if self.is_empty():
            return 'Empty Stack'
        else:
            return self.items[-1]

    def pop(self):
        if self.is_empty():
            return 'Empty Stack'
        else:
            self.size -= 1
            return self.items.pop()

class MinStack(Stack):

    def __init__(self):
        super().__init__()
        self.minstack = []

    def push(self, val):
        self.items.append(val)
        self.size += 1
        if len(self.minstack) == 0 or val < self.minstack[-1]:
            self.minstack.append(val)

    def pop(self):
        if self.is_empty():
            return None
        ans = self.items.pop()
        if ans == self.get_min():
            self.minstack.pop()
        self.size -= 1
        return ans
        
    def get_min(self):
        if len(self.minstack) == 0:
            return None
        else:
            return self.minstack[-1]
    
        

ms = MinStack()
ms.push(10)
ms.push(3)
ms.push(7)
ms.push(1)
print(ms.get_min())
print(ms.pop())
print(ms.get_min())
print(ms)
print(ms.minstack)

class TestStack(unittest.TestCase):
    
    def setUp(self):
        self.stack = Stack()
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        
    def tearDown(self):
        self.stack = None

    def test_size(self):
        self.assertEqual(len(self.stack), 3)
        self.stack.pop()
        self.assertEqual(len(self.stack), 2)

    def test_is_empty(self):
        self.assertFalse(self.stack.is_empty())
        self.stack.pop()
        self.stack.pop()
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())

    def test_peek(self):
        ans = self.stack.peek()
        self.assertEqual(ans, 3)

    def test_push(self):
        self.stack.push(4)
        self.assertEqual(len(self.stack), 4)

    def test_pop(self):
        self.assertEqual(self.stack.pop(), 3)
        self.assertEqual(self.stack.pop(), 2)
        self.assertEqual(self.stack.pop(), 1)


if __name__ == '__main__':
    unittest.main()

    
