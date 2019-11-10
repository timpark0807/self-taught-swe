import unittest

class Solution:

    def median_of_arrays(self, arr1, arr2):
        p1, p2 = 0, 0
        new_arr = []
        
        while p1 < len(arr1) and p2 < len(arr2):
            if arr1[p1] <= arr2[p2]:
                new_arr.append(arr1[p1])
                p1 += 1
            else:
                new_arr.append(arr2[p2])
                p2 += 1

        new_arr.extend(arr1[p1:])
        new_arr.extend(arr2[p2:])

        low, high = 0, len(new_arr) - 1

        while low <= high:
            if low == high:
                return new_arr[low]
            
            low += 1
            high -=1

        return (new_arr[low] + new_arr[high]) / 2



class TestSolution(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def test_even_median(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4, 6]

        answer = self.s.median_of_arrays(arr1, arr2)
        self.assertEqual(answer, 3.5)


    def test_odd_median(self):
        arr1 = [1, 3, 5]
        arr2 = [2, 4]

        answer = self.s.median_of_arrays(arr1, arr2)
        self.assertEqual(answer, 3)

        
if __name__ == '__main__':
    unittest.main()
    
