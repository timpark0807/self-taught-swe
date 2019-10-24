import unittest

class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, data):
        self.stack1.append(data)

    def dequeue(self):
        if self.stack2 == []:
            while self.stack1 != []:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

class TestSolution(unittest.TestCase):

    def test_valid(self):
        q = MyQueue()
        output = []
        q.enqueue(10)
        q.enqueue(20)
        output.append(q.dequeue())
        q.enqueue(30)
        output.append(q.dequeue())
        output.append(q.dequeue())
        self.assertEqual(output, [10, 20, 30])

if __name__ == '__main__':
    unittest.main()
        
    

                


    
