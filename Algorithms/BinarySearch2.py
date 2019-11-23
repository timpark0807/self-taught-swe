import unittest

class Solution:
    def binary_search_iter(self, arr, target):
        left = 0
        right = len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False
                
    def binary_search_recur(self, arr, target, left, right):
        if left < right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                return self.binary_search_recur(arr, target, left, mid-1)
            else:
                return self.binary_search_recur(arr, target, mid+1, right)
        return False

    def binary_search_left_most(self, arr, target):
        left = 0
        right = len(arr) -1
        answer = -1 
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                answer = mid
                right = mid-1
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return answer

    def binary_search_right_most(self, arr, target):
        left = 0
        right = len(arr) - 1
        answer = -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                answer = mid
                left = mid + 1
            elif arr[mid] > target:
                right -= 1
            else:
                left += 1                
        return answer

class Test(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        
    def tearDown(self):
        self.s = None
        
    def test_standard_iter(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(self.s.binary_search_iter(arr, 6), 6)
        
    def test_standard_recur(self):
        arr = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(self.s.binary_search_recur(arr, 6, 0, 7), 6)

    def test_left_most(self):
        #      0  1  2  3  4  5  6  7  8  9  10
        arr = [0, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7]
        #         l
        #         m
        #     r
        self.assertEqual(self.s.binary_search_left_most(arr, 1), 1)

    def test_right_most(self):
        #      0  1  2  3  4  5  6  7  8  9  10
        arr = [0, 1, 1, 1, 1, 2, 3, 4, 5, 6, 7]
        #         l
        #         m
        #     r
        self.assertEqual(self.s.binary_search_right_most(arr, 1), 4)

if __name__ == '__main__':
    unittest.main()
