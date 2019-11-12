import unittest


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        values = {   'I' : 1, 
                     'V' : 5,
                     'X' : 10,
                     'L' : 50,
                     'C' : 100,
                     'D' : 500,
                     'M' : 1000}
        output = 0
        curr = 0
        
        while curr < len(s):
            if curr < len(s)-1 and values[s[curr]] < values[s[curr+1]]:
                output += (values[s[curr+1]] - values[s[curr]])
                curr += 2
            else:
                output += values[s[curr]]
                curr += 1
                
        return output

class TestSolution(unittest.TestCase):
    
    def setUp(self):
        self.s = Solution()
        
    def tearDown(self):
        self.s = None

    def test_VIII(self):
        answer = self.s.romanToInt('VIII')
        self.assertEqual(answer, 8)
        
    def test_LXII(self):
        answer = self.s.romanToInt('LXII')
        self.assertEqual(answer, 62)

    def test_MCMXCIV(self):
        answer = self.s.romanToInt('MCMXCIV')
        self.assertEqual(answer, 1994)        
        
if __name__ == '__main__':
    unittest.main()
