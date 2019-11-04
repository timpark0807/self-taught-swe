import unittest


class Solution:
    def trap(self, heights):
        """
        input : list of integers (representing heights) 
        output : integer (representing volume of trapped water)

        
                   0  1  2  3  4  5  6  7  8  9 
        heights = [2, 1, 0, 1, 3, 0, 3, 0, 1, 2]
                                     l
                                              r
                   
        pv = 2 * (4 - 0 - 1) = 6 
        bv = 0  
        
        for i in range(left + 1, right) -> (1, 4) -> [1, 2, 3]
            bv = bv + heights[1] ->  0 + 1 = 1
            bv = bv + heights[2] ->  1 + 0 = 1
            bv = bv + heights[3] ->  1 + 1 = 2
        bv = 2
  $$    volume = pv - bv = 6 - 2 = 4


        pv = 3 * (6 - 4 - 1) = 3 
        bv = 0  
        for i in range(left+1, right) -> (5, 6) -> [5]
            bv = bv + heights[5] ->  0 + 0 = 0
        bv = 0
        
  $$    volume = pv - bv = 3 - 0 = 3

        pv = 2 * (9-6-1) = 4
        bv = 0
        for i in range(left+1, right) -> (7, 9) -> [7, 8]
            bv = bv + heights[7] -> 0 + 0 = 0
            bv = bv + heights[8] -> 0 + 1 = 1

  $$    volume = pv - bv = 4 - 1 = 3 
        
        """
        left = 0
        right = 0 
        volume = 0
        
        while right + 1 < len(heights):
            left = right
            right = left + 1

            # Set current window
            while right + 1 < len(heights) and heights[left] > heights[right]:
                right += 1

            possible_volume = min(heights[left], heights[right]) * (right - left - 1)

            blocked_volume = 0
            
            for i in range(left + 1, right):
                blocked_volume += heights[i]

            volume += (possible_volume - blocked_volume)

        return volume 


class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        self.s = None

    def test_one(self):
        heights = [3, 0, 3]
        answer = self.s.trap(heights)
        self.assertEqual(answer, 3)
        
    def test_two(self):
        heights = [2, 1, 0, 1, 3]
        answer = self.s.trap(heights)
        self.assertEqual(answer, 4)
        
    def test_one_plus_two(self):
        heights = [2, 1, 0, 1, 3, 0, 3]
        answer = self.s.trap(heights)
        self.assertEqual(answer, 7)

    def test_four(self):
        heights = [3, 0, 1, 2]
        answer = self.s.trap(heights)
        self.assertEqual(answer, 3)

    def test_one_plus_two_plus_four(self):
        heights = [2, 1, 0, 1, 3, 0, 3, 0, 1, 2]
        answer = self.s.trap(heights)
        self.assertEqual(answer, 10)
        
    def test_leetcode(self):
        heights = [0,1,0,2,1,0,1,3,2,1,2,1]
        answer = self.s.trap(heights)
        self.assertEqual(answer, 6)        
        
        
if __name__ == '__main__':
    unittest.main()



