import unittest

"""
Simple module to improve my understanding of recursion.

find_num checks if a number exists in an unsorted array by calling r_search.

r_search will check if left/right pointers are equal to the target.
    If Equal: return True
    If False: Shrink the search space from the left and right

Base Case is when left pointer passes the right pointer.
"""

class Solution:
    
    def find_num(self, arr, n):
        return self.r_search(arr, n, 0, len(arr) -1)
        
    def r_search(self, arr, target, left, right):
        if left > right:
            return False
        if target == arr[left]:
            return True
        if target == arr[right]:
            return True
        return self.r_search(arr, target, left+1, right-1)
        
    
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None
        
    def test_valid(self):
        arr = [5, 3, 2, 9, 7, 8]
        ans = self.s.find_num(arr, 8)
        self.assertTrue(ans)

    def test_invalid(self):
        arr = [5, 3, 2, 9, 7, 8]
        ans = self.s.find_num(arr, 99)
        self.assertFalse(ans)

if __name__ == '__main__':
    unittest.main()
