import unittest

class Memo:
    def __init__(self):
        self.cache = {}
    
    def fibb_recursive(self,n):
        if n == 0:
            return 0 
        if n == 1:
            return 1
        
        if n in self.cache:
            return self.cache[n]
        else:
            self.cache[n] = self.fibb_recursive(n-1) + self.fibb_recursive(n-2)
            
        return self.fibb_recursive(n-1) + self.fibb_recursive(n-2)


class TestMemo(unittest.TestCase):
    def test_case(self):
        m = Memo()
        self.assertEqual(m.fibb_recursive(50), 12586269025)
        self.assertEqual(m.fibb_recursive(60), 1548008755920)
        self.assertEqual(m.fibb_recursive(126), 96151855463018422468774568 )
            
if __name__ == '__main__':
    unittest.main()
