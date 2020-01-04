import unittest
from .Stack import stack

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

    
