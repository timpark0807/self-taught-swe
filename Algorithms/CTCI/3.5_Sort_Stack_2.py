import unittest

class Stack:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, data):
        self.s1.append(data)

    def sort(self):
        while self.s1 != []:
            if self.s2 == [] or self.s1[-1] < self.s2[-1]:
                self.s2.append(self.s1.pop())
            else:
                temp = self.s1.pop()
                while self.s2 != [] and temp > self.s2[-1]:
                    self.s1.append(self.s2.pop())
                self.s2.append(temp)
        return self.s2

class TestSolution(unittest.TestCase):
    def test_valid(self):
        s = Stack()
        arr = [15, 5, 8, 1, 3, 25, 88, 7]
        for num in arr:
            s.push(num)
        answer = s.sort()
        self.assertEqual(answer, sorted(arr, reverse=True))
        
if __name__ == '__main__':
    unittest.main()

    
# while s1 != []:
    # append s1.pop() to s2
    # if s1[-1] < s2[-1]
        # temp = s1.pop()
        # s1.append(s2.pop())
        # s1.append(temp)

# while s2 != []:
    # append s2.pop() to s1 
