class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for char in S:
            if char == '(':
                stack.append(0) 
                continue
                
            if stack[-1] == 0:
                stack[-1] = 1 
            else:
                curr = 0 
                while stack[-1] != 0:
                    curr += stack.pop()
                stack.pop() 
                stack.append(curr * 2)

        return sum(stack) 

import unittest

class TestSolution(unittest.TestCase):
    def test_one(self):
        answer = Solution().scoreOfParentheses("()")
        expected = 1
        self.assertEqual(answer, expected)
        

if __name__=='__main__':
    unittest.main() 
