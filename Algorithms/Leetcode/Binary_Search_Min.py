import unittest

def binary_search_min(arr, key):

    left = 0
    right = len(arr)-1
    global_min = arr[-1]
    global_answer = 0 
    
    while left <= right:
        mid = (left+right) // 2
        curr_min = abs(key - arr[mid])
        if curr_min < global_min:
            global_answer = arr[mid]
            global_min = curr_min

        if arr[mid] == key:
            return arr[mid]

        elif arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1
            
    return global_answer


class Test(unittest.TestCase):
    
    def setUp(self):
        self.arr = [10, 20, 25, 30, 40, 50, 55]
        
    def test_one(self):
        self.assertEqual(binary_search_min(self.arr, 37), 40)
        self.assertEqual(binary_search_min(self.arr, 60), 55)
        self.assertEqual(binary_search_min(self.arr, 5), 10)
        self.assertEqual(binary_search_min(self.arr, 20), 20)
        self.assertEqual(binary_search_min(self.arr, 21), 20)

if __name__ == '__main__':
    unittest.main()
"""
key = 37
curr_min = 50 - 30 = 20
global_min = min(20, 7) -> 7

                                r
                                l 
arr = [10, 20, 25, 30, 40, 50, 55]
        0   1   2   3   4   5   6
                                m
"""
