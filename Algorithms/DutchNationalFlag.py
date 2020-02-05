import unittest

def DutchNationalFlag(arr):
    """
    Implementation of the classic Dutch National Flag problem.

    Time  : O(n)
    Space : O(1)
    """
    left, right = 0, len(arr)- 1
    i = 0

    while i <= right:
        if arr[i] == 2:
            arr[i], arr[right] = arr[right], arr[i]
            right -= 1
        elif arr[i] == 0:
            arr[i], arr[left] = arr[left], arr[i]
            left += 1
            i += 1
        else:
            i += 1
            
    return arr

class Test(unittest.TestCase):
    def test_valid(self):
        valid = [0, 0, 1, 1, 2, 2]
        arrs = [[2, 1, 1, 0, 0, 2],
                [2, 2, 1, 1, 0, 0],
                [1, 2, 0, 2, 1, 0]]
        for arr in arrs:
            self.assertEqual(DutchNationalFlag(arr), valid)

if __name__ == '__main__':
    unittest.main()
